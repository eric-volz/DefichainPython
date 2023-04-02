from typing import Any

from defichain.exceptions.transactions import AddressError
from defichain.transactions.constants import DefiTxType
from defichain.transactions.address import Address
from defichain.transactions.utils import Converter
from ..builddefitx import BuildDefiTx
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
        pass

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
    """TODO: MVP"""
    pass


class WithdrawFromVault(BaseDefiTx):
    """TODO: MVP"""
    pass


class CloseVault(BaseDefiTx):
    pass


class PlaceAuctionBid(BaseDefiTx):
    pass