import pytest
from tests.node.util import createNode

# Import Exceptions
from defichain.exceptions.InternalServerError import InternalServerError

node = createNode()


@pytest.mark.query
def test_clearmempool():  # 01
    mempool = node.blockchain.clearmempool()
    assert mempool or mempool == []


@pytest.mark.query
def test_getbestblockhash():  # 02
    assert node.blockchain.getbestblockhash()


@pytest.mark.query
def test_getblock():  # 03
    blockhash = "934d72c71e768db9dd10c1279fd00389f576317c72f22a149566a18097046d0d"
    assert node.blockchain.getblock(blockhash)
    assert node.blockchain.getblock(blockhash=blockhash)


@pytest.mark.query
def test_getblockchaininfo():  # 04
    assert node.blockchain.getblockchaininfo()


@pytest.mark.query
def test_getblockcount():  # 05
    assert node.blockchain.getblockcount()


@pytest.mark.query
def test_getblockfilter():  # 06
    """
    Node only supports filtertype if it is started with argument: -blockfilterindex
    """
    blockhash = "934d72c71e768db9dd10c1279fd00389f576317c72f22a149566a18097046d0d"
    string = ".* RPC_MISC_ERROR: Index is not enabled for filtertype basic"
    with pytest.raises(InternalServerError, match=string):
        assert node.blockchain.getblockfilter(blockhash)
        assert node.blockchain.getblockfilter(blockhash, "basic")
        assert node.blockchain.getblockfilter(blockhash=blockhash, filtertype="basic")


@pytest.mark.query
def test_getblockhash():  # 07
    height = 0
    assert node.blockchain.getblockhash(height)
    assert node.blockchain.getblockhash(height=height)


@pytest.mark.query
def test_getblockheader():  # 08
    blockhash = "934d72c71e768db9dd10c1279fd00389f576317c72f22a149566a18097046d0d"
    assert node.blockchain.getblockheader(blockhash)
    assert node.blockchain.getblockheader(blockhash, False)
    assert node.blockchain.getblockheader(blockhash, verbose=False)


@pytest.mark.query
def test_getblockstats():  # 09
    hash = "934d72c71e768db9dd10c1279fd00389f576317c72f22a149566a18097046d0d"
    height = 100
    assert node.blockchain.getblockstats(hash)
    assert node.blockchain.getblockstats(height)
    assert node.blockchain.getblockstats(hash, ["height", "txs", "minfee"])
    assert node.blockchain.getblockstats(height, ["height", "txs", "minfee"])
    assert node.blockchain.getblockstats(hash_or_height=hash, stats=["height", "txs", "minfee"])
    assert node.blockchain.getblockstats(hash_or_height=height, stats=["height", "txs", "minfee"])


@pytest.mark.query
def test_getchaintips():  # 10
    assert node.blockchain.getchaintips()


@pytest.mark.query
def test_getchaintxstats():  # 11
    nblocks = 100
    blockhash = "934d72c71e768db9dd10c1279fd00389f576317c72f22a149566a18097046d0d"
    assert node.blockchain.getchaintxstats()
    assert node.blockchain.getchaintxstats(nblocks, blockhash)
    assert node.blockchain.getchaintxstats(nblocks=nblocks, blockhash=blockhash)


@pytest.mark.query
def test_getdifficulty():  # 12
    assert node.blockchain.getdifficulty()


@pytest.mark.query
def test_getgov():  # 13
    names = ["ATTRIBUTES", "ICX_TAKERFEE_PER_BTC", "LP_DAILY_LOAN_TOKEN_REWARD",
             "LP_LOAN_TOKEN_SPLITS", "LP_DAILY_DFI_REWARD", "LOAN_LIQUIDATION_PENALTY",
             "LP_SPLITS", "ORACLE_BLOCK_INTERVAL", "ORACLE_DEVIATION"]
    for name in names:
        assert node.blockchain.getgov(name)


@pytest.mark.query
def test_getmempoolancestors():  # 14
    while True:
        txid = node.blockchain.getrawmempool()
        if txid:
            break
    result1 = node.blockchain.getmempoolancestors(txid[0])
    assert result1 or result1 == []
    result2 = node.blockchain.getmempoolancestors(txid[0], True)
    assert result2 or result2 == {}
    result3 = node.blockchain.getmempoolancestors(txid=txid[0], verbose=True)
    assert result3 or result3 == {}


@pytest.mark.query
def test_getmempooldescendants():  # 15
    while True:
        txid = node.blockchain.getrawmempool()
        if txid:
            break
    result1 = node.blockchain.getmempooldescendants(txid[0])
    assert result1 or result1 == []
    result2 = node.blockchain.getmempooldescendants(txid[0], True)
    assert result2 or result2 == {}
    result3 = node.blockchain.getmempooldescendants(txid=txid[0], verbose=True)
    assert result3 or result3 == {}


