from typing import Any

from defichain.exceptions.transactions import NotYetSupportedError
from defichain.transactions.constants import DefiTx_SIGNATURE
from .modules.accounts import *
from .modules.loans import *
from .modules.pool import *

from .modules.vault import *


class DefiTx:

    @staticmethod
    def deserialize(network: Any, hex: str) -> "BaseDefiTx":
        position = 0

        opReturn = hex[position: position + 2]
        position += 2

        lengthStandard = hex[position: position + 2]
        position += 2

        if hex[position: position + 8] == DefiTx_SIGNATURE:
            signature = hex[position: position + 8]
            position += 8
        else:
            lengthExtra = hex[position: position + 2]
            position += 2
            signature = hex[position: position + 8]
            position += 8

        defiTxType = hex[position: position + 2]
        position += 2

        # Account
        if DefiTxType.OP_DEFI_TX_UTXOS_TO_ACCOUNT == defiTxType:
            return UtxosToAccount.deserialize(network, hex[position:])
        elif DefiTxType.OP_DEFI_TX_ACCOUNT_TO_ACCOUNT == defiTxType:
            return AccountToAccount.deserialize(network, hex[position:])

        # Loans
        if DefiTxType.OP_DEFI_TX_TAKE_LOAN == defiTxType:
            return TakeLoan.deserialize(network, hex[position:])
        if DefiTxType.OP_DEFI_TX_PAYBACK_LOAN == defiTxType:
            return PaybackLoan.deserialize(network, hex[position:])

        # Pool
        elif DefiTxType.OP_DEFI_TX_POOL_SWAP == defiTxType:
            return PoolSwap.deserialize(network, hex[position:])
        elif DefiTxType.OP_DEFI_TX_COMPOSITE_SWAP == defiTxType:
            return CompositeSwap.deserialize(network, hex[position:])
        elif DefiTxType.OP_DEFI_TX_POOL_ADD_LIQUIDITY == defiTxType:
            return AddPoolLiquidity.deserialize(network, hex[position:])
        elif DefiTxType.OP_DEFI_TX_POOL_REMOVE_LIQUIDITY == defiTxType:
            return RemovePoolLiquidity.deserialize(network, hex[position:])

        # Vault
        elif DefiTxType.OP_DEFI_TX_CREATE_VAULT == defiTxType:
            return CreateVault.deserialize(network, hex[position:])
        elif DefiTxType.OP_DEFI_TX_DEPOSIT_TO_VAULT == defiTxType:
            return DepositToVault.deserialize(network, hex[position:])
        elif DefiTxType.OP_DEFI_TX_WITHDRAW_FROM_VAULT == defiTxType:
            return WithdrawFromVault.deserialize(network, hex[position:])

        raise NotYetSupportedError()

