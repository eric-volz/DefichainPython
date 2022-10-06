# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Tokens.ts

class Tokens:
    def __init__(self, ocean):
        self._ocean = ocean

    def list(self, size: int = 30, next: str = None) -> [{}]:
        """
        Paginate query tokens

        :param size: (optional) size of tokens to query
        :type size: int
        :param next: (optional) next set of tokens
        :type next: str
        :return: (json string) {id: str, symbol: str, displaySymbol: str, symbolKey: str, name: str, decimal: float,
            limit: str, mintable: bool, tradeable: bool, isDAT: bool, isLPS: bool, isLoanToken: bool,
            finalized: bool, minted: str, creation: {tx: str, height: int}, destruction: {tx: str,
            height: int}, collateralAddress: str}

        :example:

        >>> ocean.tokens.list()
        """
        return self._ocean._conn.get("tokens", size=size, next=next)

    def get(self, id: str) -> {}:
        """
        Get information about a token with id of the token

        :param id: (required) id of the token
        :type id: str
        :return: (json string) {id: str, symbol: str, displaySymbol: str, symbolKey: str, name: str, decimal: float,
            limit: str, mintable: bool, tradeable: bool, isDAT: bool, isLPS: bool, isLoanToken: bool,
            finalized: bool, minted: str, creation: {tx: str, height: int}, destruction: {tx: str,
            height: int}, collateralAddress: str}

        :example:

        >>> ocean.tokens.get(0)
        """
        return self._ocean._conn.get(f"tokens/{id}")
