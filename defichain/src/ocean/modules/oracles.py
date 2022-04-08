#  https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Prices.ts

class Oracles:
    def __init__(self, ocean):
        self.ocean = ocean

    def list(self, size=None, next=None) -> str:
        """
        Get a list of OceanOracles
        @param size: how many oracles
        @param next: next page hash
        @return: json
        """
        size = 30 if size is None else size
        next = "" if next is None else f"&next={next}"
        addOn = f"?size={size}{next}"
        request = f"oracles{addOn}"
        return self.ocean.con.request(request)

    def getPriceFeed(self, oracleId: str, token: str, currency: str, size=None, next=None) -> str:
        """
        Get Price Feed for each Oracle by Price Ticker.
        @param oracleId: oracle id found through list() function
        @param token: ticker token like APPL
        @param currency: currency like USD
        @param size: ow many oracle feeds
        @param next: next page hash
        @return:
        """
        size = 30 if size is None else size
        next = "" if next is None else f"&next={next}"
        addOn = f"?size={size}{next}"
        request = f"oracles/{oracleId}/{token}-{currency}/feed{addOn}"
        return self.ocean.con.request(request)
