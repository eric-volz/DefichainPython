from defichain.transactions.defitx import CreateMasternode, ResignMasternode, UpdateMasternode
from defichain.transactions.utils import Converter
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Masternode:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def createmasternode(self, operatorAddress: str, timeLock: int = 0, inputs=[]) -> Transaction:
        """
        Creates a transaction to create a masternode with the given operator address and time lock

        :param operatorAddress: (required) legacy address of the operator
        :type operatorAddress: str
        :param timeLock: (optional) time period to lock the masternode: 0 (default), 5, 10 years
        :type timeLock: int
        """

        defiTx = CreateMasternode(operatorAddress, timeLock)
        return self._builder.build_defiTx(1000000000, defiTx, inputs)

    def resignmasternode(self, masternodeId: str, inputs=[]) -> Transaction:
        """
        Creates a transaction resigning your masternode.

        :param masternodeId: (required) masternodeId: txid of the creation of the masternode
        :type masternodeId: str
        """

        defiTx = ResignMasternode(masternodeId)
        return self._builder.build_defiTx(0, defiTx, inputs)

