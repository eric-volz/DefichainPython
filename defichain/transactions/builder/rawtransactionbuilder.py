from defichain import Account
from defichain.transactions.utils import calculate_fee_for_unsigned_transaction
from defichain.exceptions.transactions import TxBuilderError

from defichain.transactions.remotedata.remotedata import RemoteData
from defichain.transactions.rawtransactions import Transaction, TxInput, TxOutput, TxDefiOutput


class RawTransactionBuilder:

    @staticmethod
    def new_transaction() -> Transaction:
        return Transaction([], [])

    def __init__(self, address: str, account: Account, datasource: RemoteData):
        self._address, self._account, self._datasource = None, None, None
        self.set_address(address)
        self.set_account(account)
        self.set_datasource(datasource)

    # Build Transaction
    def build_transaction_inputs(self) -> Transaction:
        tx = self.new_transaction()
        for input in self.get_datasource().get_unspent(self.get_address()):
            tx.add_input(TxInput(input["txid"], input["index"], self.get_address(), input["value"]))
        return tx

    def build_defitx(self, value: int, defitx: str) -> Transaction:
        # TODO: Remove static fee with dynamic fee
        tx = self.build_transaction_inputs()
        defitx_output = TxDefiOutput(value, defitx)
        change_output = TxOutput(tx.get_inputs_value(), self.get_address())
        tx.add_output(defitx_output)
        tx.add_output(change_output)
        fee = calculate_fee_for_unsigned_transaction(tx)

        # Subtract fee from output
        tx.get_outputs()[1].set_value(tx.get_outputs()[1].get_value() - fee)

        self.sign(tx)
        return tx

    def sign(self, tx: Transaction) -> None:
        tx.sign([self.get_account().wif()])

    # Get Information
    def get_address(self) -> str:
        return self._address

    def get_account(self) -> Account:
        return self._account

    def get_datasource(self) -> "RemoteData":
        return self._datasource

    # Set Information
    def set_address(self, address: str) -> None:
        self._address = address

    def set_account(self, account: Account) -> None:
        self._account = account

    def set_datasource(self, datasource: RemoteData) -> None:
        self._datasource = datasource
