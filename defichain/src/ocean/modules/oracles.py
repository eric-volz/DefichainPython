#  https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Prices.ts

class Oracles:
    def __init__(self, ocean):
        self.ocean = ocean

    def list(self, size=30, next=None):  # 01
        return self.ocean._conn.get("oracles", size=size, next=next)

    def getPriceFeed(self, oracleId, token, currency, size=30, next=None):  # 02
        key = f"{token}-{currency}"
        return self.ocean._conn.get(f"oracles/{oracleId}/{key}/feed", size=size, next=next)

    def getOracleByAddress(self, address):  # 03
        return self.ocean._conn.get(f"oracles/{address}")
