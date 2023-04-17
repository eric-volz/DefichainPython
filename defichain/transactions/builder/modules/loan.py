from defichain.transactions.defitx import TakeLoan
from defichain.transactions.utils import Converter
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Loan:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def takeloan(self, vaultId: str, addressTo: str, amounts: "str | [str]", inputs=[]) -> Transaction:
        """
        Creates a transaction to mint loan token in desired amount based on defined loan

        :param vaultId: (required) id of vault used for loan
        :type vaultId: str
        :param addressTo: (required) address to transfer tokens
        :type addressTo: str
        :param amounts: (required) AddressAmount
        :type amounts: str | [str]
        """

        # Convert Float to Integer
        if not isinstance(amounts, list):
            amounts = [amounts]

        convertedAmount = []
        for amount in amounts:
            convertedAmount.append(Converter.amount_float_to_int(amount))

        defiTx = TakeLoan(vaultId, addressTo, convertedAmount)
        return self._builder.build_defiTx(0, defiTx, inputs)

