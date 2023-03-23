from typing import Any

from defichain import Ocean
from .verify import Verify
from defichain.exceptions.transactions import TokenError
from defichain.transactions.constants.tokens import Tokens, TokenTypes

ocean = Ocean()


class Token:
    TOKEN_TYPES = (TokenTypes.STANDARD, TokenTypes.LOAN, TokenTypes.LIQUIDITY, TokenTypes.CUSTOM)

    @staticmethod
    def _get_tokens(network: Any, TYPE: str) -> [{}]:
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
    def get_symbol_from_id(network: Any, tokenId: int) -> str:
        for _type in Token.TOKEN_TYPES:
            tokens = Token._get_tokens(network, _type)
            for token in tokens:
                if token["id"] == str(tokenId):
                    return token["symbol"]
        raise TokenError(f"The given id: {tokenId} does not exist. Check your token id input.")

    @staticmethod
    def get_id_from_symbol(network: Any, symbol: str) -> int:
        for _type in Token.TOKEN_TYPES:
            tokens = Token._get_tokens(network, _type)
            for token in tokens:
                if token["symbol"] == str(symbol):
                    return int(token["id"])
        raise TokenError(f"The given symbol: {symbol} does not exist. Check your input.")

    @staticmethod
    def get_name_from_id(network: Any, tokenId: int) -> str:
        for _type in Token.TOKEN_TYPES:
            tokens = Token._get_tokens(network, _type)
            for token in tokens:
                if token["id"] == str(tokenId):
                    return token["name"]
        raise TokenError(f"The given id: {tokenId} does not exist. Check your token id input.")

    @staticmethod
    def verify_tokenId(network: Any, tokenId: int) -> bool:
        try:
            Token.get_name_from_id(network, tokenId)
            return True
        except:
            raise TokenError("The given token id is not valid")

    @staticmethod
    def checkAndConvert(network: Any, tokenId: "int | str"):
        if isinstance(tokenId, str) and not Verify.is_only_number_str(tokenId):
            return int(Token.get_id_from_symbol(network, tokenId))
        else:
            Token.verify_tokenId(network, tokenId)
            return int(tokenId)
