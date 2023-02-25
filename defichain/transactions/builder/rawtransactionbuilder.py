import copy

from defichain import Account
from defichain.exceptions.transactions import TxBuilderError

from defichain.transactions.remotedata.remotedata import RemoteData
from defichain.transactions.rawtransactions import Transaction, TxP2WPKHInput, TxOutput, TxDefiOutput, define_fee
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
        if inputs:
            tx.set_inputs(inputs)
        else:
            for input in self.get_dataSource().get_unspent(self.get_address()):
                tx.add_input(TxP2WPKHInput(input["txid"], input["index"], self.get_address(), input["value"]))
        return tx

    def build_defiTx(self, value: int, defiTx: BaseDefiTx, inputs=[]) -> Transaction:
        tx = self.build_transactionInputs(inputs)
        defitx_output = TxDefiOutput(value, defiTx)
        change_output = TxOutput(tx.get_inputsValue() - value, self.get_address())
        tx.add_output(defitx_output)
        tx.add_output(change_output)

        # Calculate fee
        fee = define_fee(tx, self.get_account().get_network(), [self.get_account().get_privateKey()],
                         self.get_feePerByte())

        # Subtract fee from output
        tx.get_outputs()[1].set_value(tx.get_outputs()[1].get_value() - fee)

        # Sign and Return
        self.sign(tx)
        return tx

    def sign(self, tx: Transaction) -> None:
        tx.sign(self.get_account().get_network(), [self.get_account().get_privateKey()])

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
    def set_address(self, address: str) -> None:
        self._address = address

    def set_account(self, account: Account) -> None:
        self._account = account

    def set_dataSource(self, dataSource: RemoteData) -> None:
        self._dataSource = dataSource

    def set_feePerByte(self, feePerByte: float) -> None:
        self._feePerByte = feePerByte
