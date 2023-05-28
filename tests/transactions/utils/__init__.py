from defichain.transactions.constants import Tokens
from defichain.networks import DefichainMainnet, DefichainTestnet


class TestCalculate:
    DHASH: str = "ea07687190f4a6a974710eaaac483fad6436deb73d6a9297c76cdb658054b2d4"
    INT: int = 65535
    VARINT: str = "82fe7f"
    COMPACT_SIZE: str = "fdffff"
    ADDRESS_AMOUNT: str = {'df1qsqa3yt6sfkx3nu5ch88ymlzwnwd5wkkstywjvu': ['232@DFI', '234@DFI'],
                          '8bXZh4A9NWW9weWW7nUpLJhAMmfLL6o5wo': '32432@DFI'}


class TestConverter:
    INT: int = 478560411976
    BYTES: bytes = b'Hallo'
    HEX: str = "48616c6c6f"
    STR: str = "Hallo"
    FLOAT: float = 4785.60411976
    AMOUNT_INT: str = "100000000@DFI"
    AMOUNT_FLOAT: str = "1@DFI"
    ADDRESS_AMOUNT_INT = {'df1qsqa3yt6sfkx3nu5ch88ymlzwnwd5wkkstywjvu': ['23543352@DFI', '254353434@DFI'],
                          '8bXZh4A9NWW9weWW7nUpLJhAMmfLL6o5wo': '32454355332@DFI'}
    ADDRESS_AMOUNT_FLOAT = {'df1qsqa3yt6sfkx3nu5ch88ymlzwnwd5wkkstywjvu': ['0.23543352@DFI', '2.54353434@DFI'],
                            '8bXZh4A9NWW9weWW7nUpLJhAMmfLL6o5wo': '324.54355332@DFI'}


class TestToken:
    MAINNET_STANDARD_TOKENS = Tokens.get_standardTokens(DefichainMainnet)
    MAINNET_LIQUIDITY_TOKENS = Tokens.get_liquidityTokens(DefichainMainnet)
    MAINNET_LOAN_TOKENS = Tokens.get_loanTokens(DefichainMainnet)
    MAINNET_CUSTOM_TOKENS = Tokens.get_customTokens(DefichainMainnet)
    MAINNET_IDs = []
    for tokens in (MAINNET_STANDARD_TOKENS, MAINNET_LIQUIDITY_TOKENS, MAINNET_LOAN_TOKENS, MAINNET_CUSTOM_TOKENS):
        for token in tokens:
            MAINNET_IDs.append(int(token.get("id")))
    MAINNET_SYMBOLS = []
    for tokens in (MAINNET_STANDARD_TOKENS, MAINNET_LIQUIDITY_TOKENS, MAINNET_LOAN_TOKENS, MAINNET_CUSTOM_TOKENS):
        for token in tokens:
            MAINNET_SYMBOLS.append(token.get("symbol"))

    TESTNET_STANDARD_TOKENS = Tokens.get_standardTokens(DefichainTestnet)
    TESTNET_LIQUIDITY_TOKENS = Tokens.get_liquidityTokens(DefichainTestnet)
    TESTNET_LOAN_TOKENS = Tokens.get_loanTokens(DefichainTestnet)
    TESTNET_CUSTOM_TOKENS = Tokens.get_customTokens(DefichainTestnet)
    TESTNET_IDs = []
    for tokens in (TESTNET_STANDARD_TOKENS, TESTNET_LIQUIDITY_TOKENS, TESTNET_LOAN_TOKENS, TESTNET_CUSTOM_TOKENS):
        for token in tokens:
            TESTNET_IDs.append(int(token.get("id")))
    TESTNET_SYMBOLS = []
    for tokens in (TESTNET_STANDARD_TOKENS, TESTNET_LIQUIDITY_TOKENS, TESTNET_LOAN_TOKENS, TESTNET_CUSTOM_TOKENS):
        for token in tokens:
            TESTNET_SYMBOLS.append(token.get("symbol"))

