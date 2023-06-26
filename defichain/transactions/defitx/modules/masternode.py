from typing import Any

from defichain.exceptions.transactions import DefiTxError, AddressError
from defichain.transactions.constants import DefiTxType, AddressTypes
from defichain.transactions.address import Address, P2PKH, P2WPKH
from defichain.transactions.utils import Converter
from .baseinput import MasternodeUpdates
from .basedefitx import BaseDefiTx
from ..builddefitx import BuildDefiTx


class CreateMasternode(BaseDefiTx):
    """
    Builds the defi transaction: CreateMasternode

    :param operatorAddress: (required) legacy address of the operator
    :type operatorAddress: str
    :param timeLock: (optional) time period to lock the masternode: 0 (default), 5, 10 years
    :type timeLock: int
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "CreateMasternode":
        operatorType = Converter.hex_to_int(hex[0:2])
        operatorPublicKeyHash = hex[2:42]
        if operatorType == 1:
            operatorAddress = P2PKH.from_publicKeyHash(network, operatorPublicKeyHash)
        else:
            operatorAddress = P2WPKH.from_publicKeyHash(network, operatorPublicKeyHash)

        if hex[42:46] == "0401":  # 5 years timeLock
            timeLock = 5
        elif hex[42:46] == "0802":  # 10 years timeLock
            timeLock = 10
        else:
            timeLock = 0
        return CreateMasternode(operatorAddress.get_address(), timeLock)

    def __init__(self, operatorAddress: str, timeLock: int = 0):
        self._operatorAddress, self._timeLock = None, None
        self.set_operatorAddress(operatorAddress)
        self.set_timeLock(timeLock)

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(self.get_defiTxType())

        if Address.from_address(self.get_operatorAddress()).get_addressType() == AddressTypes.P2PKH:
            operatorType = Converter.int_to_bytes(1, 1)
            operatorPubKeyHash = P2PKH(Address.from_address(self.get_operatorAddress()).get_network(),
                                       self.get_operatorAddress()).get_publicKeyHash()
        else:
            operatorType = Converter.int_to_bytes(4, 1)
            operatorPubKeyHash = P2WPKH(Address.from_address(self.get_operatorAddress()).get_network(),
                                        self.get_operatorAddress()).get_publicKeyHash()
        operatorPubKeyHash = Converter.hex_to_bytes(operatorPubKeyHash)

        if self.get_timeLock() == 5:
            timeLock = Converter.hex_to_bytes("0401")
        elif self.get_timeLock() == 10:
            timeLock = Converter.hex_to_bytes("0802")
        else:
            timeLock = Converter.hex_to_bytes("")

        # Build CreateMasternodeDefiTx
        result = defiTxType
        result += operatorType
        result += operatorPubKeyHash
        result += timeLock

        return BuildDefiTx.build_defiTx(result)

    def to_json(self) -> {}:
        json = {}
        json.update({"defiTxType": {"typeName": DefiTxType.from_hex(self.get_defiTxType()),
                                    "typeHex": self.get_defiTxType()}})
        json.update({"operatorAddress": self.get_operatorAddress()})
        json.update({"timeLock": self.get_timeLock()})
        return json

    # Get Information
    def get_defiTxType(self) -> str:
        return DefiTxType.OP_DEFI_TX_CREATE_MASTER_NODE

    def get_operatorAddress(self) -> str:
        return self._operatorAddress

    def get_timeLock(self) -> int:
        return self._timeLock

    # Set Information
    def set_operatorAddress(self, operatorAddress: str) -> None:
        address = Address.from_address(operatorAddress)
        if not address.get_addressType() in (AddressTypes.P2PKH, AddressTypes.P2WPKH):
            raise DefiTxError("The operator address of the masternode must be a P2PKH or P2WPKH address")
        self._operatorAddress = operatorAddress

    def set_timeLock(self, timeLock: int) -> None:
        if timeLock not in (0, 5, 10):
            raise DefiTxError("The Lock of an masternode can only be 0, 5 or 10 years")
        self._timeLock = timeLock


class ResignMasternode(BaseDefiTx):
    """
    Builds the defi transaction: ResignMasternode

    :param masternodeId: (required) masternodeId: txid of the creation of the masternode
    :type masternodeId: str
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "ResignMasternode":
        masternodeId = bytes(reversed(Converter.hex_to_bytes(hex))).hex()
        return ResignMasternode(masternodeId)

    def __init__(self, masternodeId: str):
        self._masternodeId = None
        self.set_masternodeId(masternodeId)

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(self.get_defiTxType())
        masternodeId = bytes(reversed(Converter.hex_to_bytes(self.get_masternodeId())))

        # Build ResignMasternodeDefiTx
        result = defiTxType
        result += masternodeId

        return BuildDefiTx.build_defiTx(result)

    def to_json(self) -> {}:
        json = {}
        json.update({"defiTxType": {"typeName": DefiTxType.from_hex(self.get_defiTxType()),
                                    "typeHex": self.get_defiTxType()}})
        json.update({"masternodeId": self.get_masternodeId()})
        return json

    # Get Information
    def get_defiTxType(self) -> str:
        return DefiTxType.OP_DEFI_TX_RESIGN_MASTER_NODE

    def get_masternodeId(self) -> str:
        return self._masternodeId

    # Set Information
    def set_masternodeId(self, masternodeId) -> None:
        self._masternodeId = masternodeId


