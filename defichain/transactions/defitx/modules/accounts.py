from typing import Any

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
    :param tokenId: (optional) the token id or symbol to convert (default = 0 -> DFI)
    :type tokenId: int
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "BaseDefiTx":
        position = 0

        numberOfElements = Converter.hex_to_int(hex[position: position + 2])
        position += 2

        scriptBalances = ScriptBalances.deserialize(network, hex[position:])

        return UtxosToAccount(scriptBalances.get_address(), scriptBalances.get_tokenBalanceInt32()[0].get_amount(),
                              scriptBalances.get_tokenBalanceInt32()[0].get_tokenId())

    def __init__(self, address: str, amount: int, tokenId: "int | str" = 0):
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

        # Build UtxoToAccountDefiTx
        result = defiTxType
        result += numberOfElements
        result += self._scriptBalances.bytes()

        return BuildDefiTx.build_defiTx(result)

    def to_json(self) -> {}:

        json = {}
        json.update({"defiTxType": {"typeName": DefiTxType.from_hex(self.get_defiTxType()),
                                    "typeHex": self.get_defiTxType()}})
        json.update({"address": self.get_address()})
        json.update({"amount": self.get_amount()})
        json.update({"tokenId": self.get_tokenId()})
        return json

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
        address = Address.from_address(address)
        self._network = address.get_network()
        self._address = address.get_address()

    def set_tokenId(self, tokenId: "int | str") -> None:
        if isinstance(tokenId, str) and not Verify.is_only_number_str(tokenId):
            self._tokenId = Token.get_id_from_symbol(self._network, tokenId)
        else:
            Token.verify_tokenId(self._network, tokenId)
            self._tokenId = tokenId

    def set_amount(self, amount: int) -> None:
        Verify.is_int(amount)
        self._amount = amount


class AccountToUtxos(BaseDefiTx):
    """TODO: MVP"""
    pass


class AccountToAccount(BaseDefiTx):
    """
    Transfers token (DFI, BTC, ETH, ...) from one address to another

    :param addressFrom: the defi address of the sender
    :type addressFrom: str
    :param addressAmountTo: An json object where the address is the key and the value is the amount (amount@token)
    :type addressAmountTo: AddressAmounts
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "AccountToAccount":
        position = 0

        length_addressFrom = Converter.hex_to_int(hex[position: position + 2]) * 2
        position += 2

        addressFrom = Address.from_scriptPublicKey(network, hex[position: position + length_addressFrom])
        position += length_addressFrom

        scriptBalances = ScriptBalances.deserialize_array(network, hex[position:])

        return AccountToAccount(addressFrom.get_address(), ScriptBalances.to_json(scriptBalances))

    def __init__(self, addressFrom: str, addressAmountTo: {}):
        self._addressFrom, self._addressAmountTo = None, None
        self._network = None
        self._scriptBalances = None
        self.set_addressFrom(addressFrom)
        self.set_addressAmountTo(addressAmountTo)

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(DefiTxType.OP_DEFI_TX_ACCOUNT_TO_ACCOUNT)
        addressFrom = Converter.hex_to_bytes(Address.from_address(self.get_addressFrom()).get_scriptPublicKey())
        scriptBalances = ScriptBalances.from_json(self.get_addressAmountTo())

        length_addressFrom = Converter.int_to_bytes(len(addressFrom), 1)
        numberOfReceivers = Converter.int_to_bytes(len(scriptBalances), 1)

        # Build AccountToAccountDefiTx
        result = defiTxType
        result += length_addressFrom
        result += addressFrom
        result += numberOfReceivers
        for balances in scriptBalances:
            result += balances.bytes()

        return BuildDefiTx.build_defiTx(result)

    def to_json(self) -> {}:
        json = {}
        json.update({"defiTxType": {"typeName": DefiTxType.from_hex(self.get_defiTxType()),
                                    "typeHex": self.get_defiTxType()}})
        json.update({"addressFrom": self.get_addressFrom()})
        json.update({"addressAmountTo": self.get_addressAmountTo()})
        return json

    # Get Information
    def get_defiTxType(self) -> str:
        return DefiTxType.OP_DEFI_TX_ACCOUNT_TO_ACCOUNT

    def get_addressFrom(self) -> str:
        return self._addressFrom

    def get_addressAmountTo(self) -> {}:
        return self._addressAmountTo

    # Set Information
    def set_addressFrom(self, addressFrom: str) -> None:
        address = Address.from_address(addressFrom)
        self._network = address.get_network()
        self._addressFrom = address.get_address()

    def set_addressAmountTo(self, addressAmountTo: {}) -> None:
        self._scriptBalances = ScriptBalances.from_json(addressAmountTo)
        self._addressAmountTo = addressAmountTo


class AnyAccountToAccount(BaseDefiTx):
    """TODO: MVP"""
    pass


class SetFutureSwap(BaseDefiTx):
    """TODO: MVP"""
    pass
