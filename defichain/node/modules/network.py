class Network:
    def __init__(self, node):
        self._node = node

    def addnode(self, node, command):  # 01
        return self._node._rpc.call("addnode", node, command)

    def clearbanned(self):  # 02
        return self._node._rpc.call("clearbanned")

    def disconnectnode(self, address="", nodeid=None):  # 03
        return self._node._rpc.call("disconnectnode", address, nodeid)

    def getaddednodeinfo(self, node=None):  # 04
        return self._node._rpc.call("getaddednodeinfo", node)

    def getconnectioncount(self):  # 05
        return self._node._rpc.call("getconnectioncount")

    def getnettotals(self):  # 06
        return self._node._rpc.call("getnettotals")

    def getnetworkinfo(self):  # 07
        return self._node._rpc.call("getnetworkinfo")

    def getnodeaddresses(self, count=1):  # 08
        return self._node._rpc.call("getnodeaddresses", count)

    def getpeerinfo(self):  # 09
        return self._node._rpc.call("getpeerinfo")

    def getversioninfo(self):  # 10
        return self._node._rpc.call("getversioninfo")

    def listbanned(self):  # 11
        return self._node._rpc.call("listbanned")

    def ping(self):  # 12
        return self._node._rpc.call("ping")

    def setban(self, subnet, command, bantime=0, absolute=False):  # 13
        return self._node._rpc.call("setban", subnet, command, bantime, absolute)

    def setnetworkactive(self, state):  # 14
        return self._node._rpc.call("setnetworkactive", state)
