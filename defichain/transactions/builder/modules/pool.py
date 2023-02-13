from defichain.transactions.defitx import DefiTx, Poolswap
from defichain.transactions.address import Address
from defichain.transactions.utils import Converter, Verify, Token
from defichain.transactions.constants import TokenTypes
from defichain.exceptions.transactions import InputError
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Pool:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def poolswap(self, addressFrom: str, tokenFrom: str or int, amountFrom: int or float, addressTo: str,
                 tokenTo: str or int, maxPrice: int or float) -> Transaction:

        defiTx = Poolswap(addressFrom, tokenFrom, amountFrom, addressTo, tokenTo, maxPrice).serialize()
        return self._builder.build_defiTx(0, defiTx)

    def addpoolliquidity(self, addressAmount: {}, shareAddress: str) -> Transaction:
        #defiTx = DefiTx.pool.addpoolliquidity(addressAmount, shareAddress)
        #return self._builder.build_defiTx(0, defiTx)
        pass

