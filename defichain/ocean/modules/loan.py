# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Loan.ts

class Loan:
    def __init__(self, ocean):
        self._ocean = ocean

    def listScheme(self, size: int = 30, next: str = None) -> [{}]:  # 01
        """
        Paginate query loan schemes

        :param size: (optional) size of scheme to query
        :type size: int
        :param next: (optional) next set of schemes
        :type next: str
        :return: (json string) {id: str, minColRatio: str, interestRate: str}

        :example:

        >>> ocean.loan.listScheme()
        """
        return self._ocean._conn.get(f"loans/schemes", size=size, next=next)

    def getScheme(self, id: str) -> {}:  # 02
        """
        Get information about a scheme with given scheme id

        :param id: (required) id of scheme to get
        :type id: str
        :return: (json string) {id: str, minColRatio: str, interestRate: str}

        :example:

        >>> ocean.loan.getScheme("MIN150")
        """
        return self._ocean._conn.get(f"loans/schemes/{id}")

    def listCollateralToken(self, size: int = 30, next: str = None) -> [{}]:  # 03
        """
        Paginate query loan collateral tokens

        :param size: (optional) size of collateral tokens to query
        :type size: int
        :param next: (optional) next set of collateral tokens
        :type next: str
        :return: (json string) {tokenId: str, token: TokenData, factor: str, activateAfterBlock: int,
            fixedIntervalPriceId: str, activePrice: ActivePrice}

        :example:

        >>> ocean.loan.listCollateralToken()
        """
        return self._ocean._conn.get(f"loans/collaterals", size=size, next=next)

    def getCollateralToken(self, id: str) -> {}:  # 04
        """
        Get information about a collateral token with given collateral token id

        :param id: (required) id of collateral token to get
        :type id: str
        :return: (json string) {tokenId: str, token: TokenData, factor: str, activateAfterBlock: int,
            fixedIntervalPriceId: str, activePrice: ActivePrice}

        :example:

        >>> ocean.loan.getCollateralToken()
        """
        return self._ocean._conn.get(f"loans/collaterals/{id}")

    def listLoanToken(self, size: int = 30, next: str = None) -> [{}]:  # 05
        """
        Paginate query loan tokens

        :param size: (optional) size of loan token to query
        :type size: int
        :param next: (optional) next set of loan tokens
        :type next: str
        :return: (json string) {tokenId: str, token: TokenData, interest: str, fixedIntervalPriceId: str,
            activePrice: ActivePrice}

        :example:

        >>> ocean.loan.listLoanToken()
        """
        return self._ocean._conn.get(f"loans/tokens", size=size, next=next)

    def getLoanToken(self, id: str) -> {}:  # 06
        """
        Get information about a loan token with given loan token id

        :param id: (required) id of loanToken to get
        :type id: str
        :return: (json string) {tokenId: str, token: TokenData, interest: str, fixedIntervalPriceId: str,
            activePrice: ActivePrice}

        :example:

        >>> ocean.loan.getLoanToken("0")
        """
        return self._ocean._conn.get(f"loans/tokens/{id}")

    def listVault(self, size: int = 30, next: str = None) -> [{}]:  # 07
        """
        Paginate query loan vaults

        :param size: (optional) size of vaults to query
        :type size: int
        :param next: (optional) next set of vaults
        :type next: str
        :return: (json string) VaultActive or VaultLiquidated

        :example:

        >>> ocean.loan.listVault()
        """
        return self._ocean._conn.get("loans/vaults", size=size, next=next)

    def getVault(self, id: str) -> {}:  # 08
        """
        Get information about a vault with given vault id

        :param id: (required) id of vault to get
        :type id: str
        :return: (json string) VaultActive or VaultLiquidated

        :example:

        >>> ocean.loan.getVault("8f87baa094aa166cf88dd61553ad996ea2c1f7694536c18f3d8390e436900300")
        """
        return self._ocean._conn.get(f"loans/vaults/{id}")

    def listVaultAuctionHistory(self, id: str, height: int, batchIndex: int, size: int = 30, next: str = None) -> [{}]:  # 09
        """
        List vault auction history

        :param id: (required) vaultId
        :type id: str
        :param height: (required) liquidation height
        :type height: int
        :param batchIndex: (required) batch index
        :type batchIndex: int
        :param size: (optional) size of auction batch index history
        :type size: int
        :param next: (optional) next set of auction batch index history
        :type next: str
        :return: (json string) {id: string, key: string, sort: string, vaultId: string, index: number, from: string,
            address: string, amount: string, tokenId: number, block: {hash: string, height: number, time: number,
            medianTime: number}}

        :example:

        >>> ocean.loan.listVaultAuctionHistory("866889122ba23be0a71fc6a9e853d6b8f2b42b018393f091922be5ebcc23b600", 0, 0)
        """
        return self._ocean._conn.get(f"loans/vaults/{id}/auctions/{height}/batches/{batchIndex}/history", size=size,
                                     next=next)

    def listAuction(self, size: int = 30, next: str = None) -> [{}]:  # 10
        """
        Paginate query loan auctions

        :param size: (optional) size of auctions to query
        :type size: int
        :param next: (optional) next set of auctions
        :type next: str
        :return: (json string) {vaultId: string, loanScheme: LoanScheme, ownerAddress: string,
            state: LoanVaultState.IN_LIQUIDATION, liquidationHeight: number, liquidationPenalty: number,
            batchCount: number, batches: LoanVaultLiquidationBatch[]}

        :example:

        >>> ocean.loan.listAuction()
        """
        return self._ocean._conn.get(f"loans/auctions", size=size, next=next)
