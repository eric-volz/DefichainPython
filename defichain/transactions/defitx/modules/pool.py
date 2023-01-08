from defichain.transactions.address import Address
from defichain.transactions.utils import *
from defichain.transactions.constants import DefiTxType


class Pool:
    def __init__(self, defitx):
        self._defitx = defitx

    def poolswap(self, addressFrom: str, tokenFrom: str or int, amountFrom: int, addressTo: str, tokenTo: str or int, maxPrice: int):
        addressFrom = hex_to_bytes(Address.from_address(addressFrom).get_script())
        tokenFrom = hex_to_bytes(int_to_hex(tokenFrom, 1))
        amountFrom = hex_to_bytes(int_to_hex(amountFrom, 8))
        addressTo = hex_to_bytes(Address.from_address(addressTo).get_script())
        tokenTo = hex_to_bytes(int_to_hex(tokenTo, 1))
        max_price = hex_to_bytes(int_to_hex(maxPrice, 8))

        length_of_fromAddress_script = int_to_bytes(len(addressFrom), 1)
        length_of_toAddress_script = int_to_bytes(len(addressTo), 1)
        null = hex_to_bytes(int_to_hex(0, 8))

        result = hex_to_bytes(DefiTxType.OP_DEFI_TX_POOL_SWAP)
        result += length_of_fromAddress_script
        result += addressFrom
        result += tokenFrom
        result += amountFrom
        result += length_of_toAddress_script
        result += addressTo
        result += tokenTo
        result += null
        result += max_price

        return self._defitx.package_dftx(result)

