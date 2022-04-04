from ..util import BuildJson


class Wallet:
    def __init__(self, node):
        self.node = node

    def abandontransaction(self, txid):
        return self.node.rpc.call("abandontransaction", txid)

    def abortrescan(self):
        return self.node.rpc.call("abortrescan")

    def addmultisigaddress(self, nrequired, keys, label=None, address_type=None):
        label = "" if label is None else label
        return self.node.rpc.call("addmultisigaddress", nrequired, keys, label, address_type)

    def backupwallet(self, destination):
        return self.node.rpc.call("backupwallet", destination)

    def bumpfee(self, txid, confTarget=None, totalFee=None, replaceable=None, estimate_mode=None):
        options = BuildJson()
        options.append("confTarget", confTarget)
        options.append("totalFee", totalFee)
        options.append("replaceable", replaceable)
        options.append("estimate_mode", estimate_mode)
        return self.node.rpc.call("bumpfee", txid, options.build())

    def createwallet(self, wallet_name, disable_private_keys=None, blank=None, passphrase=None, avoid_reuse=None):
        disable_private_keys = False if disable_private_keys is None else disable_private_keys
        blank = False if blank is None else blank
        passphrase = "" if passphrase is None else passphrase
        return self.node.rpc.call("createwallet", wallet_name, disable_private_keys, blank, passphrase, avoid_reuse)

    def dumpprivkey(self, address):
        return self.node.rpc.call("dumpprivkey", address)

    def dumpwallet(self, filename):
        return self.node.rpc.call("dumpwallet", filename)

    def encryptwallet(self, passphrase):
        return self.node.rpc.call("encryptwallet", passphrase)

    def getaddressesbylabel(self, label):
        return self.node.rpc.call("getaddressesbylabel", label)

    def getaddressinfo(self, address):
        return self.node.rpc.call("getaddressinfo", address)

    def getbalance(self, dummy=None, minconf=None, include_watchonly=None, avoid_reuse=None, with_tokens=None):
        dummy = "*" if dummy is None else dummy
        minconf = 0 if minconf is None else minconf
        include_watchonly = True if include_watchonly is None else include_watchonly
        avoid_reuse = True if avoid_reuse is None else avoid_reuse
        return self.node.rpc.call("getbalance", dummy, minconf, include_watchonly, avoid_reuse, with_tokens)

    def getbalances(self, with_tokens=None):
        return self.node.rpc.call("getbalances", with_tokens)

    def getnewaddress(self, label, address_type):
        label = "" if label is None else label
        return self.node.rpc.call("getnewaddress", label, address_type)

