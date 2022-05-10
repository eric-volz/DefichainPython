# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/RawTx.ts
import json
from defichain.node.util import BuildJson


class RawTx:
    def __init__(self, ocean):
        self._ocean = ocean

    def send(self, hex, maxFeeRate=None):
        j = BuildJson()
        j.append("hex", hex)
        j.append("maxFeeRate", maxFeeRate)
        return self._ocean._conn.post("rawtx/send", json.dumps(j.build()))

    def test(self, hex, maxFeeRate=None):
        j = BuildJson()
        j.append("hex", hex)
        j.append("maxFeeRate", maxFeeRate)
        return self._ocean._conn.post("rawtx/test", json.dumps(j.build()))
