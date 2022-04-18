#  https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Prices.ts

class Oracles:
    def __init__(self, ocean):
        self.ocean = ocean

    def list(self, size=30, next=None):
        return self.ocean._conn.call("oracles", size=size, next=next)

    def getPriceFeed(self, oracleId, token, currency, size=30, next=None):
        key = f"{token}-{currency}"
        return self.ocean._conn.call(f"oracles/{oracleId}/{key}/feed", size=size, next=next)

    def getOracleByAddress(self, address):
        return self.ocean._conn.call(f"oracles/{address}")
