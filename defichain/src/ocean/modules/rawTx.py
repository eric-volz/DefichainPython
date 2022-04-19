# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/RawTx.ts

class RawTx:
    def __init__(self, ocean):
        self.ocean = ocean

    def send(self, rawTx):
        return self.ocean._conn.post("rawtx/send", [rawTx])

    def test(self, rawTx):
        return self.ocean._conn.post("rawtx/test", [rawTx])
