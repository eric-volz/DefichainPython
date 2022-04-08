class Network:
    def __init__(self, node):
        self.node = node

    def addnode(self, node, command):  # 01
        return self.node._rpc.call("addnode", node, command)

    def clearbanned(self):  # 02
        return self.node._rpc.call("clearbanned")

    def disconnectnode(self, address=None, nodeid=None):  # 03
        address = "" if address is None else address
        return self.node._rpc.call(address, nodeid)

    def getaddednodeinfo(self, node=None):  # 04
        return self.node._rpc.call("getaddednodeinfo", node)

    def getconnectioncount(self):  # 05
        return self.node._rpc.call("getconnectioncount")

    def getnettotals(self):  # 06
        return self.node._rpc.call("getnettotals")

    def getnetworkinfo(self):  # 07
        return self.node._rpc.call("getnetworkinfo")

    def getnodeaddresses(self, count=None):  # 08
        return self.node._rpc.call("getnodeaddresses", count)

    def getpeerinfo(self):  # 09
        return self.node._rpc.call("getpeerinfo")

    def getversioninfo(self):  # 10
        return self.node._rpc.call("getversioninfo")

    def listbanned(self):  # 11
        return self.node._rpc.call("listbanned")

    def ping(self):  # 12
        return self.node._rpc.call("ping")

    def setban(self, subnet, command, bantime=None, absolute=None):  # 13
        bantime = 0 if bantime is None else bantime
        return self.node._rpc.call("setban", subnet, command, bantime, absolute)

    def setnetworkactive(self, state):  # 14
        return self.node._rpc.call("setnetworkactive", state)
