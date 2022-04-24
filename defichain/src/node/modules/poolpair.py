from ..util import BuildJson


class Poolpair:
    def __init__(self, node):
        self._node = node
        
    def addpoolliquidity(self, _from, shareAddress, inputs=None):  # 01
        return self._node._rpc.call("addpoolliquidity", _from, shareAddress, inputs)

    def compositeswap(self, _from, tokenFrom, amountFrom, to, tokenTo, maxPrice=None, inputs=None):  # 02
        metadata = BuildJson()
        metadata.append("from", _from)
        metadata.append("tokenFrom", tokenFrom)
        metadata.append("amountFrom", amountFrom)
        metadata.append("to", to)
        metadata.append("tokenTo", tokenTo)
        metadata.append("maxPrice", maxPrice)
        return self._node._rpc.call("compositeswap", metadata.build(), inputs)

    def createpoolpair(self, tokenA, tokenB, commission, status, ownerAddress, customRewards=None, pairSymbol=None, inputs=None):  # 03
        metadata = BuildJson()
        metadata.append("tokenA", tokenA)
        metadata.append("tokenB", tokenB)
        metadata.append("commission", commission)
        metadata.append("status", status)
        metadata.append("ownerAddress", ownerAddress)
        metadata.append("customRewards", customRewards)
        metadata.append("pairSymbol", pairSymbol)
        return self._node._rpc.call("createpoolpair", metadata.build(), inputs)

    def getpoolpair(self, key, verbose=None):  # 04
        return self._node._rpc.call("getpoolpair", key, verbose)

    def listpoolpairs(self, start=None, including_start=None, limit=None, verbose=None):  # 05
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listpoolpairs", pagination.build(), verbose)

    def listpoolshares(self, start=None, including_start=None, limit=None, verbose=None, is_mine_only=None):  # 06
        verbose = True if verbose is None else verbose
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listpoolshares", pagination.build(), verbose, is_mine_only)

    def poolswap(self, _from, tokenFrom, amountFrom, to, tokenTo, maxPrice=None, inputs=None):  # 07
        metadata = BuildJson()
        metadata.append("from", _from)
        metadata.append("tokenFrom", tokenFrom)
        metadata.append("amountFrom", amountFrom)
        metadata.append("to", to)
        metadata.append("tokenTo", tokenTo)
        metadata.append("maxPrice", maxPrice)
        return self._node._rpc.call("poolswap", metadata.build(), inputs)

    def removepoolliquidity(self, _from, poolSymbol, amount, inputs=None):  # 08
        return self._node._rpc.call("removepoolliquidity", _from, f"{amount}@{poolSymbol}", inputs)

    def testpoolswap(self, _from, tokenFrom, amountFrom, to, tokenTo, maxPrice=None, path=None, verbose=None):  # 09
        path = "direct" if path is None else path

        metadata = BuildJson()
        metadata.append("from", _from)
        metadata.append("tokenFrom", tokenFrom)
        metadata.append("amountFrom", amountFrom)
        metadata.append("to", to)
        metadata.append("tokenTo", tokenTo)
        metadata.append("maxPrice", maxPrice)
        return self._node._rpc.call("testpoolswap", metadata.build(), path, verbose)

    def updatepoolpair(self, pool, status=None, commission=None, ownerAddress=None, customRewards=None, inputs=None):  # 10
        metadata = BuildJson()
        metadata.append("pool", pool)
        metadata.append("status", status)
        metadata.append("commission", commission)
        metadata.append("ownerAddress", ownerAddress)
        metadata.append("customRewards", customRewards)
        return self._node._rpc.call("updatepoolpair", metadata.build(), inputs)
