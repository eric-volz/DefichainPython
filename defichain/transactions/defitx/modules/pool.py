from typing import Any

from defichain.exceptions.transactions import AddressError
from defichain.transactions.constants import DefiTxType
from defichain.transactions.address import Address
from defichain.transactions.utils import Converter, Token, Verify, Calculate
from .basedefitx import BaseDefiTx
from .baseinput import ScriptBalances
from ..builddefitx import BuildDefiTx


class PoolSwap(BaseDefiTx):
    """
    Builds the defi transaction: PoolSwap

    :param addressFrom: (required) the address where the tokens are located
    :param tokenFrom: (required) the token that should be exchanged
    :param amountFrom: (required) the amount that should be exchanged
    :param addressTo: (required) the address where the exchanged tokens are sent to
    :param tokenTo: (required) the token to change into
    :param maxPrice: (required) maximum acceptable price
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "PoolSwap":
        position = 0

        lengthAddressFrom = Converter.hex_to_int(hex[position: position + 2]) * 2
        position += 2

        addressFrom = Address.from_scriptPublicKey(network, hex[position: position + lengthAddressFrom])
        position += lengthAddressFrom

        sizeVarIntTokenFrom = Calculate.length_varInt(hex[position:]) * 2
        tokenFrom = Calculate.read_varInt(hex[position: position + sizeVarIntTokenFrom])
        position += sizeVarIntTokenFrom

        amountFrom = Converter.hex_to_int(hex[position: position + 16])
        position += 16

        lengthAddressTo = Converter.hex_to_int(hex[position: position + 2]) * 2
        position += 2

        addressTo = Address.from_scriptPublicKey(network, hex[position: position + lengthAddressTo])
        position += lengthAddressTo

        sizeVarIntTokenTo = Calculate.length_varInt(hex[position:]) * 2
        tokenTo = Calculate.read_varInt(hex[position: position + sizeVarIntTokenTo])
        position += sizeVarIntTokenTo

        maxPriceInteger = Converter.hex_to_int(hex[position: position + 16])
        position += 16

        maxPriceFraction = str(Converter.hex_to_int(hex[position: position + 16]))
        position += 16

        while len(maxPriceFraction) < 8:
            maxPriceFraction += "0"

        maxPrice = int(str(maxPriceInteger) + maxPriceFraction)

        return PoolSwap(addressFrom.get_address(), tokenFrom, amountFrom, addressTo.get_address(), tokenTo, maxPrice)

    def __init__(self, addressFrom: str, tokenFrom: "int | str", amountFrom: int, addressTo: str, tokenTo: "int | str",
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
        tokenFrom = Converter.hex_to_bytes(Calculate.write_varInt(self.get_tokenFrom()))
        amountFrom = Converter.int_to_bytes(self.get_amountFrom(), 8)
        addressTo = Converter.hex_to_bytes(Address.from_address(self.get_addressTo()).get_scriptPublicKey())
        tokenTo = Converter.hex_to_bytes(Calculate.write_varInt(self.get_tokenTo()))

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


class CompositeSwap(PoolSwap):
    """
    Builds the defi transaction: CompositeSwap

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
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "CompositeSwap":

        poolSwap = PoolSwap.deserialize(network, hex)
        lengthPoolSwap = len(poolSwap.serialize()[16:])

        position = lengthPoolSwap
        numberOfPools = Converter.hex_to_int(hex[position: position + 2])
        position += 2

        pools = []
        for _ in range(numberOfPools):
            lengthVarInt = Calculate.length_varInt(hex[position:]) * 2
            tokenId = Calculate.read_varInt(hex[position: position + lengthVarInt])
            position += lengthVarInt
            pools.append(tokenId)

        return CompositeSwap(poolSwap.get_addressFrom(), poolSwap.get_tokenFrom(), poolSwap.get_amountFrom(),
                             poolSwap.get_addressTo(), poolSwap.get_tokenTo(), poolSwap.get_maxPrice(), pools)

    def __init__(self, addressFrom: str, tokenFrom: "int | str", amountFrom: int, addressTo: str,
                 tokenTo: "int | str", maxPrice: int, pools: [str]):
        super().__init__(addressFrom, tokenFrom, amountFrom, addressTo, tokenTo, maxPrice)
        self._pools = None
        self.set_pools(pools)

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(self.get_defiTxType())
        addressFrom = Converter.hex_to_bytes(Address.from_address(self.get_addressFrom()).get_scriptPublicKey())
        tokenFrom = Converter.hex_to_bytes(Calculate.write_varInt(self.get_tokenFrom()))
        amountFrom = Converter.int_to_bytes(self.get_amountFrom(), 8)
        addressTo = Converter.hex_to_bytes(Address.from_address(self.get_addressTo()).get_scriptPublicKey())
        tokenTo = Converter.hex_to_bytes(Calculate.write_varInt(self.get_tokenTo()))

        maxPriceInteger = int(str(self.get_maxPrice())[:-8]) if str(self.get_maxPrice())[:-8] != "" else 0
        maxPriceFraction = int(str(self.get_maxPrice())[-8:])
        maxPriceInteger = Converter.int_to_bytes(maxPriceInteger, 8)
        maxPriceFraction = Converter.int_to_bytes(maxPriceFraction, 8)

        length_addressFrom = Converter.int_to_bytes(len(addressFrom), 1)
        length_addressTo = Converter.int_to_bytes(len(addressTo), 1)

        network = Address.from_address(self.get_addressFrom()).get_network()
        numberOfPools = Converter.int_to_bytes(len(self.get_pools()), 1)

        pools = b''
        for pool in self.get_pools():
            pools += Converter.hex_to_bytes(Calculate.write_varInt(Token.checkAndConvert(network, pool)))

        # Build CompositeSwapDefiTx
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
        result += numberOfPools
        result += pools

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
        json.update({"pools": self.get_pools()})
        return json

    # Get information
    def get_defiTxType(self) -> str:
        return DefiTxType.OP_DEFI_TX_COMPOSITE_SWAP

    def get_pools(self):
        return self._pools

    # Set Information
    def set_pools(self, pools: [str]):
        self._pools = pools


class AddPoolLiquidity(BaseDefiTx):
    """
    Builds the defi transaction: AssPoolLiquidity

    :param addressAmount: (required) address as key, quantity and token as value: AddressAmount
    :type addressAmount: AddressAmount
    :param shareAddress: (required) address on which the pool token should be stored
    :type shareAddress: str
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "AddPoolLiquidity":
        position = 0

        scriptBalances = ScriptBalances.deserialize_array(network, hex[position:])

        sizeScriptBalances = 2
        for scriptBalance in scriptBalances:
            sizeScriptBalances += scriptBalance.size() * 2

        position += sizeScriptBalances

        lengthShareAddress = Converter.hex_to_int(hex[position: position + 2]) * 2
        position += 2

        shareAddress = Address.from_scriptPublicKey(network, hex[position: position + lengthShareAddress])
        position += lengthShareAddress

        return AddPoolLiquidity(ScriptBalances.to_json(scriptBalances), shareAddress.get_address())

    def __init__(self, addressAmount: {}, shareAddress: str):

        self._addressAmount, self._shareAddress = None, None
        self.set_addressAmount(addressAmount)
        self.set_shareAddress(shareAddress)

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(DefiTxType.OP_DEFI_TX_POOL_ADD_LIQUIDITY)
        scriptBalances = ScriptBalances.from_json(self.get_addressAmount())
        shareAddress = Converter.hex_to_bytes(Address.from_address(self.get_shareAddress()).get_scriptPublicKey())

        numberOfElements = Converter.int_to_bytes(len(scriptBalances), 1)
        lengthShareAddress = Converter.int_to_bytes(len(shareAddress), 1)

        # Build PoolAddLiquidityDefiTx
        result = defiTxType
        result += numberOfElements
        for balances in scriptBalances:
            result += balances.bytes()
        result += lengthShareAddress
        result += shareAddress

        return BuildDefiTx.build_defiTx(result)

    # Get Information
    def get_defiTxType(self) -> str:
        return DefiTxType.OP_DEFI_TX_POOL_ADD_LIQUIDITY

    def get_addressAmount(self):
        return self._addressAmount

    def get_shareAddress(self):
        return self._shareAddress

    def to_json(self) -> {}:
        json = {}
        json.update({"defiTxType": {"typeName": DefiTxType.from_hex(self.get_defiTxType()),
                                    "typeHex": self.get_defiTxType()}})
        json.update({"addressAmount": self.get_addressAmount()})
        json.update({"shareAddress": self.get_shareAddress()})
        return json

    # Set Information
    def set_addressAmount(self, addressAmount: {}):
        self._addressAmount = addressAmount

    def set_shareAddress(self, shareAddress: str):
        self._shareAddress = shareAddress


class RemovePoolLiquidity(BaseDefiTx):
    """
    Builds the defi transaction: RemovePoolLiquidity

    :param addressFrom: (required) the address to remove the pool tokens from
    :type addressFrom: str
    :param amount: (required) value and liquidity tokens which should be removed: Amount
    :type amount: str
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "RemovePoolLiquidity":
        position = 0

        lengthAddressFrom = Converter.hex_to_int(hex[position: position + 2]) * 2
        position += 2

        addressFrom = Address.from_scriptPublicKey(network, hex[position: position + lengthAddressFrom])
        position += lengthAddressFrom

        lengthTokenId = len(hex[position:]) - 16
        tokenId = Converter.hex_to_int(hex[position: position + 2])
        position += lengthTokenId

        value = Converter.hex_to_int(hex[position: position + 16])
        position += 16

        return RemovePoolLiquidity(addressFrom.get_address(), f"{value}@{tokenId}")

    def __init__(self, addressFrom: str, amount: str):
        self._addressFrom, self._amount = None, None
        self.set_addressFrom(addressFrom)
        self.set_amount(amount)

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(self.get_defiTxType())
        address = Address.from_address(self.get_addressFrom())
        addressFrom = Converter.hex_to_bytes(address.get_scriptPublicKey())
        tokenId = Converter.hex_to_bytes(
            Calculate.write_varInt(Token.checkAndConvert(address.get_network(), self.get_amount().split("@")[1])))
        value = Converter.int_to_bytes(int(self.get_amount().split("@")[0]), 8)

        lengthAddressFrom = Converter.int_to_bytes(len(addressFrom), 1)

        # Build RemovePoolLiquidity
        result = defiTxType
        result += lengthAddressFrom
        result += addressFrom
        result += tokenId
        result += value

        return BuildDefiTx.build_defiTx(result)

    # Get Information
    def get_defiTxType(self) -> str:
        return DefiTxType.OP_DEFI_TX_POOL_REMOVE_LIQUIDITY

    def get_addressFrom(self) -> str:
        return self._addressFrom

    def get_amount(self) -> str:
        return self._amount

    def to_json(self) -> {}:
        json = {}
        json.update({"defiTxType": {"typeName": DefiTxType.from_hex(self.get_defiTxType()),
                                    "typeHex": self.get_defiTxType()}})
        json.update({"addressFrom": self.get_addressFrom()})
        json.update({"amount": self.get_amount()})
        return json

    # Set Information
    def set_addressFrom(self, addressFrom: str):
        self._addressFrom = addressFrom

    def set_amount(self, amount: str):
        self._amount = amount
