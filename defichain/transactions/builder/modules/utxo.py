from defichain.exceptions.transactions import TxBuilderError
from defichain.transactions.rawtransactions import TxAddressOutput, estimate_fee
from defichain.transactions.utils import Converter, Calculate, Token
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class UTXO:
    """
    **The methods of this module are responsible for sending UTXO to different addresses.**

    You can do that three on different ways:

    1. **send**: send just one specified amount from the builder address to another address

    2. **sendall**: send all utxo from the builder address to another address

    3. **sendmany**: send specified amounts from the builder address to multiple different addresses.
    """

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def send(self, amount: "float | int", addressTo: str, changeAddress: str = None, inputs=[]) -> Transaction:
        """
        Creates a transaction that sends the specified amount of UTXO to the specified address and returns the
        remaining UTXO from the input to the sender address if not changed

        >>> builder.utxo.send(1, "df1qw8c57c3c4u7k2h4gv2d5x4jr4qgq6cugg33g6e") # sends one UTXO DFI to the specified address

        :param amount: (required) amount of UTXO to send
        :type amount: float | int
        :param addressTo: (required) address to send the UTXO to
        :type addressTo: str
        :param changeAddress: (optional) address to which the remaining UTXO should be sent
        :type changeAddress: str
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: Transaction
        """
        if changeAddress is None:
            changeAddress = self._builder.get_address()

        # Convert Float to Integer
        value = Converter.float_to_int(amount)

        # If to_address is the same as account address
        if addressTo == self._builder.get_address() or addressTo == changeAddress:
            return self.sendall(addressTo)

        # If to_address is different from account address
        tx = self._builder.build_transactionInputs(inputs)
        input_value = tx.get_inputsValue()
        changeOutputValue = input_value - value
        sendingOutput = TxAddressOutput(value, addressTo)
        changeOutput = TxAddressOutput(changeOutputValue, changeAddress)
        tx.add_output(sendingOutput)
        tx.add_output(changeOutput)

        # Calculate fee
        fee = estimate_fee(tx, self._builder.get_feePerByte())

        # Subtract fee from output
        value = tx.get_outputs()[1].get_value() - fee
        if value < 0:
            raise TxBuilderError("The used address has not enough UTXO to pay the transaction fee")
        tx.get_outputs()[1].set_value(value)

        self._builder.sign(tx)
        return tx

    def sendall(self, addressTo: str, inputs=[]) -> Transaction:
        """
        Creates a transaction that sends all UTXO to the specified address

        >>> builder.utxo.sendall("df1qw8c57c3c4u7k2h4gv2d5x4jr4qgq6cugg33g6e") # sends all UTXO DFI to the specified address

        :param addressTo: (required) address to send the UTXO to
        :type addressTo: str
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        :return: Transaction
        """
        tx = self._builder.build_transactionInputs(inputs)
        inputValue = tx.get_inputsValue()
        output = TxAddressOutput(inputValue, addressTo)
        tx.add_output(output)

        # Calculate fee
        fee = estimate_fee(tx, self._builder.get_feePerByte())

        # Subtract fee from output
        value = tx.get_outputs()[0].get_value() - fee
        if value < 0:
            raise TxBuilderError("The used address has not enough UTXO to pay the transaction fee")
        tx.get_outputs()[0].set_value(value)

        self._builder.sign(tx)
        return tx

    def sendmany(self, addressAmountTo: {}, changeAddress=None, inputs=[]) -> Transaction:
        """
        Creates a transaction that sends the specified amount of UTXO to the specified addresses. Returns the
        remaining UTXO from the input to the sender address if not changed

        >>> builder.utxo.sendmany({"df1qw8c57c3c4u7k2h4gv2d5x4jr4qgq6cugg33g6e": "1@DFI", "df1qzfwy63ggj5jfpul7r04kn2ss8kjz2sda57fa4m": "1@DFI"}) # sends each address one UTXO DFI

        :param addressAmountTo: (required) json with specified address and amount to send
        :type addressAmountTo:  :ref:`Transactions AddressAmount`
        :param changeAddress: (required) address to which the remaining UTXO should be sent
        :type changeAddress: str
        :param inputs: (optional) additional inputs to spend
        :type inputs: [TxInput]
        """

        if inputs is None:
            inputs = []
        if addressAmountTo is None:
            addressAmountTo = {}
        if changeAddress is None:
            changeAddress = self._builder.get_address()

        # Convert Float to Integer
        addressAmountTo = Converter.addressAmount_float_to_int(addressAmountTo)
        outputValue = Calculate.addressAmountSum(addressAmountTo)

        # Building the transaction
        tx = self._builder.build_transactionInputs(inputs)
        inputValue = tx.get_inputsValue()

        # Building Transaction Outputs
        for address in addressAmountTo:
            value, token = addressAmountTo[address].split("@")
            token = Token.checkAndConvert(self._builder.get_network(), token)
            if token != 0:
                raise TxBuilderError("The used method only support sending DFI")
            addressOutput = TxAddressOutput(int(value), address)
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

