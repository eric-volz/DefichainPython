#  https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Prices.ts

class PoolPairs:
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
        request = f"poolpairs{addOn}"
        return self.ocean.con.request(request)
