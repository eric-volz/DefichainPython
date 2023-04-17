# https://github.com/JellyfishSDK/jellyfish/blob/main/packages/whale-api-client/src/api/governance.ts


class Governance:
    def __init__(self, ocean):
        self._ocean = ocean

    def listGovProposals(self, status: str = "all", type: str = "all", cycle: int = 0, all: bool = False,
                         size: int = 30, next: str = None) -> {}:  # 01
        url = f"governance/proposals?status={status}&type={type}&cycle={cycle}"
        if all is not None:
            url += f"&all={all}"

        return self._ocean._conn.get(url, size=size, next=next)

    def getGovProposal(self, id: str) -> {}:  # 02

        return self._ocean._conn.get(f"governance/proposals/{id}")

    def listGovProposalVotes(self, id: str, masternodeId: str = "all", cycle: int = 0, all: bool = False,
                             size: int = 30, next: str = None) -> {}:  # 03
        url = f"governance/proposals/{id}/votes?masternode={masternodeId}&cycle={cycle}"

        if all is not None:
            url += f"&all={all}"

        return self._ocean._conn.get(url, size=size, next=next)
