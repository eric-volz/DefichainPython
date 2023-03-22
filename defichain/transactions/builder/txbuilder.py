from defichain import Account, Ocean, Node

from defichain.exceptions.transactions import TxBuilderError

from defichain.transactions.remotedata.remotedata import RemoteData
from defichain.transactions.remotedata import RemoteDataOcean, RemoteDataNode

from .rawtransactionbuilder import RawTransactionBuilder
from .modules import *

from defichain.transactions.rawtransactions import Transaction


class TxBuilder:
    """
    This it the main class to build transactions. The transaction will be built with the information provided and
    automatically signed.

    All transactions are created for the given address.
    The account parameter must match the given address and contains the matching private key.

    Through the given data source, all the necessary information is pulled from the blockchain which is
    required to create the transaction. The standard data source is the ocean infrastructure.
    However, this can also be replaced by a Defichain node connection.
    If no data source is specified, the appropriate inputs must be passed to the individual methods.

    By default, a fee of one satoshi per byte is used.

    Input Handling:
        All inputs of an address are always combined to one output.

    :param address: (required) address for which the transaction is created
    :type address: str
    :param account: (required) account object belonging to the given address
    :type account: Account
    :param dataSource: (required) data source for creating the transaction
    :type dataSource: Ocean | Node | None
    :param feePerByte: (optional) approximate fee paid per byte
    :type feePerByte: float
    """
    def __init__(self, address: str, account: Account, dataSource: "Ocean | Node | None", feePerByte=1.0):
        self._address, self._account, self._dataSource, self._feePerByte = None, None, None, None
        self._set_address(address)
        self._set_account(account)
        self._set_dataSource(dataSource)
        self._set_feePerByte(feePerByte)

        self._builder = RawTransactionBuilder(self.get_address(), self.get_account(), self.get_dataSource(),
                                              self.get_feePerByte())

        self.utxo = UTXO(self._builder)
        self.accounts = Accounts(self._builder)
        self.pool = Pool(self._builder)

        # Verify if address is represented by provided account
        self._verify()

    # Methods
    def send_tx(self, tx: "Transaction | str", maxFeeRate: float = None) -> str:
        """
        Broadcasts the created transaction to the blockchain using the provided data source

        :param tx: (required) transaction object or serialized transaction string
        :type tx: Transaction | str
        :param maxFeeRate: (optional) maximum fee rate
        :type maxFeeRate: float
        :return: "hex" (str) - the transaction hash
        """
        if self.get_dataSource() is not None:
            if isinstance(tx, Transaction):
                if not tx.is_signed():
                    raise TxBuilderError("The transaction cannot be sent because it is not yet signed!")
                return self.get_dataSource().send_tx(tx.serialize(), maxFeeRate)
            elif isinstance(tx, str):
                return self.get_dataSource().send_tx(tx, maxFeeRate)
            else:
                raise TxBuilderError("To send the transaction it has to be an transaction object or an hex string!")
        raise TxBuilderError("The transaction cannot be sent because no data source is given")

    def test_tx(self, tx: "Transaction | str", maxFeeRate: float = None) -> bool:
        """
        Tests if the transaction would be accepted by the blockchain using the data source

        :param tx: (required) transaction object or serialized transaction string
        :type tx: Transaction | str
        :param maxFeeRate: (optional) maximum fee rate
        :type maxFeeRate: float
        :return: bool
        """
        if self.get_dataSource() is not None:
            try:
                if isinstance(tx, Transaction):
                    if not tx.is_signed():
                        raise TxBuilderError("The transaction cannot be sent because it is not yet signed!")
                    self.get_dataSource().test_tx(tx.serialize(), maxFeeRate)
                elif isinstance(tx, str):
                    self.get_dataSource().test_tx(tx, maxFeeRate)
                else:
                    raise TxBuilderError("To send the transaction it has to be an transaction object or an hex string!")
                return True
            except:
                return False
        raise TxBuilderError("The transaction cannot be tested because no data source is given")

    def _verify(self):
        if not (self.get_address() != self.get_account().get_p2pkh() or
                self.get_address() != self.get_account().get_p2sh() or
                self.get_address() != self.get_account().get_p2wpkh()):
            raise TxBuilderError("The given address does not match the given account!")

    def get_inputs_tx(self) -> Transaction:
        """
        Builds a transaction just with the inputs of the address.
        The outputs have to be manually specified.

        :return: Transaction - just with inputs
        """
        return self._builder.build_transactionInputs()

    # Get Information
    def get_address(self) -> str:
        """
        Returns the address specified in the builder

        :return: address (str)
        """
        return self._address

    def get_account(self) -> Account:
        """
        Returns the account specified in the builder

        :return: Account
        """
        return self._account

    def get_dataSource(self) -> "RemoteData":
        """
        Returns the data source specified in the builder

        :return: RemoteData
        """
        return self._dataSource

    def get_feePerByte(self) -> float:
        """
        Returns the fee per byte specified in the builder

        :return: float
        """
        return self._feePerByte

    # Set Information
    def _set_address(self, address: str) -> None:
        self._address = address

    def _set_account(self, account: Account) -> None:
        self._account = account

    def _set_dataSource(self, dataSource: "Ocean | Node | None") -> None:
        if isinstance(dataSource, Ocean):
            self._dataSource = RemoteDataOcean(dataSource)
        elif isinstance(dataSource, Node):
            self._dataSource = RemoteDataNode(dataSource)
        elif dataSource is None:
            self._dataSource = None
        else:
            raise TxBuilderError("The given source is currently not usable")

    def _set_feePerByte(self, feePerByte: float) -> None:
        self._feePerByte = feePerByte


