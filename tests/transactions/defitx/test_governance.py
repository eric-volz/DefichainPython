import pytest

from defichain.networks import DefichainMainnet
from defichain.transactions.defitx import DefiTx, CreateCfp, CreateVoc, Vote
from . import TestGovernance


@pytest.mark.transactions
def test_vote():  # 01
    vote_yes: Vote = Vote(proposalId=TestGovernance.proposalId, masternodeId=TestGovernance.masternodeId,
                          decision=TestGovernance.decision[0])
    vote_no: Vote = Vote(proposalId=TestGovernance.proposalId, masternodeId=TestGovernance.masternodeId,
                         decision=TestGovernance.decision[1])
    vote_neutral: Vote = Vote(proposalId=TestGovernance.proposalId, masternodeId=TestGovernance.masternodeId,
                              decision=TestGovernance.decision[2])

    assert vote_yes.serialize() == TestGovernance.vote_yes_serialized
    assert vote_no.serialize() == TestGovernance.vote_no_serialized
    assert vote_neutral.serialize() == TestGovernance.vote_neutral_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestGovernance.vote_yes_serialized).serialize() == \
           TestGovernance.vote_yes_serialized
    assert DefiTx.deserialize(DefichainMainnet, TestGovernance.vote_no_serialized).serialize() == \
           TestGovernance.vote_no_serialized
    assert DefiTx.deserialize(DefichainMainnet, TestGovernance.vote_neutral_serialized).serialize() == \
           TestGovernance.vote_neutral_serialized

