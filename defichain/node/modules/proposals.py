from ..util import BuildJson


class Proposals:
    def __init__(self, node):
        self._node = node

    def creategovcfp(self, title: str, context: str, amount: float, payoutAddress: str, contextHash: str = None,
                     cycles: int = None, inputs: [{}] = None) -> str:
        """
        Creates a Community Fund Proposal

        Requires wallet passphrase to be set with walletpassphrase call.

        :param title: (required) The title of community fund request
        :type title: str
        :param context: (required) The context field of community fund request
        :type context: str
        :param amount: (required) Amount in DFI to request
        :type amount: float
        :param payoutAddress: (required) Any valid address for receiving
        :type payoutAddress: str
        :param contextHash: (optional) The hash of the content which context field point to of community fund request
        :type contextHash: str
        :param cycles: (optional) Defaulted to one cycle
        :type cycles: int
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.proposals.creategovcfp("CFP Title", "CFP Context", 1000, "payoutAddress")
        """
        data = BuildJson()
        data.append("title", title)
        data.append("context", context)
        data.append("amount", amount)
        data.append("payoutAddress", payoutAddress)
        data.append("contextHash", contextHash)
        data.append("cycles", cycles)
        return self._node._rpc.call("creategovcfp", data.build(), inputs)

    def creategovvoc(self, title: str, context: str, contextHash: str = None, emergency: bool = False,
                     inputs: [{}] = None) -> str:
        """
        Creates a Vote of Confidence

        Requires wallet passphrase to be set with walletpassphrase call.

        :param title: (required) The title of vote of confidence
        :type title: str
        :param context: (required) The context field for vote of confidence
        :type context: str
        :param contextHash: (optional) The hash of the content which context field point to of vote of confidence request
        :type contextHash: str
        :param emergency: (optional) Is this emergency VOC
        :type emergency: bool
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.proposals.creategovvoc("VOC Title", "VOC Title")
        """
        data = BuildJson()
        data.append("title", title)
        data.append("context", context)
        data.append("contextHash", contextHash)
        data.append("emergency", emergency)
        data.append("inputs", inputs)
        return self._node._rpc.call("creategovvoc", data.build(), inputs)

    def getgovproposal(self, proposalId: str) -> {}:
        """
        Returns real time information about proposal state.

        :param proposalId: (required) The proposal id
        :type proposalId: str
        :return: {id:{...},...} -- (json) Json object with proposal vote information

        :example:

            >>> node.proposals.getgovproposal("txid")
        """
        return self._node._rpc.call("getgovproposal", proposalId)

    def listgovproposals(self, type: str = "all", status: str = "all") -> {}:
        """
        Returns information about proposals.

        :param type: (optional) cfp/voc/all (default = all)
        :type type: str
        :param status: (optional) voting/rejected/completed/all (default = all)
        :type status: str
        :return: {id:{...},...} -- (json) Json object with proposals information

        :example:

            >>> node.proposals.listgovproposals()
        """
        return self._node._rpc.call("listgovproposals", type, status)

    def listgovproposalvotes(self, proposalId: str, masternode: str = "mine", cycle: int = 0) -> {}:
        """
        Returns information about proposal votes.

        :param proposalId: (required) The proposal id
        :type proposalId: str
        :param masternode: (optional) mine/all/id (default = mine)
        :type masternode: str
        :param cycle: (optional) cycle: 0 (show current), cycle: N (show cycle N), cycle: -1 (show all) (default = 0)
        :type cycle: int
        :return: {id:{...},...} -- (json) Json object with proposal vote information

        :example:

            >>> node.proposals.listgovproposalvotes("txid")
        """
        return self._node._rpc.call("listgovproposalvotes", proposalId, masternode, cycle)

    def votegov(self, proposalId: str, masternodeId: str, decision: str, inputs: [{}] = None) -> str:
        """
        Vote for community proposal
        Requires wallet passphrase to be set with walletpassphrase call.

        :param proposalId: (required) The proposal txid
        :type proposalId: str
        :param masternodeId: (required) The masternode id which made the vote
        :type masternodeId: str
        :param decision: (required) The vote decision (yes/no/neutral)
        :type decision: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.proposals.votegov("txid", "masternodeId", "yes")
        """
        return self._node._rpc.call("votegov", proposalId, masternodeId, decision, inputs)
