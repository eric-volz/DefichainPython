#  https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Prices.ts

class Prices:
    def __init__(self, ocean):
        self.ocean = ocean

    def list(self, size=None, next=None) -> str:
        """
        Get a list of available Price Ticker.
        @param size: how many ticker
        @param next: next page hash
        @return: json
        """
        size = 30 if size is None else size
        next = "" if next is None else f"&next={next}"
        addOn = f"?size={size}{next}"
        request = f"prices{addOn}"
        return self.ocean.con.request(request)

    def get(self, token: str, currency: str) -> str:
        """
        Get a single Price Ticker.
        @param token: token like DFI
        @param currency: currency like USD
        @return: json
        """
        request = f"prices/{token}-{currency}"
        return self.ocean.con.request(request)

    def getFeed(self, token: str, currency: str, size=None, next=None) -> str:
        """
        Get a list of Price Feed by Price Ticker.
        @param token: token like DFI
        @param currency: currency like USD
        @param size: how many feeds
        @param next: next page hash
        @return: json
        """
        size = 30 if size is None else size
        next = "" if next is None else f"&next={next}"
        addOn = f"?size={size}{next}"
        request = f"prices/{token}-{currency}/feed{addOn}"
        return self.ocean.con.request(request)

    def getOracles(self, token: str, currency: str, size=None, next=None) -> str:
        """
        Get a list of OceanOracles by Price Ticker.
        @param token: token like DFI
        @param currency: currency like USD
        @param size: how many oracles
        @param next: next page hash
        @return: json
        """
        size = 30 if size is None else size
        next = "" if next is None else f"&next={next}"
        addOn = f"?size={size}{next}"
        request = f"prices/{token}-{currency}/oracles{addOn}"
        return self.ocean.con.request(request)
