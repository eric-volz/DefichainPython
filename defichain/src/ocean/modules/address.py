#  https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Address.ts

class Address:
    def __init__(self, ocean):
        self.ocean = ocean

    def getBalance(self, address: str) -> str:
        """
        Get current UTXO balance of an address.
        @param address: Defichain OceanAddress
        @return: Json
        """
        request = f"address/{address}/balance"
        return self.ocean.con.request(request)

    def getAggregation(self, address: str) -> str:
        """
        Get current aggregated stats of an address.
        @param address: Defichain OceanAddress
        @return: Json
        """
        request = f"address/{address}/aggregation"
        return self.ocean.con.request(request)

    def listToken(self, address: str) -> str:
        """
        List all tokens balance belonging to an address.
        @param address: Defichain OceanAddress
        @return: Json
        """
        request = f"address/{address}/tokens"
        return self.ocean.con.request(request)

    def listVault(self, address: str) -> str:
        """
        List all vaults belonging to an address.
        @param address: Defichain OceanAddress
        @return: Json
        """
        request = f"address/{address}/vaults"
        return self.ocean.con.request(request)

    def listTransaction(self, address: str, size=None, next=None) -> str:
        """
        List all transaction activity belonging to an address, sorted by block recency.
        @param address: Defichain OceanAddress
        @param size: how many transactions
        @param next: next page hash
        @return: json
        """
        size = 30 if size is None else size
        next = "" if next is None else f"&next={next}"
        addOn = f"?size={size}{next}"
        request = f"address/{address}/transactions{addOn}"
        return self.ocean.con.request(request)
