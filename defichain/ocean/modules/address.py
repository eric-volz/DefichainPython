#  https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Address.ts

class Address:
    def __init__(self, ocean):
        self._ocean = ocean

    def listAccountHistory(self, address: str, size: int = 30, next: str = None) -> {}:  # 01
        """
        List account history

        :param address: (required) address to list account history
        :type address: str
        :param size: (optional) size of account history
        :type size: int
        :param next: (optional) next set of account history
        :type next: str
        :return: (json string) {owner: str, txid: str, txn: int, type: str, amounts: str[], block: {height: int,
            hash: str, time: int}

        :example:

        >>> ocean.address.listAccountHistory("dEPoXJzwGia1aAbz6ZRB7FFSKSeWPn1v7A")
        """
        return self._ocean._conn.get(f"address/{address}/history", size=size, next=next)

    def getBalance(self, address: str) -> {}:
        """
        Get current balance of an address

        :param address: (required) address bech32/legacy/b58 formatted address
        :type address: str
        :return: (json string) {data: float}

        :example:

        >>> ocean.address.getBalance("dEPoXJzwGia1aAbz6ZRB7FFSKSeWPn1v7A")
        """
        return self._ocean._conn.get(f"address/{address}/balance")  # 02

    def getAggregation(self, address: str) -> {}:
        """
        Get current aggregated stats of an address

        :param address: (required) address bech32/legacy/b58 formatted address
        :type address: str
        :return: (json string) {id: str, hid: str, block: {hash: str, height: int, time: int, medianTime: int},
            script: {type: str, hex: str}, statistic: {txCount: int, txInCount: int, txOutCount: int},
            amount: {txIn: str, txOut: str, unspent: str}}

        :example:

        >>> ocean.address.getAggregation("dEPoXJzwGia1aAbz6ZRB7FFSKSeWPn1v7A")
        """
        return self._ocean._conn.get(f"address/{address}/aggregation")  # 03

    def listToken(self, address: str, size: int = 30, next: str = None) -> {}:  # 04
        """
        List all tokens balance belonging to an address

        :param address: (required) address bech32/legacy/b58 formatted address
        :type address: str
        :param size: (optional) size to query
        :type size: int
        :param next: (optional) next token for next slice of AddressToken
        :type next: str
        :return: (json string) {id: str, amount: str, symbol: str, displaySymbol: str, symbolKey: str, name: str,
            isDAT: bool, isLPS: bool, isLoanToken: bool}

        :example:

        >>> ocean.address.listToken("dEPoXJzwGia1aAbz6ZRB7FFSKSeWPn1v7A")
        """
        return self._ocean._conn.get(f"address/{address}/tokens", size=size, next=next)

    def listVault(self, address: str, size: int = 30, next: str = None) -> {}:  # 05
        """
        List all vaults belonging to an address

        :param address: (required) address bech32/legacy/b58 formatted address
        :type address: str
        :param size: (optional) size of vaults to query
        :type size: int
        :param next: (optional) next set of vaults
        :type next: str
        :return: (json string) VaultActive or VaultLiquidated

        :example:

        >>> ocean.address.listVault("dEPoXJzwGia1aAbz6ZRB7FFSKSeWPn1v7A")
        """
        return self._ocean._conn.get(f"address/{address}/vaults", size=size, next=next)

    def listTransaction(self, address: str, size: int = 30, next: str = None) -> {}:  # 06
        """
        List all transaction activity belonging to an address

        :param address: (required) address bech32/legacy/b58 formatted address
        :type address: str
        :param size: (optional) size to query
        :type size: int
        :param next: (optional) next token for next slice of AddressActivity
        :type next: str
        :return: (json string) {id: str, hid: str, type: 'vin' | 'vout', typeHex: '00' | '01', txid: str,
            block: {hash: str, height: int, time: int, medianTime: int}, script: {type: str, hex: str},
            vin: {txid: str, n: int}, vout: {txid: str, n: int}, value: str, tokenId: int}

        :example:

        >>> ocean.address.listTransaction("dEPoXJzwGia1aAbz6ZRB7FFSKSeWPn1v7A")
        """
        return self._ocean._conn.get(f"address/{address}/transactions", size=size, next=next)

    def listTransactionUnspent(self, address: str, size: int = 30, next: str = None) -> {}:  # 07
        """
        List all unspent belonging to an address

        :param address: (required) address bech32/legacy/b58 formatted address
        :type address: str
        :param size: (optional) size to query
        :type size: int
        :param next: (optional) next token for next slice of AddressUnspent
        :type next: str
        :return: (json string) {id: string, hid: string, sort: string, block: {hash: string, height: number,
            time: number, medianTime: number}, script: {type: string, hex: string}, vout: {txid: string, n: number,
            value: string, tokenId?: number}}

        :example:

        >>> ocean.address.listTransactionUnspent("dEPoXJzwGia1aAbz6ZRB7FFSKSeWPn1v7A")
        """
        return self._ocean._conn.get(f"address/{address}/transactions/unspent", size=size, next=next)
