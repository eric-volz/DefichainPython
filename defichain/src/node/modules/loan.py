from ..util import BuildJson


class Loan:
    def __init__(self, node):
        self.node = node

    def createloanscheme(self, mincolratio, interestrate, id, inputs=None):  # 01
        return self.node.rpc.call("createloanscheme", mincolratio, interestrate, id, inputs)

    def destroyloanscheme(self, id, ACTIVATE_AFTER_BLOCK=None, inputs=None):  # 02
        ACTIVATE_AFTER_BLOCK = self.node.blockchain.getblockcount() + 1 if ACTIVATE_AFTER_BLOCK is None else ACTIVATE_AFTER_BLOCK
        return self.node.rpc.call("destroyloanscheme", id, ACTIVATE_AFTER_BLOCK, inputs)

    def getcollateraltoken(self, token):  # 03
        return self.node.rpc.call("getcollateraltoken", token)

    def getinterest(self, id, token=None):  # 04
        return self.node.rpc.call("getinterest", id, token)

    def getloaninfo(self):  # 05
        return self.node.rpc.call("getloaninfo")

    def getloanscheme(self, id):  # 06
        return self.node.rpc.call("getloanscheme", id)

    def getloantoken(self, token):  # 07
        return self.node.rpc.call("getloantoken", token)

    def listcollateraltokens(self, by=None):  # 08
        return self.node.rpc.call("listcollateraltokens", by)

    def listloanschemes(self):  # 09
        return self.node.rpc.call("listloanschemes")

    def listloantokens(self):  # 10
        return self.node.rpc.call("listloantokens")

    def paybackloan(self, vaultId, _from, token, amount, inputs=None):  # 11
        metadata = BuildJson()
        metadata.append("vaultId", vaultId)
        metadata.append("from", _from)
        metadata.append("amounts", f"{amount}@{token}")

        return self.node.rpc.call("paybackloan", metadata.build(), inputs)
