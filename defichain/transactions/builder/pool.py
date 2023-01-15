from defichain.transactions.defitx import DefiTx
from .rawtransactionbuilder import RawTransactionBuilder, Transaction


class Pool:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def poolswap(self, addressFrom: str, tokenFrom: str or int, amountFrom: int, addressTo: str, tokenTo: str or int,
                 maxPrice: int) -> Transaction:
        defitx = DefiTx.pool.poolswap(addressFrom, tokenFrom, amountFrom, addressTo, tokenTo, maxPrice)
        return self._builder.build_defitx(0, defitx)