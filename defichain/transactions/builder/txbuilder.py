from defichain import Account, Ocean

from defichain.exceptions.transactions import TxBuilderError

from defichain.transactions.remotedata.remotedata import RemoteData
from defichain.transactions.remotedata import RemoteDataOcean

from defichain.transactions.builder import RawTransactionBuilder, UTXO, Pool

from defichain.transactions.rawtransactions import Transaction


class TxBuilder:
    def __init__(self, address: str, account: Account, datasource: Ocean):
        self._address, self._account, self._datasource = None, None, None
        self._set_address(address)
        self._set_account(account)
        self._set_datasource(datasource)

        _builder = RawTransactionBuilder(self._get_address(), self._get_account(), self._get_datasource())

        self.utxo = UTXO(_builder)
        self.pool = Pool(_builder)

    # Methods
    def send(self, tx: Transaction, maxFeeRate: int = None) -> str:
        if not tx._signed:
            raise TxBuilderError("The transaction cannot be sent because it is not yet signed!")

        return self._get_datasource().send_tx(tx.serialize(), maxFeeRate)

    # Get Information
    def _get_address(self) -> str:
        return self._address

    def _get_account(self) -> Account:
        return self._account

    def _get_datasource(self) -> "RemoteData":
        return self._datasource

    # Set Information
    def _set_address(self, address: str) -> None:
        self._address = address

    def _set_account(self, account: Account) -> None:
        self._account = account

    def _set_datasource(self, source: Ocean) -> None:
        if isinstance(source, Ocean):
            self._datasource = RemoteDataOcean(source)
        else:
            raise TxBuilderError("The given source is currently not usable")


