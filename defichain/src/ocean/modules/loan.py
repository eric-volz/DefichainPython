# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Loan.ts

class Loan:
    def __init__(self, ocean):
        self._ocean = ocean

    def listScheme(self, size=30, next=None):  # 01
        return self._ocean._conn.get(f"loans/schemes", size=size, next=next)

    def getScheme(self, id):  # 02
        return self._ocean._conn.get(f"loans/schemes/{id}")

    def listCollateralToken(self, size=30, next=None):  # 03
        return self._ocean._conn.get(f"loans/collaterals", size=size, next=next)

    def getCollateralToken(self, id):  # 04
        return self._ocean._conn.get(f"loans/collaterals/{id}")

    def listLoanToken(self, size=30, next=None):  # 05
        return self._ocean._conn.get(f"loans/tokens", size=size, next=next)

    def getLoanToken(self, id):  # 06
        return self._ocean._conn.get(f"loans/tokens/{id}")

    def listVault(self, size=30, next=None):  # 07
        return self._ocean._conn.get("loans/vaults", size=size, next=next)

    def getVault(self, id):  # 08
        return self._ocean._conn.get(f"loans/vaults/{id}")

    def listVaultAuctionHistory(self, id, height, batchIndex, size=30, next=None):  # 09
        return self._ocean._conn.get(f"loans/vaults/{id}/auctions/{height}/batches/{batchIndex}/history", size=size,
                                     next=next)

    def listAuction(self, size=30, next=None):  # 10
        return self._ocean._conn.get(f"loans/auctions", size=size, next=next)
