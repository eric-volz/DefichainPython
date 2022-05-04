from ..util import BuildJson


class Tokens:
    def __init__(self, node):
        self._node = node

    def createtoken(self, symbol, collateralAddress, name=None, isDAT=None, decimal=None, limit=None, mintable=True,
                    tradeable=True, inputs=None):  # 01
        metadata = BuildJson()
        metadata.append("symbol", symbol)
        metadata.append("collateralAddress", collateralAddress)
        metadata.append("name", name)
        metadata.append("isDAT", isDAT)
        metadata.append("decimal", decimal)
        metadata.append("limit", limit)
        metadata.append("mintable", mintable)
        metadata.append("tradeable", tradeable)
        return self._node._rpc.call("createtoken", metadata.build(), inputs)

    def decodecustomtx(self, hexstring, iswitness=None):  # 02
        return self._node._rpc.call("decodecustomtx", hexstring, iswitness)

    def getcustomtx(self, txid, blockhash=None):  # 03
        return self._node._rpc.call("getcustomtx", txid, blockhash)

    def gettoken(self, key):  # 04
        return self._node._rpc.call("gettoken", key)

    def listtokens(self, start=None, including_start=False, limit=100, verbose=True):  # 05
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listtokens", pagination.build(), verbose)

    def minttokens(self, amounts, inputs=None):  # 06
        return self._node._rpc.call("minttokens", amounts, inputs)

    def updatetoken(self, token, symbol=None, name=None, isDAT=False, mintable=None, tradeable=None, finalize=None, inputs=None):  # 07
        metadata = BuildJson()
        metadata.append("symbol", symbol)
        metadata.append("name", name)
        metadata.append("isDAT", isDAT)
        metadata.append("mintable", mintable)
        metadata.append("tradeable", tradeable)
        metadata.append("finalize", finalize)
        return self._node._rpc.call("updatetoken", token, metadata.build(), inputs)
