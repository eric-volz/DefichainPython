from defichain.transactions.defitx import UtxosToAccount, AccountToUtxos, AccountToAccount
from defichain.transactions.utils import Converter, Calculate
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Accounts:
    """
    **The methods of this module create transactions that interact with your account/address.**

    1. **utxostoaccount**: converts the specified amount of UTXO to token

    2. **accounttoutxos**: converts specified amount of token to UTXO

    3. **accounttoaccount**: sends token from one address to another address

    """

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def utxostoaccount(self, address: str, amount: "float | int", tokenId: int = 0, inputs=[]) -> "Transaction":
        """
        Creates a transaction that converts the specified amount of UTXO to token

        >>> builder.accounts.utxostoaccount("df1qw8c57c3c4u7k2h4gv2d5x4jr4qgq6cugg33g6e", 1) # converts one UTXO to token

        :param address: (required) the address of the account to be converted from
        :type address: str
        :param amount: (required) the amount of UTXOs to convert to token
        :type amount: float | int
        :param tokenId: (optional) the token id of the converted token (default: 0 -> DFI)
        :type tokenId: int
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: :ref:`Transaction Advanced RawTransactions Transaction`
        """
        # Convert Float to Integer
        amount = Converter.float_to_int(amount)

        defiTx = UtxosToAccount(address, amount, tokenId)
        return self._builder.build_defiTx(amount, defiTx, inputs)

    def accounttoutxos(self, addressFrom: str, addressAmountTo: {}, inputs=[]) -> "Transaction":
        """
        Creates a transaction that converts specified amount of token to UTXO

        >>> builder.accounts.accounttoutxos("df1qw8c57c3c4u7k2h4gv2d5x4jr4qgq6cugg33g6e", {"df1qw8c57c3c4u7k2h4gv2d5x4jr4qgq6cugg33g6e": "1@DFI", "df1qzfwy63ggj5jfpul7r04kn2ss8kjz2sda57fa4m": "1@DFI"}) # converts two token to UTXO

        :param addressFrom: (required) the address of the account to be converted from
        :type addressFrom: str
        :param addressAmountTo: (required) json with specified address and amount to send
        :type addressAmountTo: :ref:`Transactions AddressAmount`
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: :ref:`Transaction Advanced RawTransactions Transaction`
        """
        # Convert Float to Integer
        addressAmountTo = Converter.addressAmount_float_to_int(addressAmountTo)
        value = Calculate.addressAmountSum(addressAmountTo)

        defiTx = AccountToUtxos(addressFrom, value, 2)
        return self._builder.build_defiTx(0, defiTx, inputs, addressAmountTo=addressAmountTo)

    def accounttoaccount(self, addressFrom: str, addressAmountTo: {}, inputs=[]) -> "Transaction":
        """
        Creates a transaction that sends token from one address to another address

        >>> builder.accounts.accounttoaccount("df1qw8c57c3c4u7k2h4gv2d5x4jr4qgq6cugg33g6e", {"df1qw8c57c3c4u7k2h4gv2d5x4jr4qgq6cugg33g6e": "0.00001@BTC", "df1qzfwy63ggj5jfpul7r04kn2ss8kjz2sda57fa4m": "1@DFI"}) # sends 0.00001 BTC and 1 DFI to other addresses

        :param addressFrom: (required) address from which the tokens should be sent
        :type addressFrom: str
        :param addressAmountTo: (required) json with specified address and amount to send
        :type addressAmountTo: :ref:`Transactions AddressAmount`
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: :ref:`Transaction Advanced RawTransactions Transaction`
        """

        # Convert Float to Integer
        addressAmountTo = Converter.addressAmount_float_to_int(addressAmountTo)

        defiTx = AccountToAccount(addressFrom, addressAmountTo)
        return self._builder.build_defiTx(0, defiTx, inputs)
