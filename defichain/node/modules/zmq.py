class Zmq:
    def __init__(self, node):
        self._node = node

    def getzmqnotifications(self):
        return self._node._rpc.call("getzmqnotifications")
