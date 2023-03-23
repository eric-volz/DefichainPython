

# BaseDefiTx
DefiTx_SIGNATURE: str = "44665478"  # BaseDefiTx


# Defi Transaction Types
class DefiTxType:
    # Accounts
    OP_DEFI_TX_UTXOS_TO_ACCOUNT: str = "55"  # U
    OP_DEFI_TX_ACCOUNT_TO_UTXOS: str = "62"  # b
    OP_DEFI_TX_ACCOUNT_TO_ACCOUNT: str = "42"  # B
    OP_DEFI_TX_ANY_ACCOUNT_TO_ACCOUNT: str = "61"  # a
    OP_DEFI_TX_FUTURE_SWAP: str = "51"  # Q

    # Governance
    OP_DEFI_TX_SET_GOVERNANCE: str = "47"  # G
    OP_DEFI_TX_SET_GOVERNANCE_HEIGHT: str = "6a"  # j
    OP_DEFI_TX_CREATE_CFP: str = "7a"  # z
    OP_DEFI_TX_CREATE_VOC: str = "45"  # E
    OP_DEFI_TX_VOTE: str = "4f"  # O

    # Loans
    OP_DEFI_TX_SET_LOAN_SCHEME: str = "4c"  # L
    OP_DEFI_TX_DESTROY_LOAN_SCHEME: str = "44"  # D
    OP_DEFI_TX_SET_DEFAULT_LOAN_SCHEME: str = "64"  # d
    OP_DEFI_TX_SET_COLLATERAL_TOKEN: str = "63"  # c
    OP_DEFI_TX_SET_LOAN_TOKEN: str = "67"  # g
    OP_DEFI_TX_UPDATE_LOAN_TOKEN: str = "78"  # x
    OP_DEFI_TX_TAKE_LOAN: str = "58"  # X
    OP_DEFI_TX_PAYBACK_LOAN: str = "48"  # H
    OP_DEFI_TX_PAYBACK_LOAN_V2: str = "6B"  # k

    # Masternode
    OP_DEFI_TX_CREATE_MASTER_NODE: str = "43"  # C
    OP_DEFI_TX_RESIGN_MASTER_NODE: str = "52"  # R
    OP_DEFI_TX_UPDATE_MASTER_NODE: str = "6d"  # m

    # Misc
    OP_DEFI_TX_AUTO_AUTH_PREP: str = "41"  # A

    # Oracles
    OP_DEFI_TX_APPOINT_ORACLE: str = "6f"  # o
    OP_DEFI_TX_REMOVE_ORACLE: str = "68"  # h
    OP_DEFI_TX_UPDATE_ORACLE: str = "74"  # t
    OP_DEFI_TX_SET_ORACLE_DATA: str = "79"  # y

    # Pool
    OP_DEFI_TX_POOL_SWAP: str = "73"  # s
    OP_DEFI_TX_COMPOSITE_SWAP: str = "69"  # i
    OP_DEFI_TX_POOL_ADD_LIQUIDITY: str = "6c"  # l
    OP_DEFI_TX_POOL_REMOVE_LIQUIDITY: str = "72"  # r
    OP_DEFI_TX_POOL_CREATE_PAIR: str = "70"  # p
    OP_DEFI_TX_POOL_UPDATE_PAIR: str = "75"  # u

    # Token
    OP_DEFI_TX_TOKEN_MINT: str = "4d"  # M
    OP_DEFI_TX_TOKEN_CREATE: str = "54"  # T
    OP_DEFI_TX_TOKEN_UPDATE: str = "4e"  # N
    OP_DEFI_TX_TOKEN_UPDATE_ANY: str = "6e"  # n

    # Vault
    OP_DEFI_TX_CREATE_VAULT: str = "56"  # V
    OP_DEFI_TX_UPDATE_VAULT: str = "76"  # v
    OP_DEFI_TX_DEPOSIT_TO_VAULT: str = "53"  # S
    OP_DEFI_TX_WITHDRAW_FROM_VAULT: str = "4A"  # J
    OP_DEFI_TX_CLOSE_VAULT: str = "65"  # e
    OP_DEFI_TX_AUCTION_BID: str = "49"  # I

    @staticmethod
    def from_hex(hex: str) -> str:
        # Accounts
        if hex == "55":
            return "OP_DEFI_TX_UTXOS_TO_ACCOUNT"
        elif hex == "62":
            return "OP_DEFI_TX_ACCOUNT_TO_UTXOS"
        elif hex == "42":
            return "OP_DEFI_TX_ACCOUNT_TO_ACCOUNT"
        elif hex == "61":
            return "OP_DEFI_TX_ANY_ACCOUNT_TO_ACCOUNT"
        elif hex == "51":
            return "OP_DEFI_TX_FUTURE_SWAP"

        # Pool
        elif hex == "73":
            return "OP_DEFI_TX_POOL_SWAP"


