from defichain import Ocean
from defichain.networks import DefichainMainnet, DefichainTestnet
from defichain.exceptions.transactions import TokenError
from defichain.transactions.constants.tokens import Tokens, TokenTypes

ocean = Ocean()


class Token:

    @staticmethod
    def _get_tokens(network: DefichainMainnet or DefichainTestnet, TYPE: str) -> [{}]:
        if TYPE == TokenTypes.STANDARD:
            return Tokens.get_standardTokens(network)
        elif TYPE == TokenTypes.LIQUIDITY:
            return Tokens.get_liquidityTokens(network)
        elif TYPE == TokenTypes.LOAN:
            return Tokens.get_loanTokens(network)
        elif TYPE == TokenTypes.CUSTOM:
            return Tokens.get_customTokens(network)
        else:
            raise TokenError("The given tokens type is not valid.\n"
                             "Use the token types in defichain.transaction.constance.tokens.")

    @staticmethod
    def get_symbol_from_id(network: DefichainMainnet or DefichainTestnet, tokenId: int, TYPE: str) -> str:
        tokens = Token._get_tokens(network, TYPE)
        for token in tokens:
            if token["id"] == str(tokenId):
                return token["symbol"]
        raise TokenError(f"The given id: {tokenId} does not exist. Check your token id input.")

    @staticmethod
    def get_id_from_symbol(network: DefichainMainnet or DefichainTestnet, symbol: str, TYPE: str) -> int:
        tokens = Token._get_tokens(network, TYPE)
        for token in tokens:
            if token["symbol"] == str(symbol):
                return token["id"]
        raise TokenError(f"The given symbol: {symbol} does not exist. Check your input.")

    @staticmethod
    def get_name_from_id(network: DefichainMainnet or DefichainTestnet, tokenId: int, TYPE: str) -> str:
        tokens = Token._get_tokens(network, TYPE)
        for token in tokens:
            if token["id"] == str(tokenId):
                return token["name"]
        raise TokenError(f"The given id: {tokenId} does not exist. Check your token id input.")

    @staticmethod
    def verify_tokenId(network: DefichainMainnet or DefichainTestnet, tokenId: int) -> bool:
        tokenTypes = [TokenTypes.STANDARD, TokenTypes.LOAN, TokenTypes.LIQUIDITY, TokenTypes.CUSTOM]
        for _type in tokenTypes:
            try:
                Token.get_name_from_id(network, tokenId, _type)
                return True
            except:
                pass
        raise TokenError("The given token id is not valid")
