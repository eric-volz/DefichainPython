from typing import Any

from defichain.exceptions.transactions import AddressError
from defichain.transactions.constants import DefiTxType
from defichain.transactions.address import Address
from defichain.transactions.utils import Converter, Token, Verify
from .basedefitx import BaseDefiTx
from ..builddefitx import BuildDefiTx


class Poolswap(BaseDefiTx):
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

    @staticmethod
    def deserialize(network: Any, hex: str) -> "Poolswap":
        position = 0

        lengthAddressFrom = Converter.hex_to_int(hex[position: position + 2]) * 2
        position += 2

        addressFrom = Address.from_scriptPublicKey(network, hex[position: position + lengthAddressFrom])
        position += lengthAddressFrom

        tokenFrom = Converter.hex_to_int(hex[position: position + 2])
        position += 2

        amountFrom = Converter.hex_to_int(hex[position: position + 16])
        position += 16

        lengthAddressTo = Converter.hex_to_int(hex[position: position + 2]) * 2
        position += 2

        addressTo = Address.from_scriptPublicKey(network, hex[position: position + lengthAddressTo])
        position += lengthAddressTo

        tokenTo = Converter.hex_to_int(hex[position: position + 2])
        position += 2

        maxPriceInteger = Converter.hex_to_int(hex[position: position + 16])
        position += 16

        maxPriceFraction = str(Converter.hex_to_int(hex[position: position + 16]))
        position += 16

        while len(maxPriceFraction) < 8:
            maxPriceFraction += "0"

        maxPrice = int(str(maxPriceInteger) + maxPriceFraction)

        return Poolswap(addressFrom.get_address(), tokenFrom, amountFrom, addressTo.get_address(), tokenTo, maxPrice)

    def __init__(self, addressFrom: str, tokenFrom: int, amountFrom: int, addressTo: str, tokenTo: int,
                 maxPrice: int):

        self._addressFrom, self._tokenFrom, self._amountFrom, self._addressTo, self._tokenTo, self._maxPrice = None, \
            None, None, None, None, None
        self._network = None
        self.set_addressFrom(addressFrom)
        self.set_tokenFrom(tokenFrom)
        self.set_amountFrom(amountFrom)
        self.set_addressTo(addressTo)
        self.set_tokenTo(tokenTo)
        self.set_maxPrice(maxPrice)

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(DefiTxType.OP_DEFI_TX_POOL_SWAP)
        addressFrom = Converter.hex_to_bytes(Address.from_address(self.get_addressFrom()).get_scriptPublicKey())
        tokenFrom = Converter.int_to_bytes(self.get_tokenFrom(), 1)
        amountFrom = Converter.int_to_bytes(self.get_amountFrom(), 8)
        addressTo = Converter.hex_to_bytes(Address.from_address(self.get_addressTo()).get_scriptPublicKey())
        tokenTo = Converter.int_to_bytes(self.get_tokenTo(), 1)

        maxPriceInteger = int(str(self.get_maxPrice())[:-8]) if str(self.get_maxPrice())[:-8] != "" else 0
        maxPriceFraction = int(str(self.get_maxPrice())[-8:])
        maxPriceInteger = Converter.int_to_bytes(maxPriceInteger, 8)
        maxPriceFraction = Converter.int_to_bytes(maxPriceFraction, 8)

        length_addressFrom = Converter.int_to_bytes(len(addressFrom), 1)
        length_addressTo = Converter.int_to_bytes(len(addressTo), 1)

        # Build PoolSwapDefiTx
        result = defiTxType
        result += length_addressFrom
        result += addressFrom
        result += tokenFrom
        result += amountFrom
        result += length_addressTo
        result += addressTo
        result += tokenTo
        result += maxPriceInteger
        result += maxPriceFraction

        return BuildDefiTx.build_defiTx(result)

    def to_json(self) -> {}:
        json = {}
        json.update({"defiTxType": {"typeName": DefiTxType.from_hex(self.get_defiTxType()),
                                    "typeHex": self.get_defiTxType()}})
        json.update({"addressFrom": self.get_addressFrom()})
        json.update({"tokenFrom": self.get_tokenFrom()})
        json.update({"amountFrom": self.get_amountFrom()})
        json.update({"addressTo": self.get_addressTo()})
        json.update({"tokenTo": self.get_tokenTo()})
        json.update({"maxPrice": self.get_maxPrice()})
        return json

    # Get information
    def get_defiTxType(self) -> str:
        return DefiTxType.OP_DEFI_TX_POOL_SWAP

    def get_addressFrom(self) -> str:
        return self._addressFrom

    def get_tokenFrom(self) -> int:
        return self._tokenFrom

    def get_amountFrom(self) -> int:
        return self._amountFrom

    def get_addressTo(self) -> str:
        return self._addressTo

    def get_tokenTo(self) -> int:
        return self._tokenTo

    def get_maxPrice(self) -> int:
        return self._maxPrice

    # Set Information
    def set_addressFrom(self, addressFrom: str) -> None:
        address = Address.from_address(addressFrom)
        self._network = address.get_network()
        self._addressFrom = address.get_address()

    def set_tokenFrom(self, tokenFrom: "int | str") -> None:
        self._tokenFrom = Token.checkAndConvert(self._network, tokenFrom)

    def set_amountFrom(self, amountFrom: int) -> None:
        Verify.is_int(amountFrom)
        self._amountFrom = amountFrom

    def set_addressTo(self, addressTo: str) -> None:
        address = Address.from_address(addressTo)
        if address.get_network() != self._network:
            raise AddressError("The given addresses in the poolswap are not from the same network")
        self._addressTo = address.get_address()

    def set_tokenTo(self, tokenTo: "int | str") -> None:
        self._tokenTo = Token.checkAndConvert(self._network, tokenTo)

    def set_maxPrice(self, maxPrice: int) -> None:
        Verify.is_int(maxPrice)
        self._maxPrice = maxPrice


