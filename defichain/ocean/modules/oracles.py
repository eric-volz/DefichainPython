#  https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Prices.ts

class Oracles:
    def __init__(self, ocean):
        self._ocean = ocean

    def list(self, size: int = 30, next: str = None) -> {}:  # 01
        """
        Get a list of Oracles

        :param size: (optional) for number of records per page
        :type size: int
        :param next: (optional) offset for the next page
        :type next: str
        :return: (json string) {id: str, weightage: int, ownerAddress: str, priceFeeds: [{token: str, currency: str}],
            block: {hash: str, height: int, time: int, medianTime: int}}

        :example:

        >>> ocean.oracles.list()
        """
        return self._ocean._conn.get("oracles", size=size, next=next)

    def getPriceFeed(self, oracleId: str, token: str, currency: str, size: int = 30, next: str = None) -> {}:  # 02
        """
        Get price feed

        :param oracleId: (required) oracleId identifier for an Oracle
        :type oracleId: str
        :param token: (required) token symbol as part of the price feed pair
        :type token: str
        :param currency: (required) currency fiat currency part of the price feed pair
        :type currency: str
        :param size: (optional) for number of records per page
        :type size: int
        :param next: (optional) offset for the next page
        :type next: str
        :return: (json string) {id: str, key: str, sort: str, token: str, currency: str, oracleId: str,
            txid: str, time: int, amount: str, block: {hash: str, height: int, time: int,
            medianTime: int}}

        :example:

        >>> ocean.oracles.getPriceFeed('f95b8a0ef321bcd310a9cc57b90d74fa4423895448678fbf8487807a125a08ef', "GOLD", "USD")
        """
        key = f"{token}-{currency}"
        return self._ocean._conn.get(f"oracles/{oracleId}/{key}/feed", size=size, next=next)

    def getOracleByAddress(self, address: str) -> {}:  # 03
        """
        Get oracle by address

        :param address: (required) address owner address for an Oracle
        :type address: str
        :return: (json string) {id: str, weightage: int, ownerAddress: str, priceFeeds: [{token: str, currency: str}],
            block: {hash: str, height: int, time: int, medianTime: int}}

        :example:

        >>> ocean.oracles.getOracleByAddress("df1q8cz47rwefsxme29sstumepw374gzeu025gqcy4")
        """
        return self._ocean._conn.get(f"oracles/{address}")
