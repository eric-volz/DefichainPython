import json
from defichain import Ocean
from defichain.transactions.constants.tokens import Tokens, TokenTypes
from defichain.exceptions.transactions import TokenError

ocean = Ocean()


class Token:

    @staticmethod
    def _get_tokens(TYPE: str) -> [{}]:
        if TYPE == TokenTypes.STANDARD:
            return Tokens.get_standardTokens()
        elif TYPE == TokenTypes.LIQUIDITY:
            return Tokens.get_liquidityTokens()
        elif TYPE == TokenTypes.LOAN:
            return Tokens.get_loanTokens()
        elif TYPE == TokenTypes.CUSTOM:
            return Tokens.get_customTokens()
        else:
            raise TokenError("The given tokens type is not valid.\n"
                             "Use the token types in defichain.transaction.constance.tokens.")

    @staticmethod
    def get_symbol_from_id(id: int, TYPE: str) -> str:
        tokens = Token._get_tokens(TYPE)
        for token in tokens:
            if token["id"] == str(id):
                return token["symbol"]
        raise TokenError(f"The given id: {id} does not exist. Check your token id input.")

    @staticmethod
    def get_id_from_symbol(symbol: str, TYPE: str) -> int:
        tokens = Token._get_tokens(TYPE)
        for token in tokens:
            if token["symbol"] == str(symbol):
                return token["id"]
        raise TokenError(f"The given symbol: {symbol} does not exist. Check your input.")

    @staticmethod
    def get_name_from_id(id: int, TYPE: str) -> str:
        tokens = Token._get_tokens(TYPE)
        for token in tokens:
            if token["id"] == str(id):
                return token["name"]
        raise TokenError(f"The given id: {id} does not exist. Check your token id input.")

    @staticmethod
    def verify_tokenId(tokenId: int) -> bool:
        tokenTypes = [TokenTypes.STANDARD, TokenTypes.LOAN, TokenTypes.LIQUIDITY, TokenTypes.CUSTOM]
        for _type in tokenTypes:
            try:
                Token.get_name_from_id(tokenId, _type)
                return True
            except:
                pass
        raise TokenError("The given token id is not valid")
