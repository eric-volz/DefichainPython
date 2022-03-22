class Oracles:
    def __init__(self, node):
        self.node = node

    def getprice(self, currency, token):  # 04
        return self.node.rpc.call("getprice", {"currency": currency, "token": token})
