# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Rpc.ts

class Rpc:
    def __init__(self, ocean):
        self._ocean = ocean

    def call(self, method, *params):
        if params == ():
            return self._ocean._conn.post(f"rpc/{method}", [])
        else:
            return self._ocean._conn.post(f"rpc/{method}", params)
