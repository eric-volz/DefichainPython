# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Rpc.ts

class Rpc:
    def __init__(self, ocean):
        self._ocean = ocean

    def call(self, method: str, *params: []) -> {}:
        """
        Call an RPC method

        :param method: (required) method of the RPC method
        :type method: str
        :param params: (optinal) params to send upstream
        :type params: array
        :return: json string

        :example:

        >>> ocean.rpc.call("getblockcount")
        """
        if params == ():
            return self._ocean._conn.post(f"rpc/{method}", [])
        else:
            return self._ocean._conn.post(f"rpc/{method}", params)
