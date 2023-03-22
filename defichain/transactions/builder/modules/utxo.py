from defichain.exceptions.transactions import TxBuilderError
from defichain.transactions.rawtransactions import TxAddressOutput, estimate_fee
from defichain.transactions.utils import Converter
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class UTXO:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def send(self, value: "float | int", addressTo: str, changeAddress: str = None, inputs=[]) -> Transaction:
        """
        Sends the specified amount of UTXO to the specified address. Returns the remaining UTXO from the input to the
        sender address if not changed.

        :param value: (required) amount of UTXO to send
        :type value: float | int
        :param addressTo: (required) address to send the UTXO to
        :type addressTo: str
        :param changeAddress: (optional) address to which the remaining UTXO should be sent
        :type changeAddress: str
        :param inputs: (optional) Inputs
        :type inputs: TxInputs
        :return: Transaction
        """
        if changeAddress is None:
            changeAddress = self._builder.get_address()

        # Convert Float to Integer
        value = Converter.float_to_int(value)

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
        Sends all UTXO to the specified address

        :param addressTo: (required) address to send the UTXO to
        :type addressTo: str
        :param inputs: (optional) Inputs
        :type inputs: TxInput
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
