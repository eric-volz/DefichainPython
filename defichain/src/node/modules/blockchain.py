class Blockchain:
    def __init__(self, node):
        self.node = node

    def clearmempool(self):  # 01
        return self.node.rpc.call("clearmempool")

    def getbestblockhash(self):  # 02
        return self.node.rpc.call("getbestblockhash")

    def getblock(self, blockhash, verbosity=None):  # 03
        return self.node.rpc.call("getblock", blockhash, verbosity)

    def getblockchaininfo(self):  # 04
        return self.node.rpc.call("getblockchaininfo")

    def getblockcount(self):  # 05
        return self.node.rpc.call("getblockcount")

    def getblockfilter(self, blockhash, filtertype=None):  # 06
        return self.node.rpc.call("getblockfilter", blockhash, filtertype)

    def getblockhash(self, height):  # 07
        return self.node.rpc.call("getblockhash", height)

    def getblockheader(self, blockhash, verbose=None):  # 08
        verbose = True if verbose is None else verbose
        return self.node.rpc.call("getblockheader", blockhash, verbose)

    def getblockstats(self, hash_or_height, stats=None):  # 09
        return self.node.rpc.call("getblockstats", hash_or_height, stats)

    def getchaintips(self):  # 10
        return self.node.rpc.call("getchaintips")

    def getchaintxstats(self, nblocks=None, blockhash=None):  # 11
        nblocks = 86400 if nblocks is None else nblocks
        return self.node.rpc.call("getchaintxstats", nblocks, blockhash)

    def getdifficulty(self):  # 12
        return self.node.rpc.call("getdifficulty")

    def getgov(self, name):  # 13
        return self.node.rpc.call("getgov", name)

    def getmempoolancestors(self, txid, verbose=None):  # 14
        return self.node.rpc.call("getmempoolancestors", txid, verbose)

    def getmempooldescendants(self, txid, verbose=None):  # 15
        return self.node.rpc.call("getmempooldescendants", txid, verbose)

    def getmempoolentry(self, txid):  # 16
        return self.node.rpc.call("getmempoolentry", txid)

    def getmempoolinfo(self):  # 17
        return self.node.rpc.call("getmempoolinfo")

    def getrawmempool(self, verbose=None):  # 18
        return self.node.rpc.call("getrawmempool", verbose)

    def gettxout(self, txid, n, include_mempool=None):  # 19
        return self.node.rpc.call("gettxout", txid, n, include_mempool)

    def gettxoutproof(self, txids, blockhash=None):  # 20
        return self.node.rpc.call("gettxoutproof", txids, blockhash)

    def gettxoutsetinfo(self):  # 21
        return self.node.rpc.call("gettxoutsetinfo")

    def isappliedcustomtx(self, txid, blockhash):  # 22
        return self.node.rpc.call("isappliedcustomtx", txid, blockhash)

    def listgovs(self):  # 23
        return self.node.rpc.call("listgovs")

    def preciousblock(self, blockhash):  # 24
        return self.node.rpc.call("preciousblock", blockhash)

    def pruneblockchain(self, height):  # 25
        return self.node.rpc.call("pruneblockchain", height)

    def savemempool(self):  # 26
        return self.node.rpc.call("savemempool")

    def scantxoutset(self, action, scanobjects):  # 27
        return self.node.rpc.call("scantxoutset", action, scanobjects)

    def setgov(self, variables, inputs=None):  # 28
        return self.node.rpc.call("setgov", variables, inputs)

    def setgovheight(self, variables, height, inputs=None):  # 29
        return self.node.rpc.call("setgovheight", variables, height, inputs)

    def verifychain(self, checklevel=None, nblocks=None):  # 30
        checklevel = 3 if checklevel is None else checklevel
        return self.node.rpc.call("verifychain", checklevel, nblocks)

    def verifytxoutproof(self, proof):  # 31
        return self.node.rpc.call("verifytxoutproof", proof)
