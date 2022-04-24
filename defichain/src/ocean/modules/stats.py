# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Stats.ts

class Stats:
    def __init__(self, ocean):
        self._ocean = ocean

    def get(self):
        return self._ocean._conn.get("stats")

    def getSupply(self):
        return self._ocean._conn.get("stats/supply")

    def getBurn(self):
        return self._ocean._conn.get("stats/burn")
