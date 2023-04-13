from defichain.transactions.defitx import CreateVault, DepositToVault, WithdrawFromVault
from defichain.transactions.utils import Converter
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Vault:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def createvault(self, ownerAddress: str, schemeId: str, inputs=[]) -> Transaction:
        """
        Creates a transaction for creating a vault

        :param ownerAddress: (required) the address where vault will be created
        :type ownerAddress: str
        :param schemeId: (required) the scheme id for the vault
        :type schemeId: str
        :param inputs: (optional) Inputs
        :type inputs: TxInput
        """

        defiTx = CreateVault(ownerAddress, schemeId)
        return self._builder.build_defiTx(100000000, defiTx, inputs)

    def deposittovault(self, vaultId: str, addressFrom: str, amount: str, inputs=[]) -> Transaction:
        """
        Creates a transaction for depositing collateral token amount to vault

        :param vaultId: (required) vault id
        :type vaultId: str
        :param addressFrom: (required) address containing collateral
        :type addressFrom: str
        :param amount: (required) Amount of collateral in amount@symbol format
        :type amount: str
        :param inputs: (optional) Inputs
        :type inputs: TxInput
        :return: Transaction
        """

        # Convert Float to Integer
        amount = Converter.amount_float_to_int(amount)

        defiTx = DepositToVault(vaultId, addressFrom, amount)
        return self._builder.build_defiTx(0, defiTx, inputs)

    def withdrawfromvault(self, vaultId: str, addressTo: str, amount: str, inputs=[]) -> Transaction:
        """
        Creates a transaction for withdraw of collateral token from a vault

        :param vaultId: (required) vault id
        :type vaultId: str
        :param addressTo: (required) destination address for withdraw of collateral
        :type addressTo: str
        :param amount: (required) Amount of collateral in amount@symbol format
        :type amount: str
        :param inputs: (optional) Inputs
        :type inputs: TxInput
        :return: Transaction
        """

        # Convert Float to Integer
        amount = Converter.amount_float_to_int(amount)

        defiTx = WithdrawFromVault(vaultId, addressTo, amount)
        return self._builder.build_defiTx(0, defiTx, inputs)
