from defichain import Account
from defichain.exceptions.transactions import TxBuilderError, NotYetSupportedError

from defichain.transactions.address import Address
from defichain.transactions.constants import AddressTypes, DefiTxType
from defichain.networks import Network
from defichain.transactions.remotedata.remotedata import RemoteData
from defichain.transactions.rawtransactions import Transaction, TxInput, TxP2WPKHInput, TxP2SHInput, TxAddressOutput, \
    TxDefiOutput, estimate_fee
from defichain.transactions.defitx.modules.basedefitx import BaseDefiTx


class RawTransactionBuilder:

    @staticmethod
    def new_transaction() -> Transaction:
        return Transaction([], [])

    def __init__(self, address: str, account: Account, dataSource: RemoteData, feePerByte: float):
        self._address, self._account, self._dataSource, self._feePerByte = None, None, None, None
        self.set_address(address)
        self.set_account(account)
        self.set_dataSource(dataSource)
        self.set_feePerByte(feePerByte)

    # Build Transaction
    def build_transactionInputs(self, inputs=[]) -> Transaction:
        tx = self.new_transaction()

        if inputs or self.get_dataSource() is None:
            tx.set_inputs(inputs)
        else:
            for input in self.get_dataSource().get_unspent(self.get_address()):
                address = Address.from_scriptPublicKey(self.get_account().get_network(), input["scriptPubKey"])
                # Build P2PKH Input
                if address.get_addressType() == AddressTypes.P2PKH:
                    raise NotYetSupportedError()
                # Build P2SH Input
                elif address.get_addressType() == AddressTypes.P2SH:
                    tx.add_input(TxP2SHInput(input["txid"], input["vout"], self.get_account().get_p2wpkh(),
                                             input["value"]))
                # Build P2WPKH Input
                elif address.get_addressType() == AddressTypes.P2WPKH:
                    tx.add_input(TxP2WPKHInput(input["txid"], input["vout"], self.get_address(), input["value"]))
            # Check Inputs for masternode collateral
            tx.set_inputs(self.checkMasternodeInputs(tx.get_inputs()))
        if tx.get_inputs() == []:
            raise TxBuilderError(f"Given address: {self._address} has no unspent inputs. Check your builder object!")
        return tx

    def build_defiTx(self, value: int, defiTx: BaseDefiTx, inputs=[], **additionalData) -> Transaction:
        tx = self.build_transactionInputs(inputs)

        # Check for errors in Inputs
        # Check masternode creation errors
        if defiTx.get_defiTxType() == DefiTxType.OP_DEFI_TX_CREATE_MASTER_NODE:
            if tx.get_inputsValue() - value < 2000000000000:
                raise TxBuilderError("The address holds not enough DFI to create a masternode")
            if tx.get_inputsValue() < 2001000000000:
                raise TxBuilderError("The address holds not enough DFI to pay the 10 DFI fee to create a masternode")
        if tx.get_inputsValue() - value < 0:
            raise TxBuilderError("The value of the output is bigger then the value of the input")
        # Adding Outputs to the transaction
        # DefiTx Output
        defitxOutput = TxDefiOutput(value, defiTx)
        tx.add_output(defitxOutput)

        # Masternode Output
        if defiTx.get_defiTxType() == DefiTxType.OP_DEFI_TX_CREATE_MASTER_NODE:
            masternodeOutput = TxAddressOutput(2000000000000, self.get_address())
            value = masternodeOutput.get_value() + value
            tx.add_output(masternodeOutput)

        # Change Output
        changeOutput = TxAddressOutput(tx.get_inputsValue() - value, self.get_address())
        tx.add_output(changeOutput)

        # AccountToUtxos Output
        if defiTx.get_defiTxType() == DefiTxType.OP_DEFI_TX_ACCOUNT_TO_UTXOS:
            addressAmountTo = additionalData["addressAmountTo"]

            # Build Outputs for Utxos
            for address in addressAmountTo:
                outputValue = int(addressAmountTo[address].split("@")[0])
                tx.add_output(TxAddressOutput(outputValue, address, 0))

        # Calculate fee
        fee = estimate_fee(tx, self.get_feePerByte())

        # Subtract fee from output
        value = changeOutput.get_value() - fee
        if value < 0:
            raise TxBuilderError("The used address has not enough UTXO to pay the transaction fee")
        changeOutput.set_value(value)

        # Sign and Return
        self.sign(tx)
        return tx

    def sign(self, tx: Transaction) -> None:
        tx.sign(self.get_account().get_network(), [self.get_account().get_privateKey()])

    def checkMasternodeInputs(self, inputs: [TxInput]) -> []:
        newInputs = []
        for input in inputs:
            # Check Value
            if input.get_value() == 2000000000000:
                # Check transaction txid with data source
                if self.get_dataSource().check_masternode(input.get_txid()):
                    continue
            newInputs.append(input)
        return newInputs

    # Get Information
    def get_address(self) -> str:
        return self._address

    def get_addressType(self) -> str:
        return Address.from_address(self.get_address()).get_addressType()

    def get_account(self) -> Account:
        return self._account

    def get_dataSource(self) -> "RemoteData":
        return self._dataSource

    def get_feePerByte(self) -> float:
        return self._feePerByte

    def get_network(self) -> Network:
        return self.get_account().get_network()

    # Set Information
    def set_address(self, address: str) -> None:
        self._address = address

    def set_account(self, account: Account) -> None:
        self._account = account

    def set_dataSource(self, dataSource: RemoteData) -> None:
        self._dataSource = dataSource

    def set_feePerByte(self, feePerByte: float) -> None:
        self._feePerByte = feePerByte
