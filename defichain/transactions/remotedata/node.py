from defichain.exceptions.transactions import TxBuilderError
from .remotedata import RemoteData
from defichain import Node


class RemoteDataNode(RemoteData):
    def __init__(self, source: Node):
        self.node = source

    def get_unspent(self, address: str) -> [{}]:
        # Check if address is indexed by node / wallet
        if not self.node.wallet.getaddressinfo(address)["labels"]:
            error_string = f"To build a raw transaction from the given address: {address} the node needs to index " \
                           f"the address first.\nYou can use the 'importaddress' method form your node for that."
            raise TxBuilderError(error_string)

        data = self.node.wallet.listunspent(addresses=[address])
        unspent = []
        for u in data:
            txid = u["txid"]
            index = u["vout"]
            value = int(round(float(u["amount"]) * 100000000))
            script = u["scriptPubKey"]
            unspent.append({"txid": txid, "vout": index, "value": value, "scriptPubKey": script})
        return unspent

    def test_tx(self, hex: str, maxFeeRate: float = None) -> bool:
        try:
            self.node.rawtransactions.testmempoolaccept([hex], maxFeeRate)
            return True
        except:
            return False

    def send_tx(self, hex: str, maxFeeRate: float = None) -> str:
        return self.node.rawtransactions.sendrawtransaction(hex, maxFeeRate)
