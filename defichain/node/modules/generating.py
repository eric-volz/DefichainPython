class Generating:
    def __init__(self, node):
        self._node = node

    def generatetoaddress(self, nblocks, address, maxtries=None):  # 01
        return self._node._rpc.call("generatetoaddress", nblocks, address, maxtries)
