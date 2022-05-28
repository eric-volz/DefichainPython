from ..util import BuildJson


class Stats:
    def __init__(self, node):
        self._node = node

    def getrpcstats(self, command):
        return self._node._rpc.call("getrpcstats", command)

    def listrpcstats(self):
        return self._node._rpc.call("listrpcstats")
