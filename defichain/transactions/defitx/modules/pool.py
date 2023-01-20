from defichain.transactions.address import Address
from defichain.transactions.utils import Converter
from defichain.transactions.constants import DefiTxType


class Pool:
    def __init__(self, defitx):
        self._defitx = defitx

    def poolswap(self, addressFrom: str, tokenFrom: int, amountFrom: int, addressTo: str, tokenTo: int,
                  maxPrice: int) -> str:
        """
        Builds the defi transaction for a poolswap

        :param addressFrom: (required) the address where the tokens are located
        :param tokenFrom: (required) the token that should be exchanged
        :param amountFrom: (required) the amount that should be exchanged
        :param addressTo: (required) the address where the exchanged tokens are sent to
        :param tokenTo: (required) the token to change into
        :param maxPrice: (required) maximum acceptable price
        :return: "hex" (string) -- returns the finished defi transaction
        """

        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(DefiTxType.OP_DEFI_TX_POOL_SWAP)
        addressFrom = Converter.hex_to_bytes(Address.from_address(addressFrom).get_script_public_key())
        tokenFrom = Converter.int_to_bytes(tokenFrom, 1)
        amountFrom = Converter.int_to_bytes(amountFrom, 8)
        addressTo = Converter.hex_to_bytes(Address.from_address(addressTo).get_script_public_key())
        tokenTo = Converter.int_to_bytes(tokenTo, 1)
        maxPrice = Converter.int_to_bytes(maxPrice, 8)

        length_addressFrom = Converter.int_to_bytes(len(addressFrom), 1)
        length_addressTo = Converter.int_to_bytes(len(addressTo), 1)
        null = Converter.int_to_bytes(0, 8)

        # Build PoolSwapDefiTx
        result = defiTxType
        result += length_addressFrom
        result += addressFrom
        result += tokenFrom
        result += amountFrom
        result += length_addressTo
        result += addressTo
        result += tokenTo
        result += null
        result += maxPrice

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

        number_of_entries = Converter.int_to_bytes(len(addressAmount), 1)

        result = Converter.hex_to_bytes(DefiTxType.OP_DEFI_TX_POOL_ADD_LIQUIDITY)
        result += number_of_entries

        for address in addressAmount:
            address_script = Converter.hex_to_bytes(Address.from_address(address).get_script_public_key())
            length_of_script = Converter.int_to_bytes(len(address_script), 1)
            result += length_of_script + address_script

            number_of_tokens = Converter.int_to_bytes(len(addressAmount[address]), 1)
            result += number_of_tokens
            for amount in addressAmount[address]:
                split = amount.split('@')
                value = Converter.int_to_bytes(int(split[0]), 8)
                token = Converter.int_to_bytes(int(split[1]), 4)
                result += token + value

        share_address_script = Converter.hex_to_bytes(Address.from_address(shareAddress).get_script_public_key())
        length_of_share_script = Converter.int_to_bytes(len(share_address_script), 1)
        result += length_of_share_script + share_address_script

        return self._defitx.package_defitx(result)

    def removepoolliquidity(self):
        pass

    def createpoolpair(self):
        pass

    def updatepoolpair(self):
        pass
