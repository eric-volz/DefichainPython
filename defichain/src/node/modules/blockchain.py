class Blockchain:
    def __init__(self, node):
        self.node = node

    def clearmempool(self):  # 01
        return self.node.rpc.call("clearmempool")

    def getbestblockhash(self):  # 02
        return self.node.rpc.call("getbestblockhash")

    def getblock(self, blockhash, verbosity=None):  # 03
        verbosity = verbosity if verbosity is not None else 1
        return self.node.rpc.call("getblock", blockhash, verbosity)

    def getblockchaininfo(self):  # 04
        return self.node.rpc.call("getblockchaininfo")

    def getblockcount(self):  # 05
        return self.node.rpc.call("getblockcount")

    def getblockfilter(self, blockhash, filtertype=None):  # 06
        filtertype = "basic" if filtertype is None else filtertype
        return self.node.rpc.call("getblockfilter", blockhash, filtertype)

    def getblockhash(self, height):  # 07
        return self.node.rpc.call("getblockhash", height)

    def getblockheader(self, blockhash, verbose=None):  # 08
        verbose = True if verbose is None else verbose
        return self.node.rpc.call("getblockheader", blockhash, verbose)
