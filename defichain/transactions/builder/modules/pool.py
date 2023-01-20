from defichain.transactions.defitx import DefiTx
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

        # Verify Inputs
        Address.from_address(addressFrom)

        if not (Verify.is_str(tokenFrom) or Verify.is_int(tokenFrom)):
            raise InputError("The given token from input is not an string or an integer")

        if not (Verify.is_int(amountFrom) or Verify.is_float(amountFrom)):
            raise InputError("The given amount from input is not an integer or an float")

        Address.from_address(addressTo)

        if not (Verify.is_str(tokenTo) or Verify.is_int(tokenTo)):
            raise InputError("The given token to input is not an string or an integer")

        if not (Verify.is_int(maxPrice) or Verify.is_float(maxPrice)):
            raise InputError("The given max price input is not an integer or an float")

        # Convert Token Symbol and float amount
        # tokenFrom
        if Verify.is_str(tokenFrom):
            if Verify.is_only_number_str(tokenFrom):
                tokenFrom = int(tokenFrom)
            else:
                tokenFrom = int(Token.get_id_from_symbol(tokenFrom, TokenTypes.STANDARD))

        # amountFrom
        if Verify.is_float(amountFrom):
            amountFrom = Converter.float_to_int(amountFrom)

        # tokenTo
        if Verify.is_str(tokenTo):
            if Verify.is_only_number_str(tokenTo):
                tokenTo = int(tokenTo)
            else:
                tokenTo = int(Token.get_id_from_symbol(tokenTo, TokenTypes.STANDARD))

        # maxPrice
        if Verify.is_float(maxPrice):
            maxPrice = Converter.float_to_int(maxPrice)
            print(maxPrice)

        defitx = DefiTx.pool.poolswap(addressFrom, tokenFrom, amountFrom, addressTo, tokenTo, maxPrice)
        return self._builder.build_defitx(0, defitx)

    def addpoolliquidity(self, addressAmount: {}, shareAddress: str) -> Transaction:
        defitx = DefiTx.pool.addpoolliquidity(addressAmount, shareAddress)
        return self._builder.build_defitx(0, defitx)

