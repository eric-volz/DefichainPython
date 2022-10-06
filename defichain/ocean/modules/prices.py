#  https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Prices.ts

class Prices:
    def __init__(self, ocean):
        self._ocean = ocean

    def list(self, size: int = 30, next: str = None) -> [{}]:  # 01
        """
        Get a list of PriceTicker

        :param size: (optional) for the number of records per page
        :type size: int
        :param next: (optional) offset for the next page
        :type next: str
        :return: (json string) {id: str, sort: str, price: PriceFeed}

        :example:

        >>> ocean.prices.list()
        """
        return self._ocean._conn.get("prices", size=size, next=next)

    def get(self, token: str, currency: str) -> {}:  # 02
        """
        Get a PriceTicker

        :param token: (required) token symbol for the PriceTicker
        :type token: str
        :param currency: (required) currency fiat currency for the PriceTicker
        :type currency: str
        :return: (json string) {id: str, sort: str, price: PriceFeed}

        :example:

        >>> ocean.prices.get("DFI", "USD")
        """
        key = f"{token}-{currency}"
        return self._ocean._conn.get(f"prices/{key}")

    def getFeedActive(self, token: str, currency: str, size: int = 30, next: str = None) -> [{}]:  # 03
        """
        Get active price feed

        :param token: (required) token symbol for the PriceTicker
        :type token: str
        :param currency: (required) currency fiat currency for the PriceTicker
        :type currency: str
        :param size: (optional) for the number of feeds per page
        :type size: int
        :param next: (optional) offset for the next page
        :type next: str
        :return: (json string) {id: str, key: str, sort: str, active: {amount: str, weightage: int,
            oracles: {active: int, total: int}}, next: {amount: str, weightage: int,
            oracles: {active: int, total: int}}, isLive: bool, block: {hash: str, height: int,
            time: int, medianTime: int}}

        :example:

        >>> ocean.prices.getFeedActive("DFI", "USD")
        """
        key = f"{token}-{currency}"
        return self._ocean._conn.get(f"prices/{key}/feed/active", size=size, next=next)

    def getFeed(self, token: str, currency: str, size: int = 30, next: str = None) -> [{}]:  # 04
        """
        Get a list of price feed

        :param token: (required) token symbol for the PriceTicker
        :type token: str
        :param currency: (required) currency fiat for the PriceTicker
        :type currency: str
        :param size: (optional) for number of records per page
        :type size: int
        :param next: (optional) offset for the next page
        :type next: str
        :return: (json string) {id: str, key: str, sort: str, active: {amount: str, weightage: int,
            oracles: {active: int, total: int}}, next?: {amount: str, weightage: int,
            oracles: {active: int, total: int}}, isLive: bool, block: {hash: str, height: int,
            time: int, medianTime: int}}

        :example:

        >>> ocean.prices.getFeed("DFI", "USD")
        """
        key = f"{token}-{currency}"
        return self._ocean._conn.get(f"prices/{key}/feed", size=size, next=next)

    def getFeedWithInterval(self, token: str, currency: str, interval: int, size: int = 30, next: str = None) -> [{}]:  # 05
        """
        Get a list of price feed wit interval

        :param token: (required) token symbol for the PriceTicker
        :type token: str
        :param currency: (required) currency fiat for the PriceTicker
        :type currency: str
        :param interval: (required) Time interval for graphing: 15 * 60, 60 * 60, 24 * 60 * 60
        :type interval: int
        :param size: (optional) for number of records per page
        :type size: int
        :param next: (optional) offset for the next page
        :type next: str
        :return: (json string) {id: str, key: str, sort: str, token: str, currency: str,
            aggregated: {amount: str, weightage: int, count: int, oracles: {active: int, total: int},
            time: {interval: int, start: int, end: int}}, block: hash: str, height: int, time: int,
            medianTime: int}}

        :example:

        >>> ocean.prices.getFeedWithInterval("DFI", "USD", 900)
        """
        key = f"{token}-{currency}"
        return self._ocean._conn.get(f"prices/{key}/feed/interval/{interval}", size=size, next=next)

    def getOracles(self, token: str, currency: str, size: int = 30, next: str = None) -> [{}]:  # 06
        """

        :param token: (required) token symbol for the PriceOracle
        :type token: str
        :param currency: (required) currency fiat currency for the PriceOracle
        :type currency: str
        :param size: (optional) for number of records per page
        :type size: int
        :param next: (optional) offset for the next page
        :type next: str
        :return: (json string) {id: str, key: str, token: str, currency: str, oracleId: str, weightage: int,
            feed: OraclePriceFeed, block: {hash: str, height: int, time: int, medianTime: int}}

        :example:

        >>> ocean.prices.getOracles("DFI", "USD")
        """
        key = f"{token}-{currency}"
        return self._ocean._conn.get(f"prices/{key}/oracles", size=size, next=next)
