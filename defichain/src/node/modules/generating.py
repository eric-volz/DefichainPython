class Generating:
    def __init__(self, node):
        self.node = node

    def generatetoaddress(self, nblocks, address, maxtries=None):  # 01
        return self.node.rpc.call("generatetoaddress", nblocks, address, maxtries)
