#  https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Prices.ts

class Prices:
    def __init__(self, ocean):
        self._ocean = ocean

    def list(self, size=30, next=None):  # 01
        return self._ocean._conn.get("prices", size=size, next=next)

    def get(self, token, currency):  # 02
        key = f"{token}-{currency}"
        return self._ocean._conn.get(f"prices/{key}")

    def getFeedActive(self, token, currency, size=30, next=None):  # 03
        key = f"{token}-{currency}"
        return self._ocean._conn.get(f"prices/{key}/feed/active", size=size, next=next)

    def getFeed(self, token, currency, size=30, next=None):  # 04
        key = f"{token}-{currency}"
        return self._ocean._conn.get(f"prices/{key}/feed", size=size, next=next)

    def getFeedWithInterval(self, token, currency, interval, size=30, next=None):  # 05
        key = f"{token}-{currency}"
        return self._ocean._conn.get(f"prices/{key}/feed/interval/{interval}", size=size, next=next)

    def getOracles(self, token, currency, size=30, next=None):  # 06
        key = f"{token}-{currency}"
        return self._ocean._conn.get(f"prices/{key}/oracles", size=size, next=next)
