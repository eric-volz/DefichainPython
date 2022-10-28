class Generating:
    def __init__(self, node):
        self._node = node

    def generatetoaddress(self, nblocks: int, address: str, maxtries: int = 1) -> ["str"]:  # 01
        """
        Mine blocks immediately to a specified address (before the RPC call returns)

        :param nblocks: (required) How many blocks are generated immediately
        :type nblocks: int
        :param address: (required) The address to send the newly generated DFI to
        :type address: str
        :param maxtries: (optional) How many iterations to try
        :type maxtries: int
        :return: [...] (array) -- hashes of blocks generated

        :example:

        Generate 11 blocks to myaddress

            >>> node.generating.generatetoaddress(11, address)
        """
        return self._node._rpc.call("generatetoaddress", nblocks, address, maxtries)
