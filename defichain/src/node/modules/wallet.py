from ..util import BuildJson


class Wallet:
    def __init__(self, node):
        self.node = node

    def abandontransaction(self, txid):  # 01
        return self.node.rpc.call("abandontransaction", txid)

    def abortrescan(self):  # 02
        return self.node.rpc.call("abortrescan")

    def addmultisigaddress(self, nrequired, keys, label=None, address_type=None):  # 03
        label = "" if label is None else label
        return self.node.rpc.call("addmultisigaddress", nrequired, keys, label, address_type)

    def backupwallet(self, destination):  # 04
        return self.node.rpc.call("backupwallet", destination)

    def bumpfee(self, txid, confTarget=None, totalFee=None, replaceable=None, estimate_mode=None):  # 05
        options = BuildJson()
        options.append("confTarget", confTarget)
        options.append("totalFee", totalFee)
        options.append("replaceable", replaceable)
        options.append("estimate_mode", estimate_mode)
        return self.node.rpc.call("bumpfee", txid, options.build())

    def createwallet(self, wallet_name, disable_private_keys=None, blank=None, passphrase=None, avoid_reuse=None):  # 06
        disable_private_keys = False if disable_private_keys is None else disable_private_keys
        blank = False if blank is None else blank
        passphrase = "" if passphrase is None else passphrase
        return self.node.rpc.call("createwallet", wallet_name, disable_private_keys, blank, passphrase, avoid_reuse)

    def dumpprivkey(self, address):  # 07
        return self.node.rpc.call("dumpprivkey", address)

    def dumpwallet(self, filename):  # 08
        return self.node.rpc.call("dumpwallet", filename)

    def encryptwallet(self, passphrase):  # 09
        return self.node.rpc.call("encryptwallet", passphrase)

    def getaddressesbylabel(self, label):  # 10
        return self.node.rpc.call("getaddressesbylabel", label)

    def getaddressinfo(self, address):  # 11
        return self.node.rpc.call("getaddressinfo", address)

    def getbalance(self, dummy=None, minconf=None, include_watchonly=None, avoid_reuse=None, with_tokens=None):  # 12
        dummy = "*" if dummy is None else dummy
        minconf = 0 if minconf is None else minconf
        include_watchonly = True if include_watchonly is None else include_watchonly
        avoid_reuse = True if avoid_reuse is None else avoid_reuse
        return self.node.rpc.call("getbalance", dummy, minconf, include_watchonly, avoid_reuse, with_tokens)

    def getbalances(self, with_tokens=None):  # 13
        return self.node.rpc.call("getbalances", with_tokens)

    def getnewaddress(self, label, address_type):  # 14
        label = "" if label is None else label
        return self.node.rpc.call("getnewaddress", label, address_type)

    def getrawchangeaddress(self, address_type=None):  # 15
        return self.node.rpc.call("getrawchangeaddress", address_type)

    def getreceivedbyaddress(self, address, minconf=None):  # 16
        return self.node.rpc.call("getreceivedbyaddress", address, minconf)

    def getreceivedbylabel(self, label, minconf=None):  # 17
        return self.node.rpc.call("getreceivedbylabel", label, minconf)

    def gettransaction(self, txid, include_watchonly=None):  # 18
        return self.node.rpc.call("gettransaction", txid, include_watchonly)

    def getunconfirmedbalance(self, with_tokens=None):  # 19
        return self.node.rpc.call("getunconfirmedbalance", with_tokens)

    def getwalletinfo(self, with_tokens=None):  # 20
        return self.node.rpc.call("getwalletinfo", with_tokens)

    def importaddress(self, address, label=None, rescan=None, p2sh=None):  # 21
        label = "" if label is None else label
        rescan = True if rescan is None else rescan
        return self.node.rpc.call("importaddress", address, label, rescan, p2sh)

    def importmulti(self, requests, rescan=None):  # 22
        options = BuildJson()
        options.append("rescan", rescan)
        return self.node.rpc.call("importmulti", requests, rescan)

    def importprivkey(self, privkey, label=None, rescan=None):  # 23
        label = "" if label is None else label
        return self.node.rpc.call("importprivkey", privkey, label, rescan)

    def importprunedfunds(self, rawtransaction, txoutproof):  # 24
        return self.node.rpc.call("importprunedfunds", rawtransaction, txoutproof)

    def importpubkey(self, pubkey, label=None, rescan=None):  # 25
        label = "" if label is None else label
        return self.node.rpc.call("importpubkey", pubkey, label, rescan)

    def importwallet(self, filename):  # 26
        return self.node.rpc.call("importwallet", filename)

    def keypoolrefill(self, newsize=None):  # 27
        return self.node.rpc.call("keypoolrefill", newsize)

    def listaddressgroupings(self):  # 28
        return self.node.rpc.call("listaddressgroupings")

    def listlabels(self, purpose=None):  # 29
        return self.node.rpc.call("listlabels", purpose)

    def listlockunspent(self):  # 30
        return self.node.rpc.call("listlockunspent")

    def listreceivedbyaddress(self, minconf=None, include_empty=None, include_watchonly=None, address_filter=None):  # 31
        minconf = 1 if minconf is None else minconf
        include_empty = False if include_empty is None else include_empty
        include_watchonly = True if include_watchonly is None else include_watchonly
        return self.node.rpc.call("listreceivedbyaddress", minconf, include_empty, include_watchonly, address_filter)

    def listreceivedbylabel(self, minconf=None, include_empty=None, include_watchonly=None):  # 32
        minconf = 1 if minconf is None else minconf
        include_empty = False if include_empty is None else include_empty
        include_watchonly = True if include_watchonly is None else include_watchonly
        return self.node.rpc.call("listreceivedbylabel", minconf, include_empty, include_watchonly)

    def listsinceblock(self, blockhash=None, target_confirmations=None, include_watchonly=None, include_removed=None):  # 33
        blockhash = "" if blockhash is None else blockhash
        target_confirmations = 1 if target_confirmations is None else target_confirmations
        include_watchonly = True if include_watchonly is None else include_watchonly
        return self.node.rpc.call("listsinceblock", blockhash, target_confirmations, include_watchonly, include_removed)

    def listtransactions(self, label=None, count=None, skip=None, include_watchonly=None, exclude_custom_tx=None):  # 34
        label = "*" if label is None else label
        count = 10 if count is None else count
        skip = 0 if skip is None else skip
        include_watchonly = True if include_watchonly is None else include_watchonly
        return self.node.rpc.call("listtransactions", label, count, skip, include_watchonly, exclude_custom_tx)

    def listunspent(self, mincof=None, maxcof=None, addresses=None, include_unsafe=None, minimumAmount=None,
                    maximumAmount=None, maximumCount=None, minimumSumAmount=None, tokenId=None):  # 35
        mincof = 1 if mincof is None else mincof
        maxcof = 9999999 if maxcof is None else maxcof
        addresses = [] if addresses is None else addresses
        include_unsafe = True if include_unsafe is None else include_unsafe
        query_options = BuildJson()
        query_options.append("minimumAmount", minimumAmount)
        query_options.append("maximumAmount", maximumAmount)
        query_options.append("maximumCount", maximumCount)
        query_options.append("minimumSumAmount", minimumSumAmount)
        query_options.append("tokenId", tokenId)
        return self.node.rpc.call("listunspent", mincof, maxcof, addresses, include_unsafe, query_options.build())

    def listwalletdir(self):  # 36
        return self.node.rpc.call("listwalletdir")

    def listwallets(self):  # 37
        return self.node.rpc.call("listwallets")

    def loadwallet(self, filename):  # 38
        return self.node.rpc.call("loadwallet", filename)

    def lockunspent(self):  # 39
        pass

    def removeprunedfunds(self):  # 40
        pass

    def rescanblockchain(self):  # 41
        pass

    def sendmany(self):  # 42
        pass

    def sendtoaddress(self):  # 43
        pass

    def sethdseed(self):  # 44
        pass

    def setlabel(self):  # 45
        pass

    def settxfee(self):  # 46
        pass

    def setwalletflag(self):  # 47
        pass

    def signmessage(self):  # 48
        pass

    def signrawtransactionwithwallet(self):  # 49
        pass

    def unloadwallet(self):  # 50
        pass

    def walletcreatefundedpsbt(self):  # 51
        pass

    def walletlock(self):  # 52
        pass

    def walletpassphrase(self):  # 53
        pass

    def walletpassphrasechange(self):  # 54
        pass

    def walletprocesspsbt(self):  # 55
        pass
