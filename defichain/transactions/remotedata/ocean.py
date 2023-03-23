from .remotedata import RemoteData
from defichain import Ocean


class RemoteDataOcean(RemoteData):

    def __init__(self, source: Ocean):
        self.ocean = source

    def get_unspent(self, address: str) -> [{}]:
        data = self.ocean.address.listTransactionUnspent(address, 200)["data"]
        unspent = []
        for u in data:
            txid = u["vout"]["txid"]
            index = u["vout"]["n"]
            value = int(round(float(u["vout"]["value"]) * 100000000))
            script = u["script"]["hex"]
            unspent.append({"txid": txid, "vout": index, "value": value, "scriptPubKey": script})
        return unspent

    def test_tx(self, hex: str, maxFeeRate: float = None) -> bool:
        try:
            self.ocean.rawTx.test(hex, maxFeeRate)
            return True
        except:
            return False

    def send_tx(self, hex: str, maxFeeRate: float = None) -> str:
        result = self.ocean.rawTx.send(hex, maxFeeRate)
        if "data" in result:
            return result["data"]
        else:
            return result

