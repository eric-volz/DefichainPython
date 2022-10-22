# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/PoolPairs.ts

class Poolpairs:
    def __init__(self, ocean):
        self._ocean = ocean

    def list(self, size: int = 30, next: str = None) -> [{}]:  # 01
        """
        List pool pairs

        :param size: (optional) size of PoolPairData balance to query
        :type size: int
        :param next: (optional) next set of PoolPairData
        :type next: str
        :return: (json string) {id: str, symbol: str, displaySymbol: str, name: str, status: bool,
            tokenA: {id: str, name: str, symbol: str, displaySymbol: str, reserve: str,
            blockCommission: str, fee: {pct: str, inPct: str, outPct: str}}, tokenB: {id: str,
            name: str, symbol: str, displaySymbol: str, reserve: str, blockCommission: str,
            fee: {pct: str, inPct: str, outPct: str}}, priceRatio: {ab: str, ba: str},
            commission: str, totalLiquidity: {token: str, usd: str}, tradeEnabled: bool,
            ownerAddress: str, rewardPct: str, rewardLoanPct: str, customRewards: str[],
            creation: {tx: str, height: int}, apr: {total: float, reward: float, commission: float},
            volume?: {d30: float, h24: float}}

        :example:

        >>> ocean.poolpairs.list()
        """
        return self._ocean._conn.get(f"poolpairs", size=size, next=next)

    def get(self, id: str) -> {}:  # 02
        """
        Get pool pair

        :param id: (required) id of the pool pair
        :type id: str
        :return: (json string) {id: str, symbol: str, displaySymbol: str, name: str, status: bool,
            tokenA: {id: str, name: str, symbol: str, displaySymbol: str, reserve: str,
            blockCommission: str, fee: {pct: str, inPct: str, outPct: str}}, tokenB: {id: str,
            name: str, symbol: str, displaySymbol: str, reserve: str, blockCommission: str,
            fee: {pct: str, inPct: str, outPct: str}}, priceRatio: {ab: str, ba: str},
            commission: str, totalLiquidity: {token: str, usd: str}, tradeEnabled: bool,
            ownerAddress: str, rewardPct: str, rewardLoanPct: str, customRewards: str[],
            creation: {tx: str, height: int}, apr: {total: float, reward: float, commission: float},
            volume?: {d30: float, h24: float}}

        :example:

        >>> ocean.poolpairs.get("4")
        """
        return self._ocean._conn.get(f"poolpairs/{id}")

    def listPoolSwaps(self, id: str, size: int = 30, next: str = None) -> [{}]:  # 03
        """
        List pool swaps

        :param id: (required) id of the pool pair
        :type id: str
        :param size: (optional) size of PoolSwap to query
        :type size: int
        :param next: (optional) next set of PoolSwap
        :type next: str
        :return: (json string) {id: str, sort: str, txid: str, txno: int, poolPairId: str, fromAmount: str,
            fromTokenId: int, from: PoolSwapFromToData, to: PoolSwapFromToData, type: SwapType,
            block: {hash: str, height: int, time: int, medianTime: int}}

        :example:

        >>> ocean.poolpairs.listPoolSwaps("4")
        """
        return self._ocean._conn.get(f"poolpairs/{id}/swaps", size=size, next=next)

    def listPoolSwapsVerbose(self, id: str, size: int = 10, next: str = None) -> [{}]:  # 04
        """
        List pool swaps with from/to

        :param id: (required) id of the pool pair
        :type id: str
        :param size: (optional) of PoolSwap to query, max of 20 per page
        :type size: int
        :param next: (optional) next set of PoolSwap
        :type next: str
        :return: (json string) {id: str, sort: str, txid: str, txno: int, poolPairId: str, fromAmount: str,
            fromTokenId: int, from: PoolSwapFromToData, to: PoolSwapFromToData, type: SwapType,
            block: {hash: str, height: int, time: int, medianTime: int}}

        :example:

        >>> ocean.poolpairs.listPoolSwapsVerbose("4")
        """
        return self._ocean._conn.get(f"poolpairs/{id}/swaps/verbose", size=size, next=next)

    def listPoolSwapAggregates(self, id: str, interval: int,  size: int = 30, next: str = None) -> [{}]:  # 05
        """
        List pool swap aggregates

        :param id: (required) id of the pool pair
        :type id: str
        :param interval: (required) aggregated interval: 60 * 60, 60 * 60 * 24
        :type interval: int
        :param size: (optional) size of PoolSwap to query
        :type size: str
        :param next: (optional) next set of PoolSwap
        :type next: int
        :return: (json string) {id: str, key: str, bucket: int, aggregated: {amounts: Record<str, str>, usd: float},
            block: {medianTime: int}}

        :example:

        >>> ocean.poolpairs.listPoolSwapsVerbose("4", 3600)
        """
        return self._ocean._conn.get(f"poolpairs/{id}/swaps/aggregate/{interval}", size=size, next=next)

    def getSwappableTokens(self, tokenId: str) -> {}:  # 06
        """
        Get all swappable tokens for a given token

        :param tokenId: (required) id of  a token
        :type tokenId: str
        :return: (json string) {fromToken: TokenIdentifier, swappableTokens: TokenIdentifier[]}

        :example:

        >>> ocean.poolpairs.getSwappableTokens("0")
        """
        return self._ocean._conn.get(f"poolpairs/paths/swappable/{tokenId}")

    def getBestPath(self, fromTokenId: str, toTokenId: str) -> {}:  # 07
        """
        Get the best (estimated) swap path from one token to another

        :param fromTokenId: (required) tokenId to swap from
        :type fromTokenId: str
        :param toTokenId: (required) tokenId to swap to
        :type toTokenId: str
        :return: (json string) {fromToken: TokenIdentifier, toToken: TokenIdentifier, bestPath: SwapPathPoolPair[],
            estimatedReturn: str, estimatedReturnLessDexFees: str}

        :example:

        >>> ocean.poolpairs.getBestPath("0", "75")
        """
        return self._ocean._conn.get(f"poolpairs/paths/best/from/{fromTokenId}/to/{toTokenId}")

    def getAllPaths(self, fromTokenId: str, toTokenId: str) -> {}:  # 08
        """
        Get all possible swap paths from one token to another

        :param fromTokenId: (required) tokenId to swap from
        :type fromTokenId: str
        :param toTokenId: (required) tokenId to swap to
        :type toTokenId: str
        :return: (json string) {fromToken: TokenIdentifier, toToken: TokenIdentifier, bestPath: SwapPathPoolPair[],
            estimatedReturn: str, estimatedReturnLessDexFees: str}

        :example:

        >>> ocean.poolpairs.getAllPaths("0", "75")
        """
        return self._ocean._conn.get(f"poolpairs/paths/from/{fromTokenId}/to/{toTokenId}")

    def listDexPrices(self, denomination: str) -> {}:
        """
        Get all dex prices denominated in a given token

        :param denomination: (required) denomination
        :type denomination: str
        :return: (json string) {token: TokenIdentifier, denominationPrice: str}

        :example:

        >>> ocean.poolpairs.listDexPrices("DUSD")
        """
        return self._ocean._conn.get(f"poolpairs/dexprices?denomination={denomination}")
