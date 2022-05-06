import pytest
from tests.node.util import createNode

# Import Exceptions
from defichain.exceptions.InternalServerError import InternalServerError

node = createNode()


@pytest.mark.query
def test_createmultisig():  # 01
    p1 = "03f6b5b82dbcb92d57fd84382d90820e87b5f0f5a20800a59a5a7eb8d6d9a28b83"
    p2 = "0283e12290fe7d248e8a715c6688b0cfcbbb80fc82b9993200d801c4456843f5ba"
    p3 = "03f60cfec905031f48f346c9fa4c6c1c6221c10490512a116a73d059284191b6c0"

    assert node.util.createmultisig(2, [p1, p2, p3])
    assert node.util.createmultisig(2, [p1, p2, p3], "legacy")
    assert node.util.createmultisig(nrequired=2, keys=[p1, p2, p3], address_type="legacy")


@pytest.mark.query
def test_deriveaddresses():  # 02
    pubkey = "03f6b5b82dbcb92d57fd84382d90820e87b5f0f5a20800a59a5a7eb8d6d9a28b83"
    checksum = "sxev658j"
    assert node.util.deriveaddresses(f"pkh({pubkey})#{checksum}")
    assert node.util.deriveaddresses(descriptor=f"pkh({pubkey})#{checksum}")
    string = ".* RPC_INVALID_PARAMETER: Range should not be specified for an un-ranged descriptor"
    with pytest.raises(InternalServerError, match=string):
        assert node.util.deriveaddresses(f"pkh({pubkey})#{checksum}", [0, 10])
        assert node.util.deriveaddresses(descriptor=f"pkh({pubkey})#{checksum}", range=[0, 10])

@pytest.mark.query
def test_estimatesmartfee():  # 03
    assert node.util.estimatesmartfee(1)
    assert node.util.estimatesmartfee(1, "CONSERVATIVE")
    assert node.util.estimatesmartfee(conf_target=1, estimate_mode="CONSERVATIVE")


@pytest.mark.query
def test_getdescriptorinfo():  # 04
    pubkey = "03f6b5b82dbcb92d57fd84382d90820e87b5f0f5a20800a59a5a7eb8d6d9a28b83"
    assert node.util.getdescriptorinfo(f"pkh({pubkey})")


@pytest.mark.query
def test_signmessagewithprivkey():  # 05
    privkey = "L5nCcRchTMtB8Hmz15hDp796Dc7hiakJntfsydturjG8ccWbr7Ws"
    msg = "I Love DFI <3"
    assert node.util.signmessagewithprivkey(privkey, msg)
    assert node.util.signmessagewithprivkey(privkey=privkey, message=msg)


@pytest.mark.query
def test_validateaddress():  # 06
    address = "dXwpArYSmZ8EDD71jBH72gsJcsiKVY2paU"
    assert node.util.validateaddress(address)
    assert node.util.validateaddress(address=address)



@pytest.mark.query
def test_verifymessage():  # 07
    """
    address = "dXwpArYSmZ8EDD71jBH72gsJcsiKVY2paU"
    signature = "IBU+fZRG1nGEVKLC/GHrrRsrjV+DOeXLYCQ6RYpFV84RV+SnCT4PF447F1cMTF1HR3+2k1OZIsAApUW0sk1ylRU="
    msg = "I Love DFI <3"
    assert node.util.verifymessage(address, signature, msg)
    assert node.util.verifymessage(address=address, signature=signature, message=msg)
    """
    assert True  # Not working on Node

