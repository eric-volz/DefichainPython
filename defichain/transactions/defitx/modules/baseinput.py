from abc import ABC, abstractmethod
from defichain.transactions.address import Address
from defichain.transactions.utils import Converter


class BaseInput(ABC):

    @abstractmethod
    def size(self) -> str:
        pass

    @abstractmethod
    def bytes_size(self) -> bytes:
        pass


class TokenBalanceInt32(BaseInput):

    def __init__(self, token: int, amount: int):
        self.token = token
        self.amount = amount

    def size(self) -> str:
        return Converter.int_to_hex(len(self.get_bytes_token() + self.get_bytes_amount()), 1)

    def bytes_size(self) -> bytes:
        return Converter.hex_to_bytes(self.size())

    def get_token(self) -> int:
        return self.token

    def get_amount(self) -> int:
        return self.amount

    def get_bytes_token(self) -> bytes:
        return Converter.int_to_bytes(self.get_token(), 4)

    def get_bytes_amount(self) -> bytes:
        return Converter.int_to_bytes(self.get_amount(), 8)


class TokenBalanceVarInt(BaseInput):
    pass


class ScriptBalances(BaseInput):

    def __init__(self, address, tokenBalanceInt32: [TokenBalanceInt32]):
        self.address = address
        self.tokenBalanceInt32 = tokenBalanceInt32
        self._script = Address.from_address(self.address).get_scriptPublicKey()

    def size(self) -> str:
        size = 0
        for balance in self.get_tokenBalanceInt32():
            size += Converter.hex_to_int(balance.size())
        size += Converter.hex_to_int(self.get_scriptSize())
        return Converter.int_to_hex(size, 1)

    def bytes_size(self) -> bytes:
        return Converter.hex_to_bytes(self.size())

    def get_scriptSize(self) -> str:
        return Converter.int_to_hex(len(self.get_bytes_script()), 1)

    def get_bytes_scriptSize(self) -> bytes:
        return Converter.hex_to_bytes(self.get_scriptSize())

    def get_address(self) -> str:
        return self.address

    def get_tokenBalanceInt32(self) -> [TokenBalanceInt32]:
        return self.tokenBalanceInt32

    def get_script(self) -> str:
        return self._script

    def get_bytes_script(self) -> bytes:
        return Converter.hex_to_bytes(self.get_script())


if __name__ == "__main__":
    pass

