from defichain.transactions.defitx import Vote
from defichain.transactions.utils import Converter
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Governance:
    """
    **The methods of this module create governance transactions**

    1. **vote**: transaction witch includes your own hexadecimal data
    """

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def vote(self, proposalId: str, masternodeId: str, decision: str, inputs=[]) -> Transaction:
        """
        Creates a transaction that votes for proposal

        >>> builder.governance.vote("1f4039ab714cf73ff1d92b58608ed20a73a799cde88c103b679bdafd83eb472b", "33abc61982725be797f83b47da6f41a344f4d64879d84e31d87a91281070add8", "neutral")  # creates a vote transaction

        :param proposalId: (required) the proposal txid
        :type proposalId: str
        :param masternodeId: (required) the masternodeId to vote with
        :type masternodeId: str
        :param decision: (required) the vote decision (yes / no / neutral)
        :type decision: str
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: :ref:`Transaction Advanced RawTransactions Transaction`
        """

        defiTx = Vote(proposalId, masternodeId, decision)
        return self._builder.build_defiTx(0, defiTx, inputs)
