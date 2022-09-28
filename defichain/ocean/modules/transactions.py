# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Transactions.ts

class Transactions:
    def __init__(self, ocean):
        self._ocean = ocean

    def get(self, id: str) -> {}:
        """
        Get a Transaction

        :param id: (required) id of transaction to query
        :type id: str
        :return: (json string) {id: str, order: int, block: {hash: str, height: int, time: int,
            medianTime: int}, txid: str, hash: str, version: int, size: int, vSize: int,
            weight: int, lockTime: int, vinCount: int, voutCount: int, totalVoutValue: str}

        :example:

        >>> ocean.transactions.get("8d654cdaeba4633aa08e46f1aa258aae7234e89945145f61bc1bd5b342df1069")
        """
        return self._ocean._conn.get(f"transactions/{id}")

    def getVins(self, txid: str, size: int = 30, next: str = None) -> {}:
        """
        Get a list of vins of a Transaction

        :param txid: (required) txid of the transaction
        :type txid: str
        :param size: (optional) size to query
        :type size: int
        :param next: (optional) next token for next slice of vin
        :type next: str
        :return: (json string) {id: str, txid: str, coinbase: str, vout: {id: str, txid: str, n: int,
            value: str, tokenId: int, script: {hex: str}}, script: {hex: str}, txInWitness: str[],
            sequence: str}

        :example:

        >>> ocean.transactions.getVins("8d654cdaeba4633aa08e46f1aa258aae7234e89945145f61bc1bd5b342df1069")
        """
        return self._ocean._conn.get(f"transactions/{txid}/vins", size=size, next=next)

    def getVouts(self, txid: str, size: int = 30, next: str = None) -> {}:
        """
        Get a list of vouts of a Transaction

        :param txid: (required) txid of the transaction
        :type txid: str
        :param size: (optional) size to query
        :type size: int
        :param next: (optional) next token for next slice of vout
        :type next: str
        :return: (json string) {id: str, txid: str, n: int, value: str, tokenId: int,
            script: {hex: str, type: str}}

        :example:

        >>> ocean.transactions.getVouts("8d654cdaeba4633aa08e46f1aa258aae7234e89945145f61bc1bd5b342df1069")
        """
        return self._ocean._conn.get(f"transactions/{txid}/vouts", size=size, next=next)
