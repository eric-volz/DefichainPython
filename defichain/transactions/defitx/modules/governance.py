from typing import Any

from defichain.exceptions.transactions import DefiTxError
from defichain.transactions.constants import DefiTxType
from defichain.transactions.utils import Converter
from .basedefitx import BaseDefiTx
from ..builddefitx import BuildDefiTx


class CreateCfp(BaseDefiTx):
    pass


class CreateVoc(BaseDefiTx):
    pass


class Vote(BaseDefiTx):
    """
    Builds the defi transaction: Vote

    :param proposalId: (required) The proposal txid
    :type proposalId: str
    :param masternodeId: (required) The masternodeId to vote with
    :type masternodeId: str
    :param decision: (required) The vote decision (yes/no/neutral)
    :type decision: str
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "Vote":
        proposalId = bytes(reversed(Converter.hex_to_bytes(hex[0:64]))).hex()
        masternodeId = bytes(reversed(Converter.hex_to_bytes(hex[64:128]))).hex()
        decision = Converter.hex_to_int(hex[128:130])
        if decision == 1:
            decision = "Yes"
        elif decision == 2:
            decision = "No"
        elif decision == 3:
            decision = "Neutral"
        else:
            raise DefiTxError("The voting byte is not correct. Only 01, 02 and 03 is allowed.")

        return Vote(proposalId, masternodeId, decision)

    def __init__(self, proposalId: str, masternodeId: str, decision: str):
        self._proposalId, self._masternodeId, self._decision = None, None, None
        self.set_proposalId(proposalId)
        self.set_masternodeId(masternodeId)
        self.set_decision(decision)

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(self.get_defiTxType())
        proposalId = bytes(reversed(Converter.hex_to_bytes(self.get_proposalId())))
        masternodeId = bytes(reversed(Converter.hex_to_bytes(self.get_masternodeId())))
        if self.get_decision() in ("yes", "Yes"):
            decision = Converter.int_to_bytes(1, 1)
        elif self.get_decision() in ("no", "No"):
            decision = Converter.int_to_bytes(2, 1)
        elif self.get_decision() in ("neutral", "Neutral"):
            decision = Converter.int_to_bytes(3, 1)
        else:
            raise DefiTxError("Only Yes, No and Neutral can be selected for voting.")

        # Build VoteDefiTx
        result = defiTxType
        result += proposalId
        result += masternodeId
        result += decision

        return BuildDefiTx.build_defiTx(result)

    def to_json(self) -> {}:
        json = {}
        json.update({"defiTxType": {"typeName": DefiTxType.from_hex(self.get_defiTxType()),
                                    "typeHex": self.get_defiTxType()}})
        json.update({"proposalId": self.get_proposalId()})
        json.update({"masternodeId": self.get_masternodeId()})
        json.update({"decision": self.get_decision()})
        return json

    # Get Information
    def get_defiTxType(self) -> str:
        return DefiTxType.OP_DEFI_TX_VOTE

    def get_proposalId(self) -> str:
        return self._proposalId

    def get_masternodeId(self) -> str:
        return self._masternodeId

    def get_decision(self) -> str:
        return self._decision

    # Set Information
    def set_proposalId(self, proposalId: str) -> None:
        self._proposalId = proposalId

    def set_masternodeId(self, masternodeId: str) -> None:
        self._masternodeId = masternodeId

    def set_decision(self, decision: str) -> None:
        if decision not in ("Yes", "yes", "No", "no", "neutral", "Neutral"):
            raise DefiTxError("Only Yes, No and Neutral can be selected for voting")
        self._decision = decision
