from defichain.transactions.defitx import Vote
from defichain.transactions.utils import Converter
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Governance:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def vote(self, proposalId: str, masternodeId: str, decision: str, inputs=[]) -> Transaction:
        """
        Vote for proposal

        :param proposalId: (required) The proposal txid
        :type proposalId: str
        :param masternodeId: (required) The masternodeId to vote with
        :type masternodeId: str
        :param decision: (required) The vote decision (yes/no/neutral)
        :type decision: str
        :param inputs: (optional) Inputs
        :type inputs: TxInput
        :return: Transaction
        """

        defiTx = Vote(proposalId, masternodeId, decision)
        return self._builder.build_defiTx(0, defiTx, inputs)
