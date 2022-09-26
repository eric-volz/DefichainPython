# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/MasterNodes.ts

class Masternodes:
    def __init__(self, ocean):
        self._ocean = ocean

    def list(self, size: int = 30, next: str = None) -> {}:  # 01
        """
        Get list of masternodes

        :param size: (optional) size masternodes size to query
        :type size: int
        :param next: (optional) next set of masternodes to get
        :type next: str
        :return: (json string) {id: str, sort: str, state: MasternodeState, mintedBlocks: int, owner: {address: str},
            operator: {address: str}, creation: {height: int}, resign: {tx: str, height: int},
            timelock: int}

        :example:

        >>> ocean.masternodes.list()
        """
        return self._ocean._conn.get("masternodes", size=size, next=next)

    def get(self, id: str) -> {}:  # 02
        """
        Get information about a masternode with given id

        :param id: (required) id masternode id to get
        :type id: str
        :return: (json string) {id: str, sort: str, state: MasternodeState, mintedBlocks: int, owner: {address: str},
            operator: {address: str}, creation: {height: int}, resign: {tx: str, height: int},
            timelock: int}

        :example:

        >>> ocean.masternodes.get("bbdd23cfb429680fd10a3ce169595ff6123ef576bb936add069812528f73ceaa")
        """
        return self._ocean._conn.get(f"masternodes/{id}")
