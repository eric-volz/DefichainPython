from ..util import BuildJson


class Tokens:
    def __init__(self, node):
        self.node = node

    def createtoken(self, symbol, collateralAddress, name=None, isDAT=None, decimal=None, limit=None, mintable=None, tradeable=None, inputs=None):  # 01
        metadata = BuildJson()
        metadata.append("symbol", symbol)
        metadata.append("collateralAddress", collateralAddress)
        metadata.append("name", name)
        metadata.append("isDAT", isDAT)
        metadata.append("decimal", decimal)
        metadata.append("limit", limit)
        metadata.append("mintable", mintable)
        metadata.append("tradeable", tradeable)
        return self.node._rpc.call("createtoken", metadata.build(), inputs)

    def decodecustomtx(self, hexstring, iswitness=None):  # 02
        return self.node._rpc.call("decodecustomtx", hexstring, iswitness)

    def getcustomtx(self, txid, blockhash=None):  # 03
        return self.node._rpc.call("getcustomtx", txid, blockhash)

    def gettoken(self, key):  # 04
        return self.node._rpc.call("gettoken", key)

    def listtokens(self, start=None, including_start=None, limit=None, verbose=None):  # 05
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self.node._rpc.call("listtokens", pagination.build(), verbose)

    def minttokens(self, token, amount):  # 06
        return self.node._rpc.call("minttokens", f"{amount}@{token}")

    def updatetoken(self, token, symbol, name=None, isDAT=None, mintable=None, tradeable=None, finalize=None, inputs=None):  # 07
        metadata = BuildJson()
        metadata.append("symbol", symbol)
        metadata.append("name", name)
        metadata.append("isDAT", isDAT)
        metadata.append("mintable", mintable)
        metadata.append("tradeable", tradeable)
        metadata.append("finalize", finalize)
        return self.node._rpc.call("updatetoken", token, metadata.build(), inputs)
