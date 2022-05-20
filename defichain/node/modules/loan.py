from ..util import BuildJson


class Loan:
    def __init__(self, node):
        self._node = node

    def createloanscheme(self, mincolratio, interestrate, id, inputs=None):  # 01
        return self._node._rpc.call("createloanscheme", mincolratio, interestrate, id, inputs)

    def destroyloanscheme(self, id, ACTIVATE_AFTER_BLOCK=None, inputs=None):  # 02
        ACTIVATE_AFTER_BLOCK = self._node.blockchain.getblockcount() + 1 if ACTIVATE_AFTER_BLOCK is None else ACTIVATE_AFTER_BLOCK
        return self._node._rpc.call("destroyloanscheme", id, ACTIVATE_AFTER_BLOCK, inputs)

    def getcollateraltoken(self, token):  # 03
        return self._node._rpc.call("getcollateraltoken", token)

    def getinterest(self, id, token=""):  # 04
        return self._node._rpc.call("getinterest", id, token)

    def getloaninfo(self):  # 05
        return self._node._rpc.call("getloaninfo")

    def getloanscheme(self, id):  # 06
        return self._node._rpc.call("getloanscheme", id)

    def getloantoken(self, token):  # 07
        return self._node._rpc.call("getloantoken", token)

    def listcollateraltokens(self, height=None, all=None):  # 08
        by = BuildJson()
        by.append("height", height)
        by.append("all", all)
        return self._node._rpc.call("listcollateraltokens", by.build())

    def listloanschemes(self):  # 09
        return self._node._rpc.call("listloanschemes")

    def listloantokens(self):  # 10
        return self._node._rpc.call("listloantokens")

    def paybackloan(self, vaultId, _from, amounts=None, loans=None, inputs=None):  # 11
        metadata = BuildJson()
        metadata.append("vaultId", vaultId)
        metadata.append("from", _from)
        metadata.append("amounts", amounts)
        metadata.append("loans", loans)

        return self._node._rpc.call("paybackloan", metadata.build(), inputs)

    def setcollateraltoken(self, token, factor, fixedIntervalPriceId, activateAfterBlock=None, inputs=None):  # 12
        metadata = BuildJson()
        metadata.append("token", token)
        metadata.append("factor", factor)
        metadata.append("fixedIntervalPriceId", fixedIntervalPriceId)
        metadata.append("activateAfterBlock", activateAfterBlock)
        return self._node._rpc.call("setcollateraltoken", metadata.build(), inputs)

    def setdefaultloanscheme(self, id, inputs=None):  # 13
        return self._node._rpc.call("setdefaultloanscheme", id, inputs)

    def setloantoken(self, symbol, fixedIntervalPriceId, name=None, mintable=True, interest=0, inputs=None):  # 14
        metadata = BuildJson()
        metadata.append("symbol", symbol)
        metadata.append("name", name)
        metadata.append("fixedIntervalPriceId", fixedIntervalPriceId)
        metadata.append("mintable", mintable)
        metadata.append("interest", interest)
        return self._node._rpc.call("setloantoken", metadata.build(), inputs)

    def takeloan(self, vaultId, amounts, to=None, inputs=None):  # 15
        metadata = BuildJson()
        metadata.append("vaultId", vaultId)
        metadata.append("to", to)
        metadata.append("amounts", amounts)
        return self._node._rpc.call("takeloan", metadata.build(), inputs)

    def updateloanscheme(self, mincolratio, interestrate, id, ACTIVATE_AFTER_BLOCK=None, inputs=None):  # 16
        ACTIVATE_AFTER_BLOCK = self._node.blockchain.getblockcount() + 1 if ACTIVATE_AFTER_BLOCK is None else ACTIVATE_AFTER_BLOCK
        return self._node._rpc.call("updateloanscheme", mincolratio, interestrate, id, ACTIVATE_AFTER_BLOCK, inputs)

    def updateloantoken(self, token, symbol=None, name=None, fixedIntervalPriceId=None, mintable=True, interest=None, inputs=None):  # 17
        metadata = BuildJson()
        metadata.append("symbol", symbol)
        metadata.append("name", name)
        metadata.append("fixedIntervalPriceId", fixedIntervalPriceId)
        metadata.append("mintable", mintable)
        metadata.append("interest", interest)
        return self._node._rpc.call("updateloantoken", token, metadata.build(), inputs)
