class Zmq:
    def __init__(self, node):
        self.node = node

    def getzmqnotifications(self):
        return self.node._rpc.call("getzmqnotifications")
