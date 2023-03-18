from defichain import Account, Ocean, Node

from defichain.exceptions.transactions import TxBuilderError

from defichain.transactions.remotedata.remotedata import RemoteData
from defichain.transactions.remotedata import RemoteDataOcean, RemoteDataNode

from .rawtransactionbuilder import RawTransactionBuilder
from .modules import *

from defichain.transactions.rawtransactions import Transaction


class TxBuilder:
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

    # Methods
    def send_tx(self, tx: "Transaction | str", maxFeeRate: int = None) -> str:
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

    def test_tx(self, tx: Transaction, maxFeeRate: int = None) -> bool:
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

    def get_inputs_tx(self):
        return self._builder.build_transactionInputs()

    # Get Information
    def get_address(self) -> str:
        return self._address

    def get_account(self) -> Account:
        return self._account

    def get_dataSource(self) -> "RemoteData":
        return self._dataSource

    def get_feePerByte(self) -> float:
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


