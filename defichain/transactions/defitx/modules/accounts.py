from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from defichain.transactions.constants import DefiTxType
from defichain.transactions.address import Address
from defichain.transactions.utils import Converter, Token, Verify
from .basedefitx import BaseDefiTx
from .baseinput import ScriptBalances, TokenBalanceInt32
from ..builddefitx import BuildDefiTx


class UtxosToAccount(BaseDefiTx):
    """
    Convert DFI UTXO to DFI Token

    :param address: (required) the address with the utxo
    :type address: str
    :param amount: (required) the amount to convert
    :type amount: int
    :param tokenId: (optional) the token id to convert (default = 0 -> DFI)
    :type tokenId: int
    :return: "hex" (string) -- returns the finished defi transaction
    """

    @staticmethod
    def deserialize(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, hex: str) -> "BaseDefiTx":
        position = 0

        numberOfElements1 = Converter.hex_to_int(hex[position: position + 2])
        position += 2

        lengthScriptPublicKey = Converter.hex_to_int(hex[position: position + 2]) * 2
        position += 2

        address = Address.from_scriptPublicKey(network, hex[position: position + lengthScriptPublicKey])
        position += lengthScriptPublicKey

        numberOfElements2 = Converter.hex_to_int(hex[position: position + 2])
        position += 2

        tokenId = Converter.hex_to_int(hex[position: position + 8])
        position += 8

        amount = Converter.hex_to_int(hex[position: position + 16])
        position += 16

        return UtxosToAccount(address.get_address(), amount, tokenId)

    def __init__(self, address: str, amount: int, tokenId: int = 0):

        self._address, self._tokenId, self._amount = None, None, None
        self._network = None
        self.set_address(address)
        self.set_tokenId(tokenId)
        self.set_amount(amount)

        self._scriptBalances = ScriptBalances(self.get_address(), [TokenBalanceInt32(self.get_tokenId(), self.get_amount())])

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(DefiTxType.OP_DEFI_TX_UTXOS_TO_ACCOUNT)
        numberOfElements = Converter.int_to_bytes(1, 1)

        # Build PoolSwapDefiTx
        result = defiTxType
        result += numberOfElements
        result += self._scriptBalances.bytes()

        return BuildDefiTx.build_defiTx(result)

    def __str__(self) -> str:
        result = f"""
                UtxosToAccount
                --------------
                Address: {self.get_address()}
                Amount: {self.get_amount()}
                Token ID: {self.get_tokenId()}
    
                """
        return result

    def to_json(self) -> {}:
        result = {
            "defiTxType": self.get_defiTxType(),
            "address": self.get_address(),
            "amount": self.get_amount(),
            "tokenId": self.get_tokenId()
        }
        return result

    def verify(self) -> bool:
        address = Address.from_address(self.get_address())
        self._network = address.get_network()
        Verify.is_int(self.get_amount())
        Token.verify_tokenId(self._network, self.get_tokenId())
        return True

    # Get Information
    def get_defiTxType(self) -> str:
        return DefiTxType.OP_DEFI_TX_UTXOS_TO_ACCOUNT

    def get_address(self) -> str:
        return self._address

    def get_tokenId(self) -> int:
        return self._tokenId

    def get_amount(self) -> int:
        return self._amount

    # Set Information
    def set_address(self, address: str) -> None:
        self._address = address

    def set_tokenId(self, tokenId: int) -> None:
        self._tokenId = tokenId

    def set_amount(self, amount: int) -> None:
        self._amount = amount


class AccountToUtxos(BaseDefiTx):
    """TODO: MVP"""
    pass


class AccountToAccount(BaseDefiTx):
    """TODO: MVP"""
    pass


class AnyAccountToAccount(BaseDefiTx):
    """TODO: MVP"""
    pass


class SetFutureSwap(BaseDefiTx):
    """TODO: MVP"""
    pass
