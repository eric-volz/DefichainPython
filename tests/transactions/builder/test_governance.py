import pytest
from . import builder_p2wpkh, TestGovernance

from defichain.transactions.rawtransactions import Transaction
from defichain.networks import DefichainMainnet


@pytest.mark.transactions
def test_vote():  # 01
    tx_yes = builder_p2wpkh.governance.vote(TestGovernance.proposal_id, TestGovernance.mn_id, "yes")
    tx_no = builder_p2wpkh.governance.vote(TestGovernance.proposal_id, TestGovernance.mn_id, "no")
    tx_neutral = builder_p2wpkh.governance.vote(TestGovernance.proposal_id, TestGovernance.mn_id, "neutral")

    assert tx_yes.serialize() == TestGovernance.vote_yes_serialized
    assert tx_no.serialize() == TestGovernance.vote_no_serialized
    assert tx_neutral.serialize() == TestGovernance.vote_neutral_serialized

    assert Transaction.deserialize(DefichainMainnet, tx_yes.serialize()).serialize() == tx_yes.serialize()
    assert Transaction.deserialize(DefichainMainnet, tx_no.serialize()).serialize() == tx_no.serialize()
    assert Transaction.deserialize(DefichainMainnet, tx_neutral.serialize()).serialize() == tx_neutral.serialize()
