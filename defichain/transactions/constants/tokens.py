import json
import os
from defichain import Ocean

ocean = Ocean()


class TokenTypes:
    STANDARD = "STANDARD"
    LIQUIDITY = "LIQUIDITY"
    LOAN = "LOAN"
    CUSTOM = "CUSTOM"


class Tokens:
    PATH = os.path.join(os.path.dirname(__file__))

    @staticmethod
    def get_standardTokens() -> [{}]:
        with open(Tokens.PATH + f"/{TokenTypes.STANDARD}_tokens.json", "r") as f:
            return json.loads(f.read())

    @staticmethod
    def get_liquidityTokens() -> [{}]:
        with open(Tokens.PATH + f"/{TokenTypes.LIQUIDITY}_tokens.json", "r") as f:
            return json.loads(f.read())

    @staticmethod
    def get_loanTokens() -> [{}]:
        with open(Tokens.PATH + f"/{TokenTypes.LOAN}_tokens.json", "r") as f:
            return json.loads(f.read())

    @staticmethod
    def get_customTokens() -> [{}]:
        with open(Tokens.PATH + f"/{TokenTypes.CUSTOM}_tokens.json", "r") as f:
            return json.loads(f.read())

    @staticmethod
    def _build_tokenJson() -> None:
        """
        Asks the ocean API for the newest tokens and prints the results in json files into the current folder
        """

        standard_tokens = []
        liquidity_tokens = []
        loan_tokens = []
        custom_token = []

        i = -1
        tokens = True
        while tokens:
            tokens = ocean.tokens.list(size=200, next=i)["data"]
            for token in tokens:
                token = {"id": token["id"], "symbol": token["symbol"], "name": token["name"], "isDAT": token["isDAT"],
                         "isLPS": token["isLPS"], "isLoanToken": token["isLoanToken"]}
                if token["isDAT"] and not token["isLPS"]:
                    standard_tokens.append(token)
                if token["isDAT"] and token["isLPS"]:
                    liquidity_tokens.append(token)
                if token["isDAT"] and token["isLoanToken"]:
                    loan_tokens.append(token)
                if not token["isDAT"] and not token["isLPS"]:
                    custom_token.append(token)
            i += len(tokens)

        with open(f"{TokenTypes.STANDARD}_tokens.json", "w") as f:
            f.write(json.dumps(standard_tokens))
        with open(f"{TokenTypes.LIQUIDITY}_tokens.json", "w") as f:
            f.write(json.dumps(liquidity_tokens))
        with open(f"{TokenTypes.LOAN}_tokens.json", "w") as f:
            f.write(json.dumps(loan_tokens))
        with open(f"{TokenTypes.CUSTOM}_tokens.json", "w") as f:
            f.write(json.dumps(custom_token))


if __name__ == "__main__":
    Tokens._build_tokenJson()
