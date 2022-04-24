#  https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Address.ts

class Address:
    def __init__(self, ocean):
        self._ocean = ocean

    def listAccountHistory(self, address, size=30, next=None):  # 01
        return self._ocean._conn.get(f"address/{address}/history", size=size, next=next)

    def getBalance(self, address):
        return self._ocean._conn.get(f"address/{address}/balance")  # 02

    def getAggregation(self, address):
        return self._ocean._conn.get(f"address/{address}/aggregation")  # 03

    def listToken(self, address, size=30, next=None):  # 04
        return self._ocean._conn.get(f"address/{address}/tokens", size=size, next=next)

    def listVault(self, address, size=30, next=None):  # 05
        return self._ocean._conn.get(f"address/{address}/vaults", size=size, next=next)

    def listTransaction(self, address, size=30, next=None):  # 06
        return self._ocean._conn.get(f"address/{address}/transactions", size=size, next=next)

    def listTransactionUnspent(self, address, size=30, next=None):  # 07
        return self._ocean._conn.get(f"address/{address}/transactions/unspent", size=size, next=next)
