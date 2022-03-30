from ..util import BuildJson


class Masternodes:
    def __init__(self, node):
        self.node = node

    def createmasternode(self, ownerAddress, operatorAddress=None, inputs=None, timelock=None):  # 01
        operatorAddress = ownerAddress if operatorAddress is None else operatorAddress
        inputs = [] if inputs is None else inputs
        return self.node.rpc.call("createmasternode", ownerAddress, operatorAddress, inputs, timelock)

    def getactivemasternodecount(self, blockCount=None):  # 02
        return self.node.rpc.call("getactivemasternodecount", blockCount)

    def getanchorteams(self, blockHeight=None):  # 03
        return self.node.rpc.call("getanchorteams", blockHeight)

    def getmasternode(self, mn_id):  # 04
        return self.node.rpc.call("getmasternode", mn_id)

    def getmasternodeblocks(self, id=None, ownerAddress=None, operatorAddress=None, depth=None):  # 08
        identifier = BuildJson()
        identifier.append("id", id)
        identifier.append("ownerAddress", ownerAddress)
        identifier.append("operatorAddress", operatorAddress)
        return self.node.rpc.call("getmasternodeblocks", identifier.build(), depth)

    def listanchors(self):  # 06
        return self.node.rpc.call("listanchors")

    def listmasternodes(self, start=None, including_start=None, limit=None, verbose=None):  # 07
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self.node.rpc.call("listmasternodes", pagination.build(), verbose)

    def resignmasternode(self, mn_id, inputs=None):  # 08
        return self.node.rpc.call("resignmasternode", mn_id, inputs)
