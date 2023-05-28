from typing import Any

from defichain.exceptions.transactions import DefiTxError
from defichain.transactions.constants import DefiTxType, AddressTypes
from defichain.transactions.address import Address, P2PKH, P2WPKH
from defichain.transactions.utils import Converter
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
    66ba4219032a90ca6a66370c553d27e1e7d5b17163a1d155464a82c3581b9f70

    6a
    4c54
    44665478
    6d  #defi opcode
    8e63dfce62b3695a68ccf9842c9416c9dcbaf5d4896b25cbf071b2bd994e0518 # masternodeId
    02 # number of updates
    02 # update type
    01 # address type
    14 # lenght of address
    8e6137ff96462c8f4c3eeb664c098790b3d044df
    03 # update type
    04 # address type
    14 # length of address
    6bfc452b4cba7fcdf5fd311523a6706610e385e1
    """
    pass
