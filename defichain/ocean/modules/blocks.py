# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Blocks.ts

class Blocks:
    def __init__(self, ocean):
        self._ocean = ocean

    def list(self, size=30, next=None):  # 01
        return self._ocean._conn.get("blocks", size=size, next=next)

    def get(self, id):  # 02
        return self._ocean._conn.get(f"blocks/{id}")

    def getTransactions(self, hash, size=30, next=None):  # 03
        return self._ocean._conn.get(f"blocks/{hash}/transactions", size=size, next=next)
