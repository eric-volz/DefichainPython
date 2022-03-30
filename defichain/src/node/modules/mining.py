class Mining:
    def __init__(self, node):
        self.node = node

    def getblocktemplate(self, template_request=None):  # 01
        return self.node.rpc.call("getblocktemplate", template_request)

    def getmininginfo(self):  # 02
        return self.node.rpc.call("getmininginfo")

    def getmintinginfo(self):  # 03
        return self.node.rpc.call("getmintinginfo")

    def getnetworkhashps(self, nblocks=None, height=None):  # 04
        nblocks = 120 if nblocks is None else nblocks
        return self.node.rpc.call("getnetworkhashps", nblocks, height)

    def prioritisetransaction(self, txid, fee_delta, dummy=None):  # 05
        dummy = 0 if dummy is None else dummy
        return self.node.rpc.call("prioritisetransaction", txid, dummy, fee_delta)

    def submitblock(self, hexdata, dummy=None):  # 06
        return self.node.rpc.call("submitblock", hexdata, dummy)

    def submitheader(self, hexdata):  # 07
        return self.node.rpc.call("submitheader", hexdata)
