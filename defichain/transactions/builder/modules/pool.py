from defichain.transactions.defitx import Poolswap
from defichain.transactions.utils import Converter
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Pool:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def poolswap(self, addressFrom: str, tokenFrom: "str | int", amountFrom: "float | int", addressTo: str,
                 tokenTo: "str | int", maxPrice: "float | int", inputs=[]) -> Transaction:
        """
        Creates a poolswap transaction with given metadata

        :param addressFrom: (required) the address where the tokens are located
        :type addressFrom: str
        :param tokenFrom: (required) the token that should be exchanged
        :type tokenFrom: str | int
        :param amountFrom: (required) the amount that should be exchanged
        :type amountFrom: float | int
        :param addressTo: (required) the address where the exchanged tokens are sent to
        :type addressTo: str
        :param tokenTo: (required) the token to change into
        :type tokenTo: str | int
        :param maxPrice: (required) maximum acceptable price
        :type maxPrice: float | int
        :param inputs: (optional) Inputs
        :type inputs: TxInput
        :return: Transaction
        """
        # Convert Float to Integer
        amountFrom = Converter.float_to_int(amountFrom)
        maxPrice = Converter.float_to_int(maxPrice)

        defiTx = Poolswap(addressFrom, tokenFrom, amountFrom, addressTo, tokenTo, maxPrice)
        return self._builder.build_defiTx(0, defiTx, inputs)

    #def addpoolliquidity(self, addressAmount: {}, shareAddress: str) -> Transaction:
        #defiTx = DefiTx.pool.addpoolliquidity(addressAmount, shareAddress)
        #return self._builder.build_defiTx(0, defiTx)
        #pass

