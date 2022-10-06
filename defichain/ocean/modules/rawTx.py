# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/RawTx.ts
import json
from defichain.node.util import BuildJson


class RawTx:
    def __init__(self, ocean):
        self._ocean = ocean

    def send(self, hex: str, maxFeeRate: float = None) -> str:
        """
        Send a raw transaction

        :param hex: (required) rawTx to submit to the network
        :type hex: str
        :param maxFeeRate: (optional) maximum fee rate
        :type maxFeeRate: float
        :return: "txid" (string)

        :example:

        >>> ocean.rawTx.send("hex")
        """
        j = BuildJson()
        j.append("hex", hex)
        j.append("maxFeeRate", maxFeeRate)
        return self._ocean._conn.post("rawtx/send", json.dumps(j.build()))

    def test(self, hex: str, maxFeeRate: float = None):
        """
        Send a raw transaction to test the mempool acceptance

        :param hex: (required) rawTx to submit to the network
        :type hex: str
        :param maxFeeRate: (optional) maximum fee rate
        :type maxFeeRate: float

        :example:

        >>> ocean.rawTx.test("hex")
        """
        j = BuildJson()
        j.append("hex", hex)
        j.append("maxFeeRate", maxFeeRate)
        return self._ocean._conn.post("rawtx/test", json.dumps(j.build()))
