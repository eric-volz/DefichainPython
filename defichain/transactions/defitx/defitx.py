from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from defichain.transactions.constants import DefiTxType,  DefiTx_SIGNATURE
from .modules.basedefitx import BaseDefiTx
from .modules.accounts import UtxosToAccount
from .modules.pool import Poolswap


class DefiTx:

    @staticmethod
    def deserialize(network: DefichainMainnet or DefichainTestnet or DefichainRegtest, hex: str) -> "BaseDefiTx":
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

        if DefiTxType.OP_DEFI_TX_UTXOS_TO_ACCOUNT == defiTxType:
            return UtxosToAccount.deserialize(network, hex[position:])
        elif DefiTxType.OP_DEFI_TX_POOL_SWAP == defiTxType:
            return Poolswap.deserialize(network, hex[position:])