class UpdateMasternode(BaseDefiTx):
    """
    Builds the defi transaction: UpdateMasternode

    :param masternodeId: (required) txid of the creation of the masternode
    :type masternodeId: str
    :param ownerAddress: (required) new owner address
    :type ownerAddress: str
    :param operatorAddress: (optional) new operator address
    :type operatorAddress: str
    :param rewardAddress: (optional) new reward address
    :type rewardAddress: str
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "BaseDefiTx":
        position = 0

        masternodeId = bytes(reversed(Converter.hex_to_bytes(hex[position: position + 64]))).hex()
        position += 64

        numberOfUpdates = Converter.hex_to_int(hex[position: position + 2])
        position += 2

        ownerAddress: str = None
        operatorAddress: str = None
        rewardAddress: str = None

        for _ in range(numberOfUpdates):
            updateType = Converter.hex_to_int(hex[position: position + 2])
            position += 2

            addressType = Converter.hex_to_int(hex[position: position + 2])
            position += 2

            addressSize = Converter.hex_to_int(hex[position: position + 2]) * 2
            position += 2

            publicKeyHash = hex[position: position + addressSize]
            position += addressSize

            address = ""
            if not updateType == 4:
                if addressType == 1:
                    address = P2PKH.from_publicKeyHash(network, publicKeyHash).get_address()
                elif addressType == 4:
                    address = P2WPKH.from_publicKeyHash(network, publicKeyHash).get_address()
                else:
                    raise AddressError("Only P2PKH and P2WPKH can be deserialize")

            if updateType == 1:  # Owner Address
                ownerAddress = address
            elif updateType == 2:  # Operator Address
                operatorAddress = address
            elif updateType == 3:  # Set Reward Address
                rewardAddress = address
            elif updateType == 4:  # Remove Reward Address
                rewardAddress = address

        return UpdateMasternode(masternodeId, ownerAddress, operatorAddress, rewardAddress)

    def __init__(self, masternodeId: str, ownerAddress: str = None, operatorAddress: str = None,
                 rewardAddress: str = None):

        self._masternodeId, self._ownerAddress, self._operatorAddress, self._rewardAddress = None, None, None, None
        self.set_masternodeId(masternodeId)
        self.set_ownerAddress(ownerAddress)
        self.set_operatorAddress(operatorAddress)
        self.set_rewardAddress(rewardAddress)

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(self.get_defiTxType())
        masternodeId = bytes(reversed(Converter.hex_to_bytes(self.get_masternodeId())))
        updates = self.get_updates()
        sizeUpdates = Converter.int_to_bytes(len(updates), 1)

        # Build UpdateMasternodeDefiTx
        result = defiTxType
        result += masternodeId
        result += sizeUpdates
        for update in self.get_updates():
            result += update.bytes()

        return BuildDefiTx.build_defiTx(result)

    def to_json(self) -> {}:
        json = {}
        json.update({"defiTxType": {"typeName": DefiTxType.from_hex(self.get_defiTxType()),
                                    "typeHex": self.get_defiTxType()}})
        json.update({"masternodeId": self.get_masternodeId()})
        updates = []
        for update in self.get_updates():
            updates.append({"updateType": update.get_updateType(), "addressType": update.get_addressType(),
                            "address": update.get_address()})
        json.update({"updates": updates})
        return json

    # Get Information
    def get_defiTxType(self) -> str:
        return DefiTxType.OP_DEFI_TX_UPDATE_MASTER_NODE

    def get_masternodeId(self) -> str:
        return self._masternodeId

    def get_ownerAddress(self) -> str:
        return self._ownerAddress

    def get_operatorAddress(self) -> str:
        return self._operatorAddress

    def get_rewardAddress(self) -> str:
        return self._rewardAddress

    def get_updates(self) -> [MasternodeUpdates]:
        updates = []
        if self.get_ownerAddress():
            updates.append(MasternodeUpdates(1, self.get_ownerAddress()))
        if self.get_operatorAddress():
            updates.append(MasternodeUpdates(2, self.get_operatorAddress()))
        if self.get_rewardAddress():
            if self.get_rewardAddress() == "remove":
                updates.append(MasternodeUpdates(4, ""))
            else:
                updates.append(MasternodeUpdates(3, self.get_rewardAddress()))
        return updates

    # Set Information
    def set_masternodeId(self, masternodeId) -> None:
        self._masternodeId = masternodeId

    def set_ownerAddress(self, ownerAddress) -> None:
        self._ownerAddress = ownerAddress

    def set_operatorAddress(self, operatorAddress) -> None:
        self._operatorAddress = operatorAddress

    def set_rewardAddress(self, rewardAddress) -> None:
        self._rewardAddress = rewardAddress
