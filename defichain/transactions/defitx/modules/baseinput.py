from abc import ABC, abstractmethod
from typing import Any

from defichain.exceptions.transactions import AddressError
from defichain.transactions.utils import Token, Verify, BuildAddressAmounts
from defichain.transactions.address import Address
from defichain.transactions.utils import Converter, Calculate
from defichain.transactions.constants import AddressTypes


class BaseInput(ABC):

    @staticmethod
    @abstractmethod
    def deserialize(network: Any, hex: str) -> "BaseInput":
        pass

    @abstractmethod
    def __bytes__(self) -> bytes:
        pass

    def size(self) -> int:
        return int(len(self.serialize()) / 2)

    def bytes_size(self) -> bytes:
        return Converter.int_to_bytes(self.size(), 1)

    def serialize(self) -> str:
        return bytes(self).hex()

    def bytes(self) -> bytes:
        return bytes(self)


class TokenBalanceInt32(BaseInput):

    @staticmethod
    def deserialize(network: Any, hex: str) -> "TokenBalanceInt32":
        tokenId = Converter.hex_to_int(hex[0:8])
        amount = Converter.hex_to_int(hex[8: 24])
        return TokenBalanceInt32(tokenId, amount)

    def __init__(self, tokenId: int, amount: int):
        self._token = tokenId
        self._amount = amount

    def __bytes__(self) -> bytes:
        return self.get_bytes_tokenId() + self.get_bytes_amount()

    @staticmethod
    def estimated_size() -> int:
        return 24

    @staticmethod
    def estimated_bytes_size(self) -> bytes:
        return Converter.int_to_bytes(self.estimated_size(), 1)

    def get_tokenId(self) -> int:
        return self._token

    def get_amount(self) -> int:
        return self._amount

    def get_bytes_tokenId(self) -> bytes:
        return Converter.int_to_bytes(self.get_tokenId(), 4)

    def get_bytes_amount(self) -> bytes:
        return Converter.int_to_bytes(self.get_amount(), 8)


class TokenBalanceVarInt(BaseInput):
    @staticmethod
    def deserialize(network: Any, hex: str) -> "TokenBalanceVarInt":
        tokenId = Calculate.read_varInt(hex[0: Calculate.length_varInt(hex) * 2])
        amount = Converter.hex_to_int(hex[Calculate.length_varInt(hex) * 2: Calculate.length_varInt(hex) * 2 + 16])
        return TokenBalanceVarInt(tokenId, amount)

    def __init__(self, tokenId: int, amount: int):
        self._token = tokenId
        self._amount = amount

    def __bytes__(self) -> bytes:
        return self.get_bytes_tokenId() + self.get_bytes_amount()

    def get_tokenId(self) -> int:
        return self._token

    def get_amount(self) -> int:
        return self._amount

    def get_bytes_tokenId(self) -> bytes:
        return Converter.hex_to_bytes(Calculate.write_varInt(self.get_tokenId()))

    def get_bytes_amount(self) -> bytes:
        return Converter.int_to_bytes(self.get_amount(), 8)


class ScriptBalances(BaseInput):
    @staticmethod
    def from_json(addressAmount: {}) -> ["ScriptBalances"]:
        network = None
        scriptBalances = []

        for address in addressAmount.keys():
            tokenBalanceInt32 = []
            # Check Network
            if not network:
                network = Address.from_address(address).get_network()
            else:
                _network = Address.from_address(address).get_network()
                if network != _network:
                    raise AddressError("The given addresses are not from the same network")

            # Build ScriptBalance
            if isinstance(addressAmount[address], list):
                for tokenBalance in addressAmount[address]:
                    amount, tokenId = tokenBalance.split("@")

                    tokenId = Token.checkAndConvert(network, tokenId)
                    if Verify.is_only_number_str(tokenId):
                        amount = int(amount)
                    Verify.is_int(amount)

                    tokenBalanceInt32.append(TokenBalanceInt32(tokenId, amount))
            else:
                amount, tokenId = addressAmount[address].split("@")

                tokenId = Token.checkAndConvert(network, tokenId)
                if Verify.is_only_number_str(tokenId):
                    amount = int(amount)
                Verify.is_int(amount)

                tokenBalanceInt32.append(TokenBalanceInt32(tokenId, amount))

            scriptBalances.append(ScriptBalances(address, tokenBalanceInt32))
        return scriptBalances

    @staticmethod
    def deserialize(network: Any, hex: str) -> "ScriptBalances":
        position = 0

        scriptSize = Converter.hex_to_int(hex[position: position + 2]) * 2
        position += 2

        address = Address.from_scriptPublicKey(network, hex[position: position + scriptSize])
        position += scriptSize

        numberOfTokenBalanceInt32 = Converter.hex_to_int(hex[position: position + 2])
        position += 2

        tokenBalanceInt32 = []

        for _ in range(numberOfTokenBalanceInt32):
            balance = TokenBalanceInt32.deserialize(network, hex[position: position +
                                                                           TokenBalanceInt32.estimated_size()])
            tokenBalanceInt32.append(balance)
            position += TokenBalanceInt32.estimated_size()

        return ScriptBalances(address.get_address(), tokenBalanceInt32)

    @staticmethod
    def deserialize_array(network: Any, hex: str) -> ["ScriptBalances"]:
        position = 0
        numberOfReceivers = Converter.hex_to_int(hex[position: position + 2])
        position += 2

        scriptBalances = []

        for _ in range(numberOfReceivers):
            length_addressTo = Converter.hex_to_int(hex[position: position + 2]) * 2
            numberOfAmounts = Converter.hex_to_int(
                hex[position + 2 + length_addressTo: position + 2 + length_addressTo + 2])

            scriptBalance = ScriptBalances.deserialize(network, hex[
                                                                position: position + 2 + length_addressTo + 2 + numberOfAmounts * TokenBalanceInt32.estimated_size()])
            scriptBalances.append(scriptBalance)

            position += 2 + length_addressTo + 2 + numberOfAmounts * TokenBalanceInt32.estimated_size()
        return scriptBalances

    @staticmethod
    def to_json(scriptBalances: []) -> {}:
        addressAmount = BuildAddressAmounts()
        for scriptBalance in scriptBalances:
            for tokenAmount in scriptBalance.get_tokenBalanceInt32():
                addressAmount.add(scriptBalance.get_address(), tokenAmount.get_tokenId(), tokenAmount.get_amount())
        return addressAmount.build()

    def __init__(self, address, tokenBalanceInt32: [TokenBalanceInt32]):
        self._address = address
        self._tokenBalanceInt32 = tokenBalanceInt32

    def __bytes__(self) -> bytes:
        result = self.get_bytes_scriptSize()
        result += self.get_bytes_script()
        result += Converter.int_to_bytes(len(self.get_tokenBalanceInt32()), 1)
        for tokenBalanceInt32 in self.get_tokenBalanceInt32():
            result += tokenBalanceInt32.bytes()

        return result

    def get_scriptSize(self) -> str:
        return Converter.int_to_hex(len(self.get_bytes_script()), 1)

    def get_bytes_scriptSize(self) -> bytes:
        return Converter.hex_to_bytes(self.get_scriptSize())

    def get_address(self) -> str:
        return self._address

    def get_tokenBalanceInt32(self) -> [TokenBalanceInt32]:
        return self._tokenBalanceInt32

    def get_script(self) -> str:
        return Address.from_address(self._address).get_scriptPublicKey()

    def get_bytes_script(self) -> bytes:
        return Converter.hex_to_bytes(self.get_script())


class MasternodeUpdates(BaseInput):
    """
    Update Types: 1 byte, 1 = OwnerAddress, 2 = OperatorAddress, 3 = SetRewardAddress, 4 = RemRewardAddress
    Address Types: 1 byte, 1 = p2pkh, 4 = p2wpkh, 0 to remove reward address
    """

    @staticmethod
    def deserialize(network: Any, hex: str):
        pass

    def __init__(self, updateType: int, address: str):
        self._updateType, self._address, self._addressType = None, None, None
        self.set_updateType(updateType)
        self.set_address(address)

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        updateType = Converter.int_to_bytes(self.get_updateType(), 1)
        addressType = Converter.int_to_bytes(self._addressType, 1)
        if self.get_address() == "":
            addressPubKeyHash = Converter.hex_to_bytes("")
        else:
            addressPubKeyHash = Converter.hex_to_bytes(Address.from_address(self.get_address()).get_publicKeyHash())

        sizeAddressPubKeyHash = Converter.int_to_bytes(len(addressPubKeyHash), 1)

        # Build UpdateMasternodeDefiTx
        result = updateType
        result += addressType
        result += sizeAddressPubKeyHash
        result += addressPubKeyHash

        return result

    # Get Information
    def get_updateType(self) -> int:
        return self._updateType

    def get_address(self) -> str:
        return self._address

    def get_addressType(self) -> int:
        return self._addressType

    # Set Information
    def set_updateType(self, updateType: int):
        self._updateType = updateType

    def set_address(self, address: str):
        if address == "":
            self._addressType = 0
            self._address = address
        else:
            addressType = Address.from_address(address).get_addressType()
            if addressType == AddressTypes.P2PKH:
                self._addressType = 1
            elif addressType == AddressTypes.P2WPKH:
                self._addressType = 4
            else:
                raise AddressError("Only P2PKH and P2WPKH can be used to update the masternode")
            self._address = address

