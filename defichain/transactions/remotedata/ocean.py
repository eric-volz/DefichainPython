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
            value = int(float(u["vout"]["value"]) * 100000000)
            script_type = u["script"]["type"]
            script = u["script"]["hex"]
            unspent.append({"txid": txid, "index": index, "value": value, "script_type": script_type, "script": script})
        return unspent

    def test_tx(self, hex: str, maxFeeRate: int = None) -> bool:
        try:
            self.ocean.rawTx.test(hex, maxFeeRate)
            return True
        except:
            return False

    def send_tx(self, hex: str, maxFeeRate: int = None) -> str:
        return self.ocean.rawTx.send(hex, maxFeeRate)["data"]

