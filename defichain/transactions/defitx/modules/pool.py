from defichain.transactions.address import Address
from defichain.transactions.utils import *
from defichain.transactions.constants import DefiTxType


class Pool:
    def __init__(self, defitx):
        self._defitx = defitx

    def poolswap(self, addressFrom: str, tokenFrom: str or int, amountFrom: int, addressTo: str, tokenTo: str or int,
                 maxPrice: int) -> str:
        """
        Builds the defi transaction for a poolswap

        :param addressFrom: (required) the address where the tokens are located
        :param tokenFrom: (required) the token that should be changed
        :param amountFrom: (required) the amount that should be changed
        :param addressTo: (required) the address where the exchanged tokens are sent to
        :param tokenTo: (required) the token to change into
        :param maxPrice: (required) maximum acceptable price
        :return: "hex" (string) -- returns the finished defi transaction
        """
        addressFrom = hex_to_bytes(Address.from_address(addressFrom).get_script_public_key())
        tokenFrom = hex_to_bytes(int_to_hex(tokenFrom, 1))
        amountFrom = hex_to_bytes(int_to_hex(amountFrom, 8))
        addressTo = hex_to_bytes(Address.from_address(addressTo).get_script_public_key())
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

        return self._defitx.package_defitx(result)

    def compositeswap(self):
        pass

    def addpoolliquidity(self, addressAmount: {}, shareAddress: str) -> str:
        """
        Builds the defi transaction for addpoolliquidity

        :param addressAmount: (required) :ref:`Node Address Amount`
        :param shareAddress: (required) the address where the pool shares are placed
        :return: "hex" (string) -- returns the finished defi transaction
        """

        number_of_entries = int_to_bytes(len(addressAmount), 1)

        result = hex_to_bytes(DefiTxType.OP_DEFI_TX_POOL_ADD_LIQUIDITY)
        result += number_of_entries

        for address in addressAmount:
            address_script = hex_to_bytes(Address.from_address(address).get_script_public_key())
            length_of_script = int_to_bytes(len(address_script), 1)
            result += length_of_script + address_script

            number_of_tokens = int_to_bytes(len(addressAmount[address]), 1)
            result += number_of_tokens
            for amount in addressAmount[address]:
                split = amount.split('@')
                value = int_to_bytes(int(split[0]), 8)
                token = int_to_bytes(int(split[1]), 4)
                result += token + value

        share_address_script = hex_to_bytes(Address.from_address(shareAddress).get_script_public_key())
        length_of_share_script = int_to_bytes(len(share_address_script), 1)
        result += length_of_share_script + share_address_script

        return self._defitx.package_defitx(result)

    def removepoolliquidity(self):
        pass

    def createpoolpair(self):
        pass

    def updatepoolpair(self):
        pass



