# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Transactions.ts

class Transactions:
    def __init__(self, ocean):
        self._ocean = ocean

    def get(self, id):
        return self._ocean._conn.get(f"transactions/{id}")

    def getVins(self, txid, size=30, next=None):
        return self._ocean._conn.get(f"transactions/{txid}/vins", size=size, next=next)

    def getVouts(self, txid, size=30, next=None):
        return self._ocean._conn.get(f"transactions/{txid}/vouts", size=size, next=next)
