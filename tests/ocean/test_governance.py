import pytest
from . import ocean


@pytest.mark.query
def test_listGovProposals():  # 01
    assert ocean.governance.listGovProposals()
    assert ocean.governance.listGovProposals("all", "all", 0, False, 30, None)
    assert ocean.governance.listGovProposals(status="all", type="all", cycle=0, all=False, size=30, next=None)


@pytest.mark.query
def test_getGovProposal():  # 02
    proposalId = "a252bea49341adb75842dd30442e5836f9e204e7fa96a1585983eca3b3b5407c"
    assert ocean.governance.getGovProposal(proposalId)
    assert ocean.governance.getGovProposal(id=proposalId)


@pytest.mark.query
def test_listGovProposalVotes():  # 03
    proposalId = "a252bea49341adb75842dd30442e5836f9e204e7fa96a1585983eca3b3b5407c"
    assert ocean.governance.listGovProposalVotes(proposalId)
    assert ocean.governance.listGovProposalVotes(proposalId, "all", 0, False, 30, None)
    assert ocean.governance.listGovProposalVotes(id=proposalId, masternodeId="all", cycle=0, all=False, size=30,
                                                 next=None)
