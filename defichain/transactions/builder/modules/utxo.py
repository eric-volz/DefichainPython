from defichain.transactions.rawtransactions import TxOutput, calculate_fee_for_unsigned_transaction
from defichain.transactions.builder.rawtransactionbuilder import RawTransactionBuilder, Transaction


class UTXO:

    def __init__(self, builder):
        self._builder: RawTransactionBuilder = builder

    def send(self, value: int, to_address: str, change_address: str = "from_address") -> Transaction:
        # TODO: Remove static fee with dynamic fee
        if change_address == "from_address":
            change_address = self._builder.get_address()

        # If to_address is the same as account address
        if to_address == self._builder.get_address() or to_address == change_address:
            return self.sendall(to_address)

        # If to_address is different from account address
        tx = self._builder.build_transaction_inputs()
        input_value = tx.get_inputs_value()
        change_output_value = input_value - value
        sending_output = TxOutput(value, to_address)
        change_output = TxOutput(change_output_value, change_address)
        tx.add_output(sending_output)
        tx.add_output(change_output)

        # Subtract fee from output
        fee = calculate_fee_for_unsigned_transaction(tx)
        tx.get_outputs()[1].set_value(tx.get_outputs()[1].get_value() - fee)

        self._builder.sign(tx)
        return tx

    def sendall(self, to_address: str) -> Transaction:
        tx = self._builder.build_transaction_inputs()
        input_value = tx.get_inputs_value()
        output = TxOutput(input_value, to_address)
        tx.add_output(output)

        # Subtract fee from output
        fee = calculate_fee_for_unsigned_transaction(tx)
        tx.get_outputs()[0].set_value(tx.get_outputs()[0].get_value() - fee)

        self._builder.sign(tx)
        return tx


