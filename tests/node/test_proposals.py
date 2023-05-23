import pytest

# Import Exceptions
from defichain.exceptions.http.BadRequest import BadRequest
from defichain.exceptions.http.InternalServerError import InternalServerError

from tests.util import load_secrets_conf

from . import node
address = load_secrets_conf()["wallet_address"]


@pytest.mark.query
def test_creategovcfp():  # 01
    string = ".* RPC_WALLET_ERROR: Insufficient funds"
    with pytest.raises(InternalServerError, match=string):
        assert node.proposals.creategovcfp("Test", "Test", 0, address)
    with pytest.raises(InternalServerError, match=string):
        assert node.proposals.creategovcfp("Test", "Test", 0, address, "hash", 1, [])
    with pytest.raises(InternalServerError, match=string):
        assert node.proposals.creategovcfp(title="Test", context="Test", amount=0,
                                           payoutAddress=address, contextHash="hash",
                                           cycles=1, inputs=[])


@pytest.mark.query
def test_creategovvoc():  # 02
    string = ".* RPC_WALLET_ERROR: Insufficient funds"
    with pytest.raises(InternalServerError, match=string):
        assert node.proposals.creategovvoc("Test", "Test")
    with pytest.raises(InternalServerError, match=string):
        assert node.proposals.creategovvoc("Test", "Test", "hash", False, [])
    with pytest.raises(InternalServerError, match=string):
        assert node.proposals.creategovvoc(title="Test", context="Test", contextHash="hash", emergency=False, inputs=[])


@pytest.mark.query
def test_getgovproposal():  # 03
    string = ".* RPC_INVALID_PARAMETER: Proposal <df925903d16ddcde1c10062b20f990a2f653002d37fe9633daf978a45bd7c612> does not exist"
    with pytest.raises(InternalServerError, match=string):
        assert node.proposals.getgovproposal("df925903d16ddcde1c10062b20f990a2f653002d37fe9633daf978a45bd7c612")
    with pytest.raises(InternalServerError, match=string):
        assert node.proposals.getgovproposal(proposalId="df925903d16ddcde1c10062b20f990a2f653002d37fe9633daf978a45bd7c612")


@pytest.mark.query
def test_listgovproposals():  # 04
    result1 = node.proposals.listgovproposals()
    assert result1 == [] or result1
    result2 = node.proposals.listgovproposals("all", "all")
    assert result2 == [] or result2
    result3 = node.proposals.listgovproposals(type="all", status="all")
    assert result3 == [] or result3


@pytest.mark.query
def test_listgovproposalvotes():  # 05
    string = ".* RPC_INVALID_PARAMETER: Proposal <df925903d16ddcde1c10062b20f990a2f653002d37fe9633daf978a45bd7c612> does not exist"
    with pytest.raises(InternalServerError, match=string):
        assert node.proposals.listgovproposalvotes("df925903d16ddcde1c10062b20f990a2f653002d37fe9633daf978a45bd7c612")

    result1 = node.proposals.listgovproposalvotes("df925903d16ddcde1c10062b20f990a2f653002d37fe9633daf978a45bd7c612", "all", -1)
    assert result1 == [] or result1
    result2 = node.proposals.listgovproposalvotes(proposalId="df925903d16ddcde1c10062b20f990a2f653002d37fe9633daf978a45bd7c612",
                                               masternode="all", cycle=-1)
    assert result2 == [] or result2


@pytest.mark.query
def test_votegov():  # 06
    string = ".* RPC_INVALID_PARAMETER: Proposal <df925903d16ddcde1c10062b20f990a2f653002d37fe9633daf978a45bd7c612> does not exist"
    with pytest.raises(InternalServerError, match=string):
        assert node.proposals.votegov("df925903d16ddcde1c10062b20f990a2f653002d37fe9633daf978a45bd7c612",
                                      "e54d0814d406317dfaa38f365471ff59fb7f7725769c0aecf3d0830a59de0100",
                                      "yes")
    with pytest.raises(InternalServerError, match=string):
        assert node.proposals.votegov("df925903d16ddcde1c10062b20f990a2f653002d37fe9633daf978a45bd7c612",
                                      "e54d0814d406317dfaa38f365471ff59fb7f7725769c0aecf3d0830a59de0100",
                                      "yes", [])
    with pytest.raises(InternalServerError, match=string):
        assert node.proposals.votegov(proposalId="df925903d16ddcde1c10062b20f990a2f653002d37fe9633daf978a45bd7c612",
                                      masternodeId="e54d0814d406317dfaa38f365471ff59fb7f7725769c0aecf3d0830a59de0100",
                                      decision="yes",
                                      inputs=[])
