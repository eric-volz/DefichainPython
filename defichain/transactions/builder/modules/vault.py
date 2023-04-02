from defichain.transactions.defitx import CreateVault
from defichain.transactions.utils import Converter
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Vault:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def createvault(self, ownerAddress: str, schemeId: str, inputs=[]):
        """
        Creates a transaction for creating a vault with the specified data

        :param ownerAddress: (required) the address where vault will be created
        :type ownerAddress: str
        :param schemeId: (required) the scheme id for the vault
        :type schemeId: str
        """

        defiTx = CreateVault(ownerAddress, schemeId)
        return self._builder.build_defiTx(100000000, defiTx, inputs)
