from defichain.transactions.rawtransactions import TxOutput, calculate_fee_for_unsigned_transaction
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class UTXO:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def send(self, value: int, addressTo: str, changeAddress: str = "fromAddress") -> Transaction:
        if changeAddress == "fromAddress":
            changeAddress = self._builder.get_address()

        # If to_address is the same as account address
        if addressTo == self._builder.get_address() or addressTo == changeAddress:
            return self.sendall(addressTo)

        # If to_address is different from account address
        tx = self._builder.build_transactionInputs()
        input_value = tx.get_inputsValue()
        changeOutputValue = input_value - value
        sendingOutput = TxOutput(value, addressTo)
        changeOutput = TxOutput(changeOutputValue, changeAddress)
        tx.add_output(sendingOutput)
        tx.add_output(changeOutput)

        # Subtract fee from output
        fee = calculate_fee_for_unsigned_transaction(tx)
        tx.get_outputs()[1].set_value(tx.get_outputs()[1].get_value() - fee)

        self._builder.sign(tx)
        return tx

    def sendall(self, addressTo: str) -> Transaction:
        tx = self._builder.build_transactionInputs()
        inputValue = tx.get_inputsValue()
        output = TxOutput(inputValue, addressTo)
        tx.add_output(output)

        # Subtract fee from output
        fee = calculate_fee_for_unsigned_transaction(tx)
        tx.get_outputs()[0].set_value(tx.get_outputs()[0].get_value() - fee)

        self._builder.sign(tx)
        return tx


