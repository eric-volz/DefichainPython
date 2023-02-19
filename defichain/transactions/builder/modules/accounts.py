from defichain.transactions.defitx import DefiTx, Poolswap, UtxosToAccount
from defichain.transactions.address import Address
from defichain.transactions.utils import Converter, Verify, Token
from defichain.transactions.constants import TokenTypes
from defichain.exceptions.transactions import InputError
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Accounts:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def utxostoaccount(self, address: str, amount: int, tokenId: int = 0, inputs=[]) -> Transaction:

        defiTx = UtxosToAccount(address, amount, tokenId)
        return self._builder.build_defiTx(amount, defiTx, inputs)
