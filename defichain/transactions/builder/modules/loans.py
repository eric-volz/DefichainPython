from defichain.transactions.defitx import TakeLoan, PaybackLoan
from defichain.transactions.utils import Converter
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Loans:
    """
    **The methods of this module create loan transactions**

    1. **takeloan**: transaction to take a loan in the desired amount out of the specified vault

    2. **paybackloan**: transaction to pay back the loan token to the specified vault
    """

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def takeloan(self, vaultId: str, addressTo: str, amounts: "str | [str]", inputs=[]) -> Transaction:
        """
        Creates a transaction to take a loan in the desired amount out of the specified vault

        >>> builder.loan.takeloan("8040fe5eaa75f942dabf57bcdace3a5b71e3eb4fab53467e064e870396913800", "df1qrvrnk0zyaen8x3pfrza3yznwrrrv5y08rkgrk2", ["1@DUSD", "2@COIN"]) # takes loan from a vault

        :param vaultId: (required) vault id
        :type vaultId: str
        :param addressTo: (required) address to transfer tokens to
        :type addressTo: str
        :param amounts: (required) string with amount and token separated by an @
        :type amounts: :ref:`Transactions Amounts`
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: :ref:`Transaction Advanced RawTransactions Transaction`
        """

        # Convert Float to Integer
        if not isinstance(amounts, list):
            amounts = [amounts]

        convertedAmount = []
        for amount in amounts:
            convertedAmount.append(Converter.amount_float_to_int(amount))

        defiTx = TakeLoan(vaultId, addressTo, convertedAmount)
        return self._builder.build_defiTx(0, defiTx, inputs)

    def paybackloan(self, vaultId: str, addressFrom: str, amounts: "str | [str]", inputs=[]) -> Transaction:
        """
        Creates a transaction to pay back the loan token to the specified vault

        >>> builder.loan.paybackloan("8040fe5eaa75f942dabf57bcdace3a5b71e3eb4fab53467e064e870396913800", "df1qrvrnk0zyaen8x3pfrza3yznwrrrv5y08rkgrk2", ["1@DUSD", "2@COIN"]) # pay backs loan to a vault

        :param vaultId: (required) vault id
        :type vaultId: str
        :param addressFrom: (required) address containing repayment tokens
        :type addressFrom: str
        :param amounts: (required) string with amount and token separated by an @
        :type amounts: :ref:`Transactions Amounts`
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: :ref:`Transaction Advanced RawTransactions Transaction`
        """

        # Convert Float to Integer
        if not isinstance(amounts, list):
            amounts = [amounts]

        convertedAmount = []
        for amount in amounts:
            convertedAmount.append(Converter.amount_float_to_int(amount))

        defiTx = PaybackLoan(vaultId, addressFrom, convertedAmount)
        return self._builder.build_defiTx(0, defiTx, inputs)
