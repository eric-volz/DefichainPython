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
        :param inputs: (optional) Inputs
        :type inputs: TxInput
        :return: Transaction
        """

        defiTx = CreateMasternode(operatorAddress, timeLock)
        return self._builder.build_defiTx(1000000000, defiTx, inputs)

    def resignmasternode(self, masternodeId: str, inputs=[]) -> Transaction:
        """
        Creates a transaction resigning your masternode.

        :param masternodeId: (required) txid of the creation of the masternode
        :type masternodeId: str
        :param inputs: (optional) Inputs
        :type inputs: TxInput
        :return: Transaction
        """

        defiTx = ResignMasternode(masternodeId)
        return self._builder.build_defiTx(0, defiTx, inputs)

    def updatemasternode(self, masternodeId: str, ownerAddress: str = None, operatorAddress: str = None,
                         rewardAddress: str = None, inputs=[]) -> Transaction:
        """
        Creates a transaction to change owner, operator or reward address of a masternode.

        :param masternodeId: (required) txid of the creation of the masternode
        :type masternodeId: str
        :param ownerAddress: (optional) new owner address
        :type ownerAddress: str
        :param operatorAddress: (optional) new operator address
        :type operatorAddress: str
        :param rewardAddress: (optional) new reward address
        :type rewardAddress: str
        :param inputs:(optional) Inputs
        :type inputs: TxInput
        :return: Transaction
        """
        defiTx = UpdateMasternode(masternodeId, ownerAddress, operatorAddress, rewardAddress)
        return self._builder.build_defiTx(0, defiTx, inputs)