class CompositeSwap(BaseDefiTx):
    """TODO: MVP"""
    pass


class PoolAddLiquidity(BaseDefiTx):
    """
    TODO: MVP

        Builds the defi transaction for addpoolliquidity

        :param addressAmount: (required) :ref:`Node Address Amount`
        :param shareAddress: (required) the address where the pool shares are placed
        :return: "hex" (string) -- returns the finished defi transaction


        number_of_entries = Converter.int_to_bytes(len(addressAmount), 1)

        result = Converter.hex_to_bytes(DefiTxType.OP_DEFI_TX_POOL_ADD_LIQUIDITY)
        result += number_of_entries

        for address in addressAmount:
            address_script = Converter.hex_to_bytes(Address.from_address(address).get_scriptPublicKey())
            length_of_script = Converter.int_to_bytes(len(address_script), 1)
            result += length_of_script + address_script

            number_of_tokens = Converter.int_to_bytes(len(addressAmount[address]), 1)
            result += number_of_tokens
            for amount in addressAmount[address]:
                split = amount.split('@')
                value = Converter.int_to_bytes(int(split[0]), 8)
                token = Converter.int_to_bytes(int(split[1]), 4)
                result += token + value

        share_address_script = Converter.hex_to_bytes(Address.from_address(shareAddress).get_scriptPublicKey())
        length_of_share_script = Converter.int_to_bytes(len(share_address_script), 1)
        result += length_of_share_script + share_address_script

        return self._defitx.package_defiTx(result)
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "BaseDefiTx":
        pass

    def __init__(self, addressAmount: {}, shareAddress: str):
        self._addressAmount, self._shareAddress = None, None
        self.set_addressAmount(addressAmount)
        self.set_shareAddress(shareAddress)

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(DefiTxType.OP_DEFI_TX_POOL_ADD_LIQUIDITY)
        numberOfEntries = Converter.int_to_bytes(len(self.get_addressAmount()), 1)

        # Build PoolSwapDefiTx
        result = defiTxType

        return BuildDefiTx.build_defiTx(result)

    # Get Information
    def get_defiTxType(self) -> str:
        pass

    def get_addressAmount(self):
        return self._addressAmount

    def get_shareAddress(self):
        return self._shareAddress

    def to_json(self) -> {}:
        pass

    # Set Information
    def set_addressAmount(self, addressAmount: {}):
        self._addressAmount = addressAmount

    def set_shareAddress(self, shareAddress: str):
        self._shareAddress = shareAddress


class PoolRemoveLiquidity(BaseDefiTx):
    """TODO: MVP"""
    pass


class PoolCreatePair(BaseDefiTx):
    pass


class PoolUpdatePair(BaseDefiTx):
    pass
