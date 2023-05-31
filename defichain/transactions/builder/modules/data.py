from defichain.exceptions.transactions import TxBuilderError
from defichain.transactions.rawtransactions import TxAddressOutput, TxDataOutput, estimate_fee
from defichain.transactions.utils import Converter, Calculate
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class Data:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def hex_data(self, data: str, addressAmountTo=None, changeAddress: str = None, inputs=None) -> Transaction:
        """
        Creates a transaction to submit data to the blockchain

        :param data: (required) hexadecimal data
        :type data: str
        :param addressAmountTo: (required) AddressAmount
        :type addressAmountTo: json string
        :param changeAddress: (required) address to which the remaining UTXO should be sent
        :type changeAddress: str
        :param inputs: (optional) Inputs
        :type inputs: TxInput
        :return: Transaction
        """

        if inputs is None:
            inputs = []
        if addressAmountTo is None:
            addressAmountTo = {}
        if changeAddress is None:
            changeAddress = self._builder.get_address()

        # Convert Float to Integer
        addressAmountTo = Converter.addressAmount_float_to_int(addressAmountTo)
        outputValue = Calculate.addressAmount_sum(addressAmountTo)

        # Building the transaction
        tx = self._builder.build_transactionInputs(inputs)
        inputValue = tx.get_inputsValue()

        # Building Transaction Outputs
        messageOutput = TxDataOutput(data)
        tx.add_output(messageOutput)

        for address in addressAmountTo:
            value, token = addressAmountTo[address].split("@")
            addressOutput = TxAddressOutput(value, address)
            tx.add_output(addressOutput)

        changeOutputValue = inputValue - outputValue
        changeOutput = TxAddressOutput(changeOutputValue, changeAddress)
        tx.add_output(changeOutput)

        # Calculate fee
        fee = estimate_fee(tx, self._builder.get_feePerByte())

        # Subtract fee from output
        value = changeOutput.get_value() - fee
        if value < 0:
            raise TxBuilderError("The used address has not enough UTXO to pay the transaction fee")
        changeOutput.set_value(value)

        self._builder.sign(tx)
        return tx

    def str_data(self, data: str, addressAmountTo=None, changeAddress: str = None, inputs=None) -> Transaction:
        """
        Creates a transaction to submit data to the blockchain

        :param data: (required) string data
        :type data: str
        :param addressAmountTo: (required) AddressAmount
        :type addressAmountTo: json string
        :param changeAddress: (required) address to which the remaining UTXO should be sent
        :type changeAddress: str
        :param inputs: (optional) Inputs
        :type inputs: TxInput
        :return: Transaction
        """
        if inputs is None:
            inputs = []
        if addressAmountTo is None:
            addressAmountTo = {}

        return self.hex_data(Converter.str_to_hex(data), addressAmountTo, changeAddress, inputs)
