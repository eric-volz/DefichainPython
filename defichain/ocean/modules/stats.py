# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Stats.ts

class Stats:
    def __init__(self, ocean):
        self._ocean = ocean

    def get(self) -> {}:  # 01
        """
        Get stats of DeFi Blockchain

        :return: (json string) {count: {blocks: int, tokens: int, prices: int, masternodes: int}, tvl: {total: float,
            dex: float, loan: float, masternodes: float}, burned: {total: float, address: float, fee: int,
            auction: float, payback: float, emission: float}, price: {usd: float, usdt: float},
            masternodes: {locked: [{ weeks: int, tvl: float, count: int}]}, emission: {total: float,
            masternode: float, dex: float, community: float, anchor: float, burned: float},
            loan: {count: {schemes: int, loanTokens: int, collateralTokens: int, openVaults: int,
            openAuctions: int}, value: {collateral: float, loan: float}}, blockchain: {difficulty: float},
            net: {version: int, subversion: str, protocolversion: int}}

        :example:

        >>> ocean.stats.get()
        """
        return self._ocean._conn.get("stats")

    def getRewardDistribution(self) -> {}:
        """
        Get reward distribution of DeFi Blockchain

        :return: (json string) {masternode: int, community: int, anchor: int, liquidity: int, loan: int, options: int, unallocated: int}

        :example:

        >>> ocean.stats.getRewardDistribution()
        """
        return self._ocean._conn.get("stats/rewards/distribution")

    def getSupply(self) -> {}:  # 02
        """
        Get supply of DeFi Blockchain

        :return: (json string) {max: float, total: float, burned: float, circulating: float}

        :example:

        >>> ocean.stats.getSupply()
        """
        return self._ocean._conn.get("stats/supply")

    def getBurn(self) -> {}:  # 03
        """
        Get burn info of DeFi Blockchain

        :return: (json string) {address: str, amount: str, tokens: str[], feeburn: float, emissionburn: float,
            auctionburn: float, paybackburn: float, paybackburntokens: str[], dexfeetokens: str[],
            dfipaybackfee: float, dfipaybacktokens: str[], paybackfees: str[], paybacktokens: str[],
            dfip2203: str[], dfip2206f: str[]}

        :example:

        >>> ocean.stats.getBurn()
        """
        return self._ocean._conn.get("stats/burn")
