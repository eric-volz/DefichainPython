from ..util import BuildJson


class Wallet:
    def __init__(self, node):
        self.node = node

    def abandontransaction(self, txid):  # 01
        return self.node._rpc.call("abandontransaction", txid)

    def abortrescan(self):  # 02
        return self.node._rpc.call("abortrescan")

    def addmultisigaddress(self, nrequired, keys, label=None, address_type=None):  # 03
        label = "" if label is None else label
        return self.node._rpc.call("addmultisigaddress", nrequired, keys, label, address_type)

    def backupwallet(self, destination):  # 04
        return self.node._rpc.call("backupwallet", destination)

    def bumpfee(self, txid, confTarget=None, totalFee=None, replaceable=None, estimate_mode=None):  # 05
        options = BuildJson()
        options.append("confTarget", confTarget)
        options.append("totalFee", totalFee)
        options.append("replaceable", replaceable)
        options.append("estimate_mode", estimate_mode)
        return self.node._rpc.call("bumpfee", txid, options.build())

    def createwallet(self, wallet_name, disable_private_keys=None, blank=None, passphrase=None, avoid_reuse=None):  # 06
        disable_private_keys = False if disable_private_keys is None else disable_private_keys
        blank = False if blank is None else blank
        passphrase = "" if passphrase is None else passphrase
        return self.node._rpc.call("createwallet", wallet_name, disable_private_keys, blank, passphrase, avoid_reuse)

    def dumpprivkey(self, address):  # 07
        return self.node._rpc.call("dumpprivkey", address)

    def dumpwallet(self, filename):  # 08
        return self.node._rpc.call("dumpwallet", filename)

    def encryptwallet(self, passphrase):  # 09
        return self.node._rpc.call("encryptwallet", passphrase)

    def getaddressesbylabel(self, label):  # 10
        return self.node._rpc.call("getaddressesbylabel", label)

    def getaddressinfo(self, address):  # 11
        return self.node._rpc.call("getaddressinfo", address)

    def getbalance(self, dummy=None, minconf=None, include_watchonly=None, avoid_reuse=None, with_tokens=None):  # 12
        dummy = "*" if dummy is None else dummy
        minconf = 0 if minconf is None else minconf
        include_watchonly = True if include_watchonly is None else include_watchonly
        avoid_reuse = True if avoid_reuse is None else avoid_reuse
        return self.node._rpc.call("getbalance", dummy, minconf, include_watchonly, avoid_reuse, with_tokens)

    def getbalances(self, with_tokens=None):  # 13
        return self.node._rpc.call("getbalances", with_tokens)

    def getnewaddress(self, label, address_type):  # 14
        label = "" if label is None else label
        return self.node._rpc.call("getnewaddress", label, address_type)

    def getrawchangeaddress(self, address_type=None):  # 15
        return self.node._rpc.call("getrawchangeaddress", address_type)

    def getreceivedbyaddress(self, address, minconf=None):  # 16
        return self.node._rpc.call("getreceivedbyaddress", address, minconf)

    def getreceivedbylabel(self, label, minconf=None):  # 17
        return self.node._rpc.call("getreceivedbylabel", label, minconf)

    def gettransaction(self, txid, include_watchonly=None):  # 18
        return self.node._rpc.call("gettransaction", txid, include_watchonly)

    def getunconfirmedbalance(self, with_tokens=None):  # 19
        return self.node._rpc.call("getunconfirmedbalance", with_tokens)

    def getwalletinfo(self, with_tokens=None):  # 20
        return self.node._rpc.call("getwalletinfo", with_tokens)

    def importaddress(self, address, label=None, rescan=None, p2sh=None):  # 21
        label = "" if label is None else label
        rescan = True if rescan is None else rescan
        return self.node._rpc.call("importaddress", address, label, rescan, p2sh)

    def importmulti(self, requests, rescan=None):  # 22
        options = BuildJson()
        options.append("rescan", rescan)
        return self.node._rpc.call("importmulti", requests, rescan)

    def importprivkey(self, privkey, label=None, rescan=None):  # 23
        label = "" if label is None else label
        return self.node._rpc.call("importprivkey", privkey, label, rescan)

    def importprunedfunds(self, rawtransaction, txoutproof):  # 24
        return self.node._rpc.call("importprunedfunds", rawtransaction, txoutproof)

    def importpubkey(self, pubkey, label=None, rescan=None):  # 25
        label = "" if label is None else label
        return self.node._rpc.call("importpubkey", pubkey, label, rescan)

    def importwallet(self, filename):  # 26
        return self.node._rpc.call("importwallet", filename)

    def keypoolrefill(self, newsize=None):  # 27
        return self.node._rpc.call("keypoolrefill", newsize)

    def listaddressgroupings(self):  # 28
        return self.node._rpc.call("listaddressgroupings")

    def listlabels(self, purpose=None):  # 29
        return self.node._rpc.call("listlabels", purpose)

    def listlockunspent(self):  # 30
        return self.node._rpc.call("listlockunspent")

    def listreceivedbyaddress(self, minconf=None, include_empty=None, include_watchonly=None, address_filter=None):  # 31
        minconf = 1 if minconf is None else minconf
        include_empty = False if include_empty is None else include_empty
        include_watchonly = True if include_watchonly is None else include_watchonly
        return self.node._rpc.call("listreceivedbyaddress", minconf, include_empty, include_watchonly, address_filter)

    def listreceivedbylabel(self, minconf=None, include_empty=None, include_watchonly=None):  # 32
        minconf = 1 if minconf is None else minconf
        include_empty = False if include_empty is None else include_empty
        include_watchonly = True if include_watchonly is None else include_watchonly
        return self.node._rpc.call("listreceivedbylabel", minconf, include_empty, include_watchonly)

    def listsinceblock(self, blockhash=None, target_confirmations=None, include_watchonly=None, include_removed=None):  # 33
        blockhash = "" if blockhash is None else blockhash
        target_confirmations = 1 if target_confirmations is None else target_confirmations
        include_watchonly = True if include_watchonly is None else include_watchonly
        return self.node._rpc.call("listsinceblock", blockhash, target_confirmations, include_watchonly, include_removed)

    def listtransactions(self, label=None, count=None, skip=None, include_watchonly=None, exclude_custom_tx=None):  # 34
        label = "*" if label is None else label
        count = 10 if count is None else count
        skip = 0 if skip is None else skip
        include_watchonly = True if include_watchonly is None else include_watchonly
        return self.node._rpc.call("listtransactions", label, count, skip, include_watchonly, exclude_custom_tx)

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
        return self.node._rpc.call("listunspent", mincof, maxcof, addresses, include_unsafe, query_options.build())

    def listwalletdir(self):  # 36
        return self.node._rpc.call("listwalletdir")

    def listwallets(self):  # 37
        return self.node._rpc.call("listwallets")

    def loadwallet(self, filename):  # 38
        return self.node._rpc.call("loadwallet", filename)

    def lockunspent(self, unlock, transaction=None):  # 39
        return self.node._rpc.call("lockunspent", unlock, transaction)

    def removeprunedfunds(self, txid):  # 40
        return self.node._rpc.call("removeprunedfunds", txid)

    def rescanblockchain(self, start_height=None, stop_height=None):  # 41
        start_height = 0 if start_height is None else start_height
        return self.node._rpc.call("rescanblockchain", start_height, stop_height)

    def sendmany(self, dummy, amounts, minconf=None, comment=None, subtractfeefrom=None, replaceable=None,
                 conf_target=None, estimate_mode=None):  # 42
        minconf = 1 if minconf is None else minconf
        comment = "" if comment is None else comment
        subtractfeefrom = [] if subtractfeefrom is None else subtractfeefrom
        replaceable = False if replaceable is None else replaceable
        conf_target = 1 if conf_target is None else conf_target
        return self.node._rpc.call("sendmany", dummy, amounts, minconf, comment, subtractfeefrom, replaceable,
                                   conf_target, estimate_mode)

    def sendtoaddress(self, address, amount, comment=None, comment_to=None, subtractfeefromamount=None,
                      replaceable=None, conf_target=None, estimate_mode=None, avoid_reuse=None):  # 43
        comment = "" if comment is None else comment
        comment_to = "" if comment_to is None else comment_to
        subtractfeefromamount = False if subtractfeefromamount is None else subtractfeefromamount
        replaceable = False if replaceable is None else replaceable
        conf_target = 1 if conf_target is None else conf_target
        estimate_mode = "UNSET" if estimate_mode is None else estimate_mode
        return self.node._rpc.call("sendtoaddress", address, amount, comment, comment_to, subtractfeefromamount,
                                   replaceable, conf_target, estimate_mode, avoid_reuse)

    def sethdseed(self, newkeypool=None, seed=None):  # 44
        newkeypool = True if newkeypool is None else newkeypool
        return self.node._rpc.call("sethdseed", newkeypool, seed)

    def setlabel(self, address, label):  # 45
        return self.node._rpc.call("setlabel", address, label)

    def settxfee(self, amount):  # 46
        return self.node._rpc.call("settxfee", amount)

    def setwalletflag(self, flag, value):  # 47
        return self.node._rpc.call("setwalletflag", flag, value)

    def signmessage(self, address, message):  # 48
        return self.node._rpc.call("signmessage", address, message)

    def signrawtransactionwithwallet(self, hexstring, prevtxs=None, sighashtype=None):  # 49
        prevtxs = [] if prevtxs is None else prevtxs
        return self.node._rpc.call("signrawtransactionwithwallet", hexstring, prevtxs, sighashtype)

    def unloadwallet(self, wallet_name=None):  # 50
        return self.node._rpc.call("unloadwallet", wallet_name)

    def walletcreatefundedpsbt(self, inputs, outputs, locktime=None, changeAddress=None, changePosition=None,
                               change_type=None, includeWatching=None, lockUnspents=None, feeRate=None,
                               subtractFeeFromOutputs=None, replaceable=None, conf_target=None, estimate_mode=None,
                               bip32derivs=None):  # 51
        locktime = 0 if locktime is None else locktime
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
        return self.node._rpc.call("walletcreatefundedpsbt", inputs, outputs, locktime, options.build(), bip32derivs)

    def walletlock(self):  # 52
        return self.node._rpc.call("walletlock")

    def walletpassphrase(self, passphrase, timeout):  # 53
        return self.node._rpc.call("walletpassphrase", passphrase, timeout)

    def walletpassphrasechange(self, oldpassphrase, newpassphrase):  # 54
        return self.node._rpc.call("walletpassphrasechange", oldpassphrase, newpassphrase)

    def walletprocesspsbt(self, psbt, sign=None, sighashtype=None, bip32derivs=None):  # 55
        sign = True if sign is None else sign
        sighashtype = "ALL" if sighashtype is None else sighashtype
        return self.node._rpc.call("walletprocesspsbt", psbt, sign, sighashtype, bip32derivs)
