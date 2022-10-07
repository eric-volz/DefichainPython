import pytest
from tests.util import createNode

# Import Exceptions
from defichain.exceptions.http.BadRequest import BadRequest

node = createNode()


@pytest.mark.query
def test_getblocktemplate():  # 01
    string = ".* RPC_INVALID_REQUEST: getblocktemplate can only be called by masternodes"
    with pytest.raises(BadRequest, match=string):
        assert node.mining.getblocktemplate()
        assert node.mining.getblocktemplate({})
        assert node.mining.getblocktemplate(template_request={})


@pytest.mark.query
def test_getmininginfo():  # 02
    assert node.mining.getmininginfo()


@pytest.mark.query
def test_getmintinginfo():  # 03
    assert node.mining.getmintinginfo()


@pytest.mark.query
def test_getnetworkhashps():  # 04
    assert node.mining.getnetworkhashps()
    assert node.mining.getnetworkhashps(120, -1)
    assert node.mining.getnetworkhashps(nblocks=120, height=-1)


@pytest.mark.query
def test_prioritisetransaction():  # 05
    txid = "16960f9001a021d745757714baf25fe7f8a4637d92efe708ecac77cc0da7e404"
    assert node.mining.prioritisetransaction(txid, 10000)
    assert node.mining.prioritisetransaction(txid, 10000, 0)
    assert node.mining.prioritisetransaction(txid=txid, fee_delta=10000, dummy=0)


@pytest.mark.query
def test_submitblock():  # 06
    hex="000000202d120af2bdbd115199f04ce2369457f29809c5c76bfc2b3631f7e715002f5865934e2276696daba9f3f93a5c81ff8be17" \
        "164ab0d49c668fe2b19daafc9caee964be97362be7534185ca48cd64f8f118a9c59cb38d71f0648d4d892566548e2a13289dbdc2e" \
        "fdb22919531c00000000004e000000000000004120de510ff026945302ce0ce8abd9bde6ebb77bd8805c65abca1ec4ea402666aa7" \
        "6313f618a7c4e9445cb2323add0dd2979ff8c4ce843c1c9964d471c20f9032b140104000000000101000000000000000000000000" \
        "0000000000000000000000000000000000000000ffffffff050319531c00ffffffff033b8180ef010000001976a914c5dbd91efad" \
        "0e2ccc02942cea009fa12e0bac3b488ac0046a7fe480000000017a914dd7730517e0e4969b4e43677ff5bee682e53420a87000000" \
        "000000000000266a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf9000120000000000" \
        "000000000000000000000000000000000000000000000000000000000000000"
    assert node.mining.submitblock(hex)
    assert node.mining.submitblock(hex, "ignored")
    assert node.mining.submitblock(hexdata=hex, dummy="ignored")


@pytest.mark.query
def test_submitheader():  # 06
    hex = "000000202d120af2bdbd115199f04ce2369457f29809c5c76bfc2b3631f7e715002f5865934e2276696daba9f3f93a5c81ff8be17" \
          "164ab0d49c668fe2b19daafc9caee964be97362be7534185ca48cd64f8f118a9c59cb38d71f0648d4d892566548e2a13289dbdc2e" \
          "fdb22919531c00000000004e000000000000004120de510ff026945302ce0ce8abd9bde6ebb77bd8805c65abca1ec4ea402666aa7" \
          "6313f618a7c4e9445cb2323add0dd2979ff8c4ce843c1c9964d471c20f9032b140104000000000101000000000000000000000000" \
          "0000000000000000000000000000000000000000ffffffff050319531c00ffffffff033b8180ef010000001976a914c5dbd91efad" \
          "0e2ccc02942cea009fa12e0bac3b488ac0046a7fe480000000017a914dd7730517e0e4969b4e43677ff5bee682e53420a87000000" \
          "000000000000266a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf9000120000000000" \
          "000000000000000000000000000000000000000000000000000000000000000"
    assert node.mining.submitheader(hex) is None
    assert node.mining.submitheader(hexdata=hex) is None
