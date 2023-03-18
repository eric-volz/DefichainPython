from typing import Any

from defichain.exceptions.transactions import NotYetSupportedError
from defichain.transactions.constants import DefiTx_SIGNATURE
from .modules.accounts import *
from .modules.pool import *


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

        # Pool
        elif DefiTxType.OP_DEFI_TX_POOL_SWAP == defiTxType:
            return Poolswap.deserialize(network, hex[position:])

        raise NotYetSupportedError()

