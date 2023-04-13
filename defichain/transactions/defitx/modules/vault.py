from typing import Any

from defichain.exceptions.transactions import AddressError
from defichain.transactions.constants import DefiTxType
from defichain.transactions.address import Address
from defichain.transactions.utils import Converter, Token, Calculate
from ..builddefitx import BuildDefiTx
from .baseinput import TokenBalanceVarInt
from .basedefitx import BaseDefiTx


class CreateVault(BaseDefiTx):
    """
    Builds the defi transaction: Create Vault

    :param ownerAddress: (required) the address where vault will be created
    :type ownerAddress: str
    :param schemeId: (required) the scheme id for the vault
    :type schemeId: str
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "BaseDefiTx":
        position = 0

        lengthOwnerAddress = Converter.hex_to_int(hex[position: position + 2]) * 2
        position += 2

        ownerAddress = Address.from_scriptPublicKey(network, hex[position: position + lengthOwnerAddress])
        position += lengthOwnerAddress

        lengthSchemeId = Converter.hex_to_int(hex[position: position + 2]) * 2
        position += 2

        schemeId = Converter.hex_to_str(hex[position: position + lengthSchemeId])
        position += lengthSchemeId

        return CreateVault(ownerAddress.get_address(), schemeId)

    def __init__(self, ownerAddress: str, schemeId: str):
        self._ownerAddress, self._schemeId = None, None
        self.set_ownerAddress(ownerAddress)
        self.set_schemeId(schemeId)

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(self.get_defiTxType())
        ownerAddress = Converter.hex_to_bytes(Address.from_address(self.get_ownerAddress()).get_scriptPublicKey())
        schemeId = Converter.hex_to_bytes(Converter.str_to_hex(self.get_schemeId()))

        lengthOwnerAddress = Converter.int_to_bytes(len(ownerAddress), 1)
        lengthSchemeId = Converter.int_to_bytes(len(schemeId), 1)

        # Build PoolSwapDefiTx
        result = defiTxType
        result += lengthOwnerAddress
        result += ownerAddress
        result += lengthSchemeId
        result += schemeId

        return BuildDefiTx.build_defiTx(result)

    def to_json(self) -> {}:
        json = {}
        json.update({"defiTxType": {"typeName": DefiTxType.from_hex(self.get_defiTxType()),
                                    "typeHex": self.get_defiTxType()}})
        json.update({"ownerAddress": self.get_ownerAddress()})
        json.update({"schemeId": self.get_schemeId()})
        return json

    # Get Information
    def get_defiTxType(self) -> str:
        return DefiTxType.OP_DEFI_TX_CREATE_VAULT

    def get_ownerAddress(self):
        return self._ownerAddress

    def get_schemeId(self):
        return self._schemeId

    # Set Information
    def set_ownerAddress(self, ownerAddress: str):
        self._ownerAddress = ownerAddress

    def set_schemeId(self, schemeId: str):
        self._schemeId = schemeId


class UpdateVault(BaseDefiTx):
    pass


class DepositToVault(BaseDefiTx):
    """
    Builds the defi transaction: Deposit To Vault

    :param vaultId: (required) vault id
    :type vaultId: str
    :param addressFrom: (required) address containing collateral
    :type addressFrom: str
    :param amount: (required) Amount of collateral in amount@symbol format
    :type amount: str
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "DepositToVault":
        position = 0

        vaultId = Converter.bytes_to_hex(bytes(reversed(Converter.hex_to_bytes(hex[position: position + 64]))))
        position += 64

        lenghtAddressFrom = Converter.hex_to_int(hex[position: position + 2]) * 2
        position += 2

        addressFrom = Address.from_scriptPublicKey(network, hex[position: position + lenghtAddressFrom])
        position += lenghtAddressFrom

        lengthTokenId = Calculate.length_varInt(hex[position:]) * 2
        tokenId = Calculate.read_varInt(hex[position: position + lengthTokenId])
        position += lengthTokenId
        amount = Converter.hex_to_int(hex[position: position + 16])

        return DepositToVault(vaultId, addressFrom.get_address(), f"{amount}@{tokenId}")

    def __init__(self, vaultId: str, addressFrom: str, amount: str):
        """

        :param vaultId:
        :type vaultId:
        :param addressFrom:
        :type addressFrom:
        :param amount:
        :type amount:
        """
        self._vaultId, self._addressFrom, self._amount = None, None, None
        self._network = None
        self.set_vaultId(vaultId)
        self.set_addressFrom(addressFrom)
        self.set_amount(amount)

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(self.get_defiTxType())
        vaultId = bytes(reversed(Converter.hex_to_bytes(self.get_vaultId())))
        addressFrom = Converter.hex_to_bytes(Address.from_address(self.get_addressFrom()).get_scriptPublicKey())
        amountSplit = self.get_amount().split("@")
        tokenAmount = TokenBalanceVarInt(int(amountSplit[1]), int(amountSplit[0])).bytes()

        length_addressFrom = Converter.int_to_bytes(len(addressFrom), 1)

        # Build DepositToVaultDefiTx
        result = defiTxType
        result += vaultId
        result += length_addressFrom
        result += addressFrom
        result += tokenAmount

        return BuildDefiTx.build_defiTx(result)

    def to_json(self) -> {}:
        json = {}
        json.update({"defiTxType": {"typeName": DefiTxType.from_hex(self.get_defiTxType()),
                                    "typeHex": self.get_defiTxType()}})
        json.update({"vaultId": self.get_vaultId()})
        json.update({"addressFrom": self.get_addressFrom()})
        json.update({"amount": self.get_amount()})
        return json

    # Get Information
    def get_defiTxType(self) -> str:
        return DefiTxType.OP_DEFI_TX_DEPOSIT_TO_VAULT

    def get_vaultId(self) -> str:
        return self._vaultId

    def get_addressFrom(self) -> str:
        return self._addressFrom

    def get_amount(self) -> str:
        return self._amount

    # Set Information
    def set_vaultId(self, vaultId: str) -> None:
        self._vaultId = vaultId

    def set_addressFrom(self, addressFrom: str) -> None:
        address = Address.from_address(addressFrom)
        self._network = address.get_network()
        self._addressFrom = addressFrom

    def set_amount(self, amount: str) -> None:
        self._amount = f'{amount.split("@")[0]}@{Token.checkAndConvert(self._network, amount.split("@")[1])}'


class WithdrawFromVault(BaseDefiTx):
    """TODO: MVP"""
    pass


class CloseVault(BaseDefiTx):
    pass


class PlaceAuctionBid(BaseDefiTx):
    pass