from defichain.transactions.defitx import PoolSwap, CompositeSwap, AddPoolLiquidity, RemovePoolLiquidity
from defichain.transactions.utils import Converter
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Pool:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def poolswap(self, addressFrom: str, tokenFrom: "str | int", amountFrom: "float | int", addressTo: str,
                 tokenTo: "str | int", maxPrice: "float | int", inputs=[]) -> Transaction:
        """
        Creates a pool swap transaction with the specified data

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

        defiTx = PoolSwap(addressFrom, tokenFrom, amountFrom, addressTo, tokenTo, maxPrice)
        return self._builder.build_defiTx(0, defiTx, inputs)

    def compositeswap(self, addressFrom: str, tokenFrom: "str | int", amountFrom: "float | int", addressTo: str,
                      tokenTo: "str | int", maxPrice: "float | int", pools: [], inputs=[]) -> Transaction:
        """
        Creates a composite swap transaction with the specified data

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
        :param pools: (required) specification of all pools through which the swap should take place
        :type pools: [str]
        :param inputs: (optional) Inputs
        :type inputs: TxInput
        :return: Transaction
        """

        # Convert Float to Integer
        amountFrom = Converter.float_to_int(amountFrom)
        maxPrice = Converter.float_to_int(maxPrice)

        defiTx = CompositeSwap(addressFrom, tokenFrom, amountFrom, addressTo, tokenTo, maxPrice, pools)
        return self._builder.build_defiTx(0, defiTx, inputs)

    def addpoolliquidity(self, addressAmount: {}, shareAddress: str, inputs=[]) -> Transaction:
        """
        Creates a add pool liquidity transaction with the specified data

        :param addressAmount: (required) AddressAmount
        :type addressAmount: AddressAmount
        :param shareAddress: (required) the address where the pool tokens are sent to
        :type shareAddress: str
        :param inputs: (optional) Inputs
        :type inputs: TxInput
        :return: Transaction
        """

        # Convert Float to Integer
        addressAmount = Converter.addressAmount_float_to_int(addressAmount)

        defiTx = AddPoolLiquidity(addressAmount, shareAddress)
        return self._builder.build_defiTx(0, defiTx, inputs)

    def removepoolliquidity(self, addressFrom: str, amount: str, inputs=[]):
        """
        Creates a remove pool liquidity transaction with the specified data

        :param addressFrom: (required) the address to remove the pool tokens from
        :type addressFrom: str
        :param amount: (required) value and liquidity tokens which should be removed: Amount
        :type amount: str
        :param inputs: (optional) Inputs
        :type inputs: TxInput
        :return: Transaction
        """

        # Convert Float to Integer
        amount = f"{Converter.float_to_int(float(amount.split('@')[0]))}@{amount.split('@')[1]}"

        defiTx = RemovePoolLiquidity(addressFrom, amount)
        return self._builder.build_defiTx(0, defiTx, inputs)

