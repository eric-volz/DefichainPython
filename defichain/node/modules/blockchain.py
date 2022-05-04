class Blockchain:
    def __init__(self, node):
        self._node = node

    def clearmempool(self):  # 01
        return self._node._rpc.call("clearmempool")

    def getbestblockhash(self):  # 02
        return self._node._rpc.call("getbestblockhash")

    def getblock(self, blockhash, verbosity=1):  # 03
        return self._node._rpc.call("getblock", blockhash, verbosity)

    def getblockchaininfo(self):  # 04
        return self._node._rpc.call("getblockchaininfo")

    def getblockcount(self):  # 05
        return self._node._rpc.call("getblockcount")

    def getblockfilter(self, blockhash, filtertype="basic"):  # 06
        return self._node._rpc.call("getblockfilter", blockhash, filtertype)

    def getblockhash(self, height):  # 07
        return self._node._rpc.call("getblockhash", height)

    def getblockheader(self, blockhash, verbose=True):  # 08
        return self._node._rpc.call("getblockheader", blockhash, verbose)

    def getblockstats(self, hash_or_height, stats=None):  # 09
        return self._node._rpc.call("getblockstats", hash_or_height, stats)

    def getchaintips(self):  # 10
        return self._node._rpc.call("getchaintips")

    def getchaintxstats(self, nblocks=86400, blockhash=None):  # 11
        return self._node._rpc.call("getchaintxstats", nblocks, blockhash)

    def getdifficulty(self):  # 12
        return self._node._rpc.call("getdifficulty")

    def getgov(self, name):  # 13
        return self._node._rpc.call("getgov", name)

    def getmempoolancestors(self, txid, verbose=False):  # 14
        return self._node._rpc.call("getmempoolancestors", txid, verbose)

    def getmempooldescendants(self, txid, verbose=False):  # 15
        return self._node._rpc.call("getmempooldescendants", txid, verbose)

    def getmempoolentry(self, txid):  # 16
        return self._node._rpc.call("getmempoolentry", txid)

    def getmempoolinfo(self):  # 17
        return self._node._rpc.call("getmempoolinfo")

    def getrawmempool(self, verbose=False):  # 18
        return self._node._rpc.call("getrawmempool", verbose)

    def gettxout(self, txid, n, include_mempool=True):  # 19
        return self._node._rpc.call("gettxout", txid, n, include_mempool)

    def gettxoutproof(self, txids, blockhash=None):  # 20
        return self._node._rpc.call("gettxoutproof", txids, blockhash)

    def gettxoutsetinfo(self):  # 21
        return self._node._rpc.call("gettxoutsetinfo")

    def isappliedcustomtx(self, txid, blockHeight):  # 22
        return self._node._rpc.call("isappliedcustomtx", txid, blockHeight)

    def listgovs(self):  # 23
        return self._node._rpc.call("listgovs")

    def listsmartcontracts(self):
        return self._node._rpc.call("listsmartcontracts")  # 24

    def preciousblock(self, blockhash):  # 25
        return self._node._rpc.call("preciousblock", blockhash)

    def pruneblockchain(self, height):  # 26
        return self._node._rpc.call("pruneblockchain", height)

    def savemempool(self):  # 27
        return self._node._rpc.call("savemempool")

    def scantxoutset(self, action, scanobjects):  # 28
        return self._node._rpc.call("scantxoutset", action, scanobjects)

    def setgov(self, variables, inputs=None):  # 29
        return self._node._rpc.call("setgov", variables, inputs)

    def setgovheight(self, variables, height, inputs=None):  # 30
        return self._node._rpc.call("setgovheight", variables, height, inputs)

    def verifychain(self, checklevel=3, nblocks=6):  # 31
        return self._node._rpc.call("verifychain", checklevel, nblocks)

    def verifytxoutproof(self, proof):  # 32
        return self._node._rpc.call("verifytxoutproof", proof)
