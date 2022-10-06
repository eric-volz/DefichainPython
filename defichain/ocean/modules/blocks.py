# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Blocks.ts

class Blocks:
    def __init__(self, ocean):
        self._ocean = ocean

    def list(self, size: int = 30, next: str = None) -> {}:  # 01
        """
        Returns a list of blocks

        :param size: (optional) size to query
        :type size: int
        :param next: next token for next slice of blocks
        :type next: (optional) str
        :return: (json string) {id: str, hash: str, previousHash: str, height: int, version: int, time: int,
            medianTime: int, transactionCount: int, difficulty: float, masternode: str, minter: str,
            minterBlockCount: int, reward: str, stakeModifier: str, merkleroot: str, size: int,
            sizeStripped: int, weight: int}

        :example:

        >>> ocean.blocks.list()
        """
        return self._ocean._conn.get("blocks", size=size, next=next)

    def get(self, id: str) -> {}:  # 02
        """
        Returns the specified block

        :param id: (required) id as hash or height of the block
        :type id: str
        :return: (json string) {id: str, hash: str, previousHash: str, height: int, version: int, time: int,
            medianTime: int, transactionCount: int, difficulty: float, masternode: str, minter: str,
            minterBlockCount: int, reward: str, stakeModifier: str, merkleroot: str, size: int,
            sizeStripped: int, weight: int}

        :example:

        >>> ocean.blocks.get(0)
        """
        return self._ocean._conn.get(f"blocks/{id}")

    def getTransactions(self, hash: str, size: int = 30, next: str = None) -> {}:  # 03
        """
        Gets all transactions within a block

        :param hash: (required) hash of the block
        :type hash: str
        :param size: (optional) size to query
        :type size: int
        :param next: (optional) next token for next slice of blocks
        :type next: str
        :return: (json string) {id: str, order: int, block: {hash: str, height: int, time: int,
            medianTime: int}, txid: str, hash: str, version: int, size: int, vSize: int,
            weight: int, lockTime: int, vinCount: int, voutCount: int, totalVoutValue: str}

        :example:

        >>> ocean.blocks.getTransactions("e5b266f18db7662628ea503eb9f889197f05660981f22c07b1b3b86f14329099")
        """
        return self._ocean._conn.get(f"blocks/{hash}/transactions", size=size, next=next)
