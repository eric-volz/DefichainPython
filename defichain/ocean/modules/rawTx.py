# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/RawTx.ts

class RawTx:
    def __init__(self, ocean):
        self._ocean = ocean

    def send(self, rawTx):
        return self._ocean._conn.post("rawtx/send", [rawTx])

    def test(self, rawTx):
        return self._ocean._conn.post("rawtx/test", [rawTx])
