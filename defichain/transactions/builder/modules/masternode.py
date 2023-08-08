from defichain.transactions.defitx import CreateMasternode, ResignMasternode, UpdateMasternode
from defichain.transactions.utils import Converter
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Masternode:
    """
    **The methods of this module create masternode transactions**

    1. **createmasternode**: transaction to create a masternode

    2. **resignmasternode**: transaction to resigning the masternode

    3. **updatemasternode**: transaction to change owner, operator or reward address of a masternode
    """

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def createmasternode(self, operatorAddress: str, timeLock: int = 0, inputs=[]) -> Transaction:
        """
        Creates a transaction to create a masternode with the given operator address and time lock

        >>> builder.masternode.createmasternode("8HZ4oMoussmoVRghTaSqmB4Q74wPeiCyHC") # create a masternode

        :param operatorAddress: (required) legacy address of the operator
        :type operatorAddress: str
        :param timeLock: (optional) time period to lock the masternode: 0 (default), 5, 10 years
        :type timeLock: int
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: :ref:`Transaction Advanced RawTransactions Transaction`
        """

        defiTx = CreateMasternode(operatorAddress, timeLock)
        return self._builder.build_defiTx(1000000000, defiTx, inputs)

    def resignmasternode(self, masternodeId: str, inputs=[]) -> Transaction:
        """
        Creates a transaction to resigning the masternode.

        >>> builder.masternode.resignmasternode("4e5a3a891653b7ea017a0560f5c873bdf183f52a013606341faa2823c54a2d9c") # resign a masternode

        :param masternodeId: (required) masternode id
        :type masternodeId: str
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: :ref:`Transaction Advanced RawTransactions Transaction`
        """

        defiTx = ResignMasternode(masternodeId)
        return self._builder.build_defiTx(0, defiTx, inputs)

    def updatemasternode(self, masternodeId: str, ownerAddress: str = None, operatorAddress: str = None,
                         rewardAddress: str = None, inputs=[]) -> Transaction:
        """
        Creates a transaction to change owner, operator or reward address of a masternode.

        >>> builder.masternode.updatemasternode(rewardAddress="df1qtmk8nad9n03nwmanqfpug94h3jqjn3gyytl3gl") # update masternode reward address

        :param masternodeId: (required) masternode id
        :type masternodeId: str
        :param ownerAddress: (optional) new owner address
        :type ownerAddress: str
        :param operatorAddress: (optional) new operator address
        :type operatorAddress: str
        :param rewardAddress: (optional) new reward address
        :type rewardAddress: str
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: :ref:`Transaction Advanced RawTransactions Transaction`
        """
        defiTx = UpdateMasternode(masternodeId, ownerAddress, operatorAddress, rewardAddress)
        return self._builder.build_defiTx(0, defiTx, inputs)

