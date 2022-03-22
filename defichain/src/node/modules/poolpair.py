class Poolpair:
    def __init__(self, node):
        self.node = node

    def getpoolpair(self, key,  verbose=None):  # 04
        verbose = True if verbose is None else False
        return self.node.rpc.call("getpoolpair", key, verbose)

    def listpoolpairs(self, start=None, including_start=None, limit=None, verbose=None):  # 05
        start = 0 if start is None else start
        including_start = False if including_start is None else including_start
        limit = 100 if limit is None else limit
        verbose = True if verbose is None else verbose
        return self.node.rpc.call("listpoolpairs", {"start": start, "including_start": including_start, "limit": limit},
                                  verbose)
