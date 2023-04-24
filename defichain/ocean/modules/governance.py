# https://github.com/JellyfishSDK/jellyfish/blob/main/packages/whale-api-client/src/api/governance.ts


class Governance:
    def __init__(self, ocean):
        self._ocean = ocean

    def listGovProposals(self, status: str = "all", type: str = "all", cycle: int = 0, all: bool = False,
                         size: int = 30, next: str = None) -> {}:  # 01
        """
        Paginate query on-chain governance proposals

        :param status: (required) proposal status: all, voting, rejected, completed
        :type status: str
        :param type: (required) proposal type: all, cfp, voc
        :type type: str
        :param cycle: (required) proposal cycle: 0 (show all), cycle: N (show cycle N), cycle: -1 (show previous cycle)
        :type cycle: int
        :param all: (optional) all True to return all records, otherwise it will return based on size param
        :type all: bool
        :param size: (optional) number of returned proposals
        :type size: int
        :param next: (optional) next set of proposals
        :type next: str
        :return: Json String

            .. code-block::

                [
                    {
                        proposalId: string
                        title: string
                        context: string
                        contextHash: string
                        type: GovernanceProposalType
                        status: GovernanceProposalStatus
                        amount?: string
                        currentCycle: number
                        totalCycles: number
                        creationHeight: number
                        cycleEndHeight: number
                        proposalEndHeight: number
                        payoutAddress?: string
                        votingPeriod: number
                        approvalThreshold: string
                        quorum: string
                        votesPossible?: number
                        votesPresent?: number
                        votesPresentPct?: string
                        votesYes?: number
                        votesYesPct?: string
                        fee: number
                        options?: string[]
                    }
                ]

        :example:

        >>> ocean.governance.listGovProposals("all", "all")
        """
        url = f"governance/proposals?status={status}&type={type}&cycle={cycle}"
        if all is not None:
            url += f"&all={all}"

        return self._ocean._conn.get(url, size=size, next=next)

    def getGovProposal(self, id: str) -> {}:  # 02
        """
        Get information about a proposal with given proposal id.

        :param id: (required) txid of proposal
        :type id: str
        :return: Json String

            .. code-block::

                {
                    proposalId: string
                    title: string
                    context: string
                    contextHash: string
                    type: GovernanceProposalType
                    status: GovernanceProposalStatus
                    amount?: string
                    currentCycle: number
                    totalCycles: number
                    creationHeight: number
                    cycleEndHeight: number
                    proposalEndHeight: number
                    payoutAddress?: string
                    votingPeriod: number
                    approvalThreshold: string
                    quorum: string
                    votesPossible?: number
                    votesPresent?: number
                    votesPresentPct?: string
                    votesYes?: number
                    votesYesPct?: string
                    fee: number
                    options?: string[]
                }

        :example:

        >>> ocean.governance.getGovProposal("a252bea49341adb75842dd30442e5836f9e204e7fa96a1585983eca3b3b5407c")
        """

        return self._ocean._conn.get(f"governance/proposals/{id}")

    def listGovProposalVotes(self, id: str, masternodeId: str = "all", cycle: int = 0, all: bool = False,
                             size: int = 30, next: str = None) -> {}:  # 03
        """
        Returns votes for a proposal

        :param id: (required) txid of proposal
        :type id: str
        :param masternodeId: (required) masternodeId, mine, all
        :type masternodeId: str
        :param cycle: (required) proposal cycle: 0 (show all), cycle: N (show cycle N), cycle: -1 (show previous cycle)
        :type cycle: int
        :param all: (optional) all True to return all records, otherwise it will return based on size param
        :type all: bool
        :param size: (optional) number of returned proposals votes
        :type size: int
        :param next: (optional) next set of proposals votes
        :type next: str
        :return: Json String

            .. code-block::

                {
                    proposalId: string
                    masternodeId: string
                    cycle: number
                    vote: YES, NO, NEUTRAL, UNKNOWN
                    valid: boolean
                }

        :example:

        >>> ocean.governance.listGovProposalVotes("a252bea49341adb75842dd30442e5836f9e204e7fa96a1585983eca3b3b5407c")
        """

        url = f"governance/proposals/{id}/votes?masternode={masternodeId}&cycle={cycle}"

        if all is not None:
            url += f"&all={all}"

        return self._ocean._conn.get(url, size=size, next=next)
