from defichain.transactions.defitx import UtxosToAccount, AccountToAccount
from defichain.transactions.utils import Converter
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Accounts:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def utxostoaccount(self, address: str, value: "int | float", tokenId: int = 0, inputs=[]) -> "Transaction":
        """
        Converts UTXOs to token

        :param address: (required) the address of the account to be converted from
        :type address: str
        :param value: (required) the amount of UTXOs to convert to token
        :type value: int | float
        :param tokenId: (optional) the token id of the converted token (default: 0 -> DFI)
        :type tokenId: int
        :param inputs: (optional) Inputs
        :type inputs: TxInput
        :return: Transaction
        """
        # Convert Float to Integer
        value = Converter.float_to_int(value)

        defiTx = UtxosToAccount(address, value, tokenId)
        return self._builder.build_defiTx(value, defiTx, inputs)

    def accounttoaccount(self, addressFrom: str, addressAmountTo: {}, inputs=[]) -> "Transaction":
        """
        Sends token from one address to another address

        :param addressFrom: (required) address from which the tokens should be sent
        :type addressFrom: str
        :param addressAmountTo: (required) addressAmount
        :type addressAmountTo: addressAmount
        :param inputs: (optional) Inputs
        :type inputs: TxInput
        :return: Transaction
        """

        # Convert Float to Integer
        addressAmountTo = Converter.addressAmount_float_to_int(addressAmountTo)

        defiTx = AccountToAccount(addressFrom, addressAmountTo)
        return self._builder.build_defiTx(0, defiTx, inputs)
