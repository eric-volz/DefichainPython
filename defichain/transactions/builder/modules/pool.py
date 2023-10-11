from defichain.transactions.defitx import PoolSwap, CompositeSwap, AddPoolLiquidity, RemovePoolLiquidity
from defichain.transactions.utils import Converter
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Pool:
    """
    **The methods of this module create pool transactions**

    1. **poolswap**: create a pool swap transaction

    2. **compositeswap**: create a composite swap transaction

    3. **addpoolliquidity**: create an add pool liquidity transaction

    4. **removepoolliquidity**: create a remove pool liquidity transaction
    """

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def poolswap(self, addressFrom: str, tokenFrom: "str | int", amountFrom: "float | int", addressTo: str,
                 tokenTo: "str | int", maxPrice: "float | int", inputs=[]) -> Transaction:
        """
        Creates a pool swap transaction with the specified data

        >>> builder.pool.poolswap("df1qm8fgh8l9sa336jrdf40sghgthvsmagagc4tq9x", "BTC", 0.00001, "df1qm8fgh8l9sa336jrdf40sghgthvsmagagc4tq9x", "DFI", 9999999999) # create a poolswap transaction

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
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: :ref:`Transaction Advanced RawTransactions Transaction`
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

        >>> builder.pool.compositeswap("df1qm8fgh8l9sa336jrdf40sghgthvsmagagc4tq9x", "BTC", 0.00001, "df1qm8fgh8l9sa336jrdf40sghgthvsmagagc4tq9x", "TSLA", 9999999999, ["BTC-DFI", "DUSD-DFI", "TSLA-DUSD"]) # create a compositeswap transaction

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
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: :ref:`Transaction Advanced RawTransactions Transaction`
        """

        # Convert Float to Integer
        amountFrom = Converter.float_to_int(amountFrom)
        maxPrice = Converter.float_to_int(maxPrice)

        defiTx = CompositeSwap(addressFrom, tokenFrom, amountFrom, addressTo, tokenTo, maxPrice, pools)
        return self._builder.build_defiTx(0, defiTx, inputs)

    def addpoolliquidity(self, addressAmountFrom: {}, shareAddress: str, inputs=[]) -> Transaction:
        """
        Creates an add pool liquidity transaction with the specified data

        >>> builder.pool.addpoolliquidity({"df1qw8c57c3c4u7k2h4gv2d5x4jr4qgq6cugg33g6e": ["1@DFI", "0.0001@BTC"]}, "df1qw8c57c3c4u7k2h4gv2d5x4jr4qgq6cugg33g6e") # creates a add pool liquidity transaction

        :param addressAmountFrom: (required) json with specified address and amount to send
        :type addressAmountFrom: :ref:`Transactions AddressAmount`
        :param shareAddress: (required) the address where the pool tokens are sent to
        :type shareAddress: str
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: :ref:`Transaction Advanced RawTransactions Transaction`
        """

        # Convert Float to Integer
        addressAmount = Converter.addressAmount_float_to_int(addressAmountFrom)

        defiTx = AddPoolLiquidity(addressAmount, shareAddress)
        return self._builder.build_defiTx(0, defiTx, inputs)

    def removepoolliquidity(self, addressFrom: str, amount: str, inputs=[]) -> "Transaction":
        """
        Creates a remove pool liquidity transaction with the specified data

        >>> builder.pool.removepoolliquidity("df1qw8c57c3c4u7k2h4gv2d5x4jr4qgq6cugg33g6e", "0.0001@BTC-DFI") # creates a remove pool liquidity transaction

        :param addressFrom: (required) the address to remove the pool tokens from
        :type addressFrom: str
        :param amount: (required) string with amount and token separated by an @
        :type amount: :ref:`Transactions Amounts`
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: :ref:`Transaction Advanced RawTransactions Transaction`
        """

        # Convert Float to Integer
        amount = f"{Converter.float_to_int(float(amount.split('@')[0]))}@{amount.split('@')[1]}"

        defiTx = RemovePoolLiquidity(addressFrom, amount)
        return self._builder.build_defiTx(0, defiTx, inputs)

