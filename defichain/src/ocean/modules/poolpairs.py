# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/PoolPairs.ts

class Poolpairs:
    def __init__(self, ocean):
        self._ocean = ocean

    def list(self, size=30, next=None):  # 01
        return self._ocean._conn.get(f"poolpairs", size=size, next=next)

    def get(self, id):  # 02
        return self._ocean._conn.get(f"poolpairs/{id}")

    def listPoolSwaps(self, id, size=30, next=None):  # 03
        return self._ocean._conn.get(f"poolpairs/{id}/swaps", size=size, next=next)

    def listPoolSwapsVerbose(self, id, size=10, next=None):  # 04
        return self._ocean._conn.get(f"poolpairs/{id}/swaps/verbose", size=size, next=next)

    def listPoolSwapAggregates(self, id, interval,  size=30, next=None):  # 05
        return self._ocean._conn.get(f"poolpairs/{id}/swaps/aggregate/{interval}", size=size, next=next)

    def getSwappableTokens(self, tokenId):  # 06
        return self._ocean._conn.get(f"poolpairs/paths/swappable/{tokenId}")

    def getBestPath(self, fromTokenId, toTokenId):  # 07
        return self._ocean._conn.get(f"poolpairs/paths/best/from/{fromTokenId}/to/{toTokenId}")

    def getAllPaths(self, fromTokenId, toTokenId):  # 08
        return self._ocean._conn.get(f"poolpairs/paths/from/{fromTokenId}/to/{toTokenId}")