@pytest.mark.query
def test_getmempoolentry():  # 16
    while True:
        txid = node.blockchain.getrawmempool()
        if txid:
            break
    assert node.blockchain.getmempoolentry(txid[0])


@pytest.mark.query
def test_getmempoolinfo():  # 17
    assert node.blockchain.getmempoolinfo()


@pytest.mark.query
def test_getrawmempool():  # 18
    result = node.blockchain.getrawmempool()
    assert result or result == []
    result2 = node.blockchain.getrawmempool(True)
    assert result2 or result2 == []
    result3 = node.blockchain.getrawmempool(verbose=True)
    assert result3 or result3 == []


@pytest.mark.query
def test_gettxout():  # 19
    txid = "be1e5d5f26752d6957e527c94c8b0758b7ce30b01bbc5f5f97db28fa2a3b4e2d"
    n = 0
    result1 = node.blockchain.gettxout(txid, n)
    assert result1 or result1 is None
    result2 = node.blockchain.gettxout(txid=txid, n=n)
    assert result2 or result2 is None
    result3 = node.blockchain.gettxout(txid=txid, n=n, include_mempool=True)
    assert result3 or result3 is None


@pytest.mark.query
def test_gettxoutproof():  # 20
    txid = "be1e5d5f26752d6957e527c94c8b0758b7ce30b01bbc5f5f97db28fa2a3b4e2d"
    blockhash = "3da537b48af9ff99d472486c2ecbc34aa84a22f43a0a900cc0168ab4fc460c10"
    assert node.blockchain.gettxoutproof([txid], blockhash)
    assert node.blockchain.gettxoutproof([txid], blockhash=blockhash)


@pytest.mark.query
def test_gettxoutsetinfo():  # 21
    assert node.blockchain.gettxoutsetinfo()


@pytest.mark.query
def test_isappliedcustomtx():  # 22
    txid = "be1e5d5f26752d6957e527c94c8b0758b7ce30b01bbc5f5f97db28fa2a3b4e2d"
    blockHeight = 1825112
    assert node.blockchain.isappliedcustomtx(txid, blockHeight)
    assert node.blockchain.isappliedcustomtx(txid=txid, blockHeight=blockHeight)


@pytest.mark.query
def test_listgovs():  # 23
    assert node.blockchain.listgovs()


@pytest.mark.query
def test_listsmartcontracts():  # 24
    assert node.blockchain.listsmartcontracts()


@pytest.mark.query
def test_preciousblock():  # 25
    blockhash = "3da537b48af9ff99d472486c2ecbc34aa84a22f43a0a900cc0168ab4fc460c10"
    assert node.blockchain.preciousblock(blockhash) is None
    assert node.blockchain.preciousblock(blockhash=blockhash) is None


@pytest.mark.query
def test_pruneblockchain():  # 26
    height = 1825112
    with pytest.raises(InternalServerError):
        assert node.blockchain.pruneblockchain(height)
        assert node.blockchain.pruneblockchain(height=height)


@pytest.mark.query
def test_savemempool():  # 27
    assert node.blockchain.savemempool() is None


@pytest.mark.query
def test_scantxoutset():  # 28
    assert True


@pytest.mark.query
def test_setgov():  # 29
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Need foundation member authorization"
    with pytest.raises(InternalServerError, match=string):
        assert node.blockchain.setgov({"ORACLE_BLOCK_INTERVAL": 60})
        assert node.blockchain.setgov({"ORACLE_BLOCK_INTERVAL": 60}, [])
        assert node.blockchain.setgov(variables={"ORACLE_BLOCK_INTERVAL": 60}, inputs=[])


@pytest.mark.query
def test_setgovheight():  # 30
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Need foundation member authorization"
    with pytest.raises(InternalServerError, match=string):
        assert node.blockchain.setgovheight({"ORACLE_DEVIATION": 1}, 20000000)
        assert node.blockchain.setgovheight({"ORACLE_DEVIATION": 1}, 20000000, [])
        assert node.blockchain.setgovheight(variables={"ORACLE_DEVIATION": 1}, height=20000000, inputs=[])
        assert node.blockchain.setgovheight(variables={"LP_SPLITS": {"2": 0.2, "3": 0.8}}, height=20000000, inputs=[])


@pytest.mark.query
def test_verifychain():  # 31
    assert node.blockchain.verifychain()
    assert node.blockchain.verifychain(1, 10)
    assert node.blockchain.verifychain(checklevel=1, nblocks=10)


@pytest.mark.query
def test_verifytxoutproof():  # 32
    txid = "d6e2b314f928ba02fa844a94c75baf43dbab4c095b7592f7df18d504765072e3"
    blockhash = "090d161e7f6be039bb416ae3033d683d00b6c71a7102156a77af8c0e6baba242"
    proof = node.blockchain.gettxoutproof([txid], blockhash=blockhash)
    assert node.blockchain.verifytxoutproof(proof)
    assert node.blockchain.verifytxoutproof(proof=proof)
