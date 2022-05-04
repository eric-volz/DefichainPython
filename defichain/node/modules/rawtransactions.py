from ..util import BuildJson


class Rawtransactions:
    def __init__(self, node):
        self._node = node

    def analyzepsbt(self, psbt):  # 01
        return self._node._rpc.call("analyzepsbt", psbt)

    def combinepsbt(self, txs):  # 02
        return self._node._rpc.call("combinepsbt", txs)

    def combinerawtransaction(self, txs):  # 03
        return self._node._rpc.call("combinerawtransaction", txs)

    def converttopsbt(self, hexstring, permitsigdata=False, iswitness=None):  # 04
        return self._node._rpc.call("converttopsbt", hexstring, permitsigdata, iswitness)

    def createpsbt(self, inputs, outputs, locktime=0, replaceable=False):  # 05
        return self._node._rpc.call("createpsbt", inputs, outputs, locktime, replaceable)

    def createrawtransaction(self, inputs, outputs, locktime=0, replaceable=False):  # 06
        return self._node._rpc.call("createrawtransaction", inputs, outputs, locktime, replaceable)

    def decodepsbt(self, psbt):  # 07
        return self._node._rpc.call("decodepsbt", psbt)

    def decoderawtransaction(self, hexstring, iswitness=None):  # 08
        return self._node._rpc.call("decoderawtransaction", hexstring, iswitness)

    def decodescript(self, hexstring):  # 09
        return self._node._rpc.call("decodescript", hexstring)

    def finalizepsbt(self, psbt, extract=True):  # 10
        return self._node._rpc.call("finalizepsbt", psbt, extract)

    def fundrawtransaction(self, hexstring, changeAddress=None, changePosition=None, change_type=None,
                           includeWatching=True, lockUnspents=False, feeRate=None, subtractFeeFromOutputs=None,
                           replaceable=None, conf_target=None, estimate_mode=None, iswitness=None):  # 11
        options = BuildJson()
        options.append("changeAddress", changeAddress)
        options.append("changePosition", changePosition)
        options.append("change_type", change_type)
        options.append("includeWatching", includeWatching)
        options.append("lockUnspents", lockUnspents)
        options.append("feeRate", feeRate)
        options.append("subtractFeeFromOutputs", subtractFeeFromOutputs)
        options.append("replaceable", replaceable)
        options.append("conf_target", conf_target)
        options.append("estimate_mode", estimate_mode)
        return self._node._rpc.call("fundrawtransaction", hexstring, options.build(), iswitness)

    def getrawtransaction(self, txid, verbose=False, blockhash=None):  # 12
        verbose = False if verbose is None else verbose
        return self._node._rpc.call("getrawtransaction", txid, verbose, blockhash)

    def joinpsbts(self, txs):  # 13
        return self._node._rpc.call("joinpsbts", txs)

    def sendrawtransaction(self, hexstring, maxfeerate=0.10):  # 14
        return self._node._rpc.call("sendrawtransaction", hexstring, maxfeerate)

    def signrawtransactionwithkey(self, hexstring, privatekey, prevtxs=None, sighashtype="ALL"):  # 15
        prevtxs = [] if prevtxs is None else prevtxs
        return self._node._rpc.call("signrawtransactionwithkey", hexstring, privatekey, prevtxs, sighashtype)

    def testmempoolaccept(self, rawtxs, maxfeerate=0.10):  # 16
        return self._node._rpc.call("testmempoolaccept", rawtxs, maxfeerate)

    def utxoupdatepsbt(self, psbt, descriptors=None):  # 17
        return self._node._rpc.call("utxoupdatepsbt", psbt, descriptors)
