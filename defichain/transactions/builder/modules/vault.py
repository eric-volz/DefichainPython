from defichain.transactions.defitx import CreateVault, DepositToVault, WithdrawFromVault
from defichain.transactions.utils import Converter
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Vault:
    """
    **The methods of this module create vault transactions**

    1. **createvault**: transaction for creating a vault

    2. **deposittovault**: transaction for depositing collateral token to a vault

    3. **withdrawfromvault**: transaction for withdraw of collateral from a vault
    """

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def createvault(self, ownerAddress: str, schemeId: str, inputs=[]) -> Transaction:
        """
        Creates a transaction for creating a vault.

        The creation of a vault will cost you 1 UTXO as a fee by the blockchain.

        SchemeIDs mainnet: MIN1000, MIN500, MIN350, MIN200, MIN175, MIN150
        SchemeIDs testnet: C1000, C500, C350, C200, C175, C150

        >>> builder.vault.createvault("df1qw8c57c3c4u7k2h4gv2d5x4jr4qgq6cugg33g6e", "MIN150") # creates a new vault

        :param ownerAddress: (required) the address where vault will be created
        :type ownerAddress: str
        :param schemeId: (required) the scheme id for the vault
        :type schemeId: str
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: Transaction
        """

        defiTx = CreateVault(ownerAddress, schemeId)
        return self._builder.build_defiTx(100000000, defiTx, inputs)

    def deposittovault(self, vaultId: str, addressFrom: str, amount: str, inputs=[]) -> Transaction:
        """
        Creates a transaction for depositing collateral token to a vault

        >>> builder.vault.deposittovault("5cbe99407674a689fa9b8a522462b7a4b3e7893f61453ce3fa77f1307f7d0600", "df1qw8c57c3c4u7k2h4gv2d5x4jr4qgq6cugg33g6e", "100@DFI") # deposits collateral to a vault

        :param vaultId: (required) vault id
        :type vaultId: str
        :param addressFrom: (required) address containing collateral
        :type addressFrom: str
        :param amount: (required) string with amount and token separated by an @
        :type amount: :ref:`Transactions Amounts`
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: Transaction
        """

        # Convert Float to Integer
        amount = Converter.amount_float_to_int(amount)

        defiTx = DepositToVault(vaultId, addressFrom, amount)
        return self._builder.build_defiTx(0, defiTx, inputs)

    def withdrawfromvault(self, vaultId: str, addressTo: str, amount: str, inputs=[]) -> Transaction:
        """
        Creates a transaction for withdraw of collateral from a vault

        >>> builder.vault.withdrawfromvault("5cbe99407674a689fa9b8a522462b7a4b3e7893f61453ce3fa77f1307f7d0600", "df1qw8c57c3c4u7k2h4gv2d5x4jr4qgq6cugg33g6e", "100@DFI") # withdraws collateral from a vault

        :param vaultId: (required) vault id
        :type vaultId: str
        :param addressTo: (required) destination address for withdrawn collateral
        :type addressTo: str
        :param amount: (required) string with amount and token separated by an @
        :type amount: :ref:`Transactions Amounts`
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: Transaction
        """

        # Convert Float to Integer
        amount = Converter.amount_float_to_int(amount)

        defiTx = WithdrawFromVault(vaultId, addressTo, amount)
        return self._builder.build_defiTx(0, defiTx, inputs)
