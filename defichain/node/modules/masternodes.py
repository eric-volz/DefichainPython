from ..util import BuildJson


class Masternodes:
    def __init__(self, node):
        self._node = node

    def createmasternode(self, ownerAddress, operatorAddress=None, inputs=[], timelock=None):  # 01
        operatorAddress = ownerAddress if operatorAddress is None else operatorAddress
        return self._node._rpc.call("createmasternode", ownerAddress, operatorAddress, inputs, timelock)

    def getactivemasternodecount(self, blockCount=20160):  # 02
        return self._node._rpc.call("getactivemasternodecount", blockCount)

    def getanchorteams(self, blockHeight=None):  # 03
        return self._node._rpc.call("getanchorteams", blockHeight)

    def getmasternode(self, mn_id):  # 04
        return self._node._rpc.call("getmasternode", mn_id)

    def getmasternodeblocks(self, id=None, ownerAddress=None, operatorAddress=None, depth=None):  # 08
        depth = self._node.blockchain.getblockcount() if depth is None else depth
        identifier = BuildJson()
        identifier.append("id", id)
        identifier.append("ownerAddress", ownerAddress)
        identifier.append("operatorAddress", operatorAddress)
        return self._node._rpc.call("getmasternodeblocks", identifier.build(), depth)

    def listanchors(self):  # 06
        return self._node._rpc.call("listanchors")

    def listmasternodes(self, start=None, including_start=False, limit=1000000, verbose=True):  # 07
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listmasternodes", pagination.build(), verbose)

    def resignmasternode(self, mn_id, inputs=None):  # 08
        return self._node._rpc.call("resignmasternode", mn_id, inputs)
