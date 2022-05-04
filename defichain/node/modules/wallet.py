from ..util import BuildJson


class Wallet:
    def __init__(self, node):
        self._node = node

    def abandontransaction(self, txid):  # 01
        return self._node._rpc.call("abandontransaction", txid)

    def abortrescan(self):  # 02
        return self._node._rpc.call("abortrescan")

    def addmultisigaddress(self, nrequired, keys, label="", address_type=None):  # 03
        return self._node._rpc.call("addmultisigaddress", nrequired, keys, label, address_type)

    def backupwallet(self, destination):  # 04
        return self._node._rpc.call("backupwallet", destination)

    def bumpfee(self, txid, confTarget=None, totalFee=None, replaceable=True, estimate_mode="UNSET"):  # 05
        options = BuildJson()
        options.append("confTarget", confTarget)
        options.append("totalFee", totalFee)
        options.append("replaceable", replaceable)
        options.append("estimate_mode", estimate_mode)
        return self._node._rpc.call("bumpfee", txid, options.build())

    def createwallet(self, wallet_name, disable_private_keys=False, blank=False, passphrase="", avoid_reuse=False):  # 06
        return self._node._rpc.call("createwallet", wallet_name, disable_private_keys, blank, passphrase, avoid_reuse)

    def dumpprivkey(self, address):  # 07
        return self._node._rpc.call("dumpprivkey", address)

    def dumpwallet(self, filename):  # 08
        return self._node._rpc.call("dumpwallet", filename)

    def encryptwallet(self, passphrase):  # 09
        return self._node._rpc.call("encryptwallet", passphrase)

    def getaddressesbylabel(self, label):  # 10
        return self._node._rpc.call("getaddressesbylabel", label)

    def getaddressinfo(self, address):  # 11
        return self._node._rpc.call("getaddressinfo", address)

    def getbalance(self, dummy="*", minconf=0, include_watchonly=True, avoid_reuse=True, with_tokens=False):  # 12
        return self._node._rpc.call("getbalance", dummy, minconf, include_watchonly, avoid_reuse, with_tokens)

    def getbalances(self, with_tokens=None):  # 13
        return self._node._rpc.call("getbalances", with_tokens)

    def getnewaddress(self, label="", address_type=None):  # 14
        return self._node._rpc.call("getnewaddress", label, address_type)

    def getrawchangeaddress(self, address_type=None):  # 15
        return self._node._rpc.call("getrawchangeaddress", address_type)

    def getreceivedbyaddress(self, address, minconf=1):  # 16
        return self._node._rpc.call("getreceivedbyaddress", address, minconf)

    def getreceivedbylabel(self, label, minconf=1):  # 17
        return self._node._rpc.call("getreceivedbylabel", label, minconf)

    def gettransaction(self, txid, include_watchonly=True):  # 18
        return self._node._rpc.call("gettransaction", txid, include_watchonly)

    def getunconfirmedbalance(self, with_tokens=False):  # 19
        return self._node._rpc.call("getunconfirmedbalance", with_tokens)

    def getwalletinfo(self, with_tokens=False):  # 20
        return self._node._rpc.call("getwalletinfo", with_tokens)

    def importaddress(self, address, label="", rescan=True, p2sh=False):  # 21
        return self._node._rpc.call("importaddress", address, label, rescan, p2sh)

    def importmulti(self, requests, rescan=True):  # 22
        options = BuildJson()
        options.append("rescan", rescan)
        return self._node._rpc.call("importmulti", requests, rescan)

    def importprivkey(self, privkey, label="", rescan=True):  # 23
        return self._node._rpc.call("importprivkey", privkey, label, rescan)

    def importprunedfunds(self, rawtransaction, txoutproof):  # 24
        return self._node._rpc.call("importprunedfunds", rawtransaction, txoutproof)

    def importpubkey(self, pubkey, label="", rescan=True):  # 25
        label = "" if label is None else label
        return self._node._rpc.call("importpubkey", pubkey, label, rescan)

    def importwallet(self, filename):  # 26
        return self._node._rpc.call("importwallet", filename)

    def keypoolrefill(self, newsize=100):  # 27
        return self._node._rpc.call("keypoolrefill", newsize)

    def listaddressgroupings(self):  # 28
        return self._node._rpc.call("listaddressgroupings")

    def listlabels(self, purpose=None):  # 29
        return self._node._rpc.call("listlabels", purpose)

    def listlockunspent(self):  # 30
        return self._node._rpc.call("listlockunspent")

    def listreceivedbyaddress(self, minconf=1, include_empty=False, include_watchonly=True, address_filter=None):  # 31
        return self._node._rpc.call("listreceivedbyaddress", minconf, include_empty, include_watchonly, address_filter)

    def listreceivedbylabel(self, minconf=1, include_empty=False, include_watchonly=True):  # 32
        return self._node._rpc.call("listreceivedbylabel", minconf, include_empty, include_watchonly)

    def listsinceblock(self, blockhash=None, target_confirmations=1, include_watchonly=True, include_removed=True):  # 33
        blockhash = "" if blockhash is None else blockhash
        target_confirmations = 1 if target_confirmations is None else target_confirmations
        include_watchonly = True if include_watchonly is None else include_watchonly
        return self._node._rpc.call("listsinceblock", blockhash, target_confirmations, include_watchonly, include_removed)

    def listtransactions(self, label="*", count=10, skip=0, include_watchonly=True, exclude_custom_tx=False):  # 34
        return self._node._rpc.call("listtransactions", label, count, skip, include_watchonly, exclude_custom_tx)

    def listunspent(self, mincof=1, maxcof=9999999, addresses=[], include_unsafe=True, minimumAmount=0,
                    maximumAmount=None, maximumCount=None, minimumSumAmount=None, tokenId=None):  # 35
        query_options = BuildJson()
        query_options.append("minimumAmount", minimumAmount)
        query_options.append("maximumAmount", maximumAmount)
        query_options.append("maximumCount", maximumCount)
        query_options.append("minimumSumAmount", minimumSumAmount)
        query_options.append("tokenId", tokenId)
        return self._node._rpc.call("listunspent", mincof, maxcof, addresses, include_unsafe, query_options.build())

    def listwalletdir(self):  # 36
        return self._node._rpc.call("listwalletdir")

    def listwallets(self):  # 37
        return self._node._rpc.call("listwallets")

    def loadwallet(self, filename):  # 38
        return self._node._rpc.call("loadwallet", filename)

    def lockunspent(self, unlock, transaction=None):  # 39
        return self._node._rpc.call("lockunspent", unlock, transaction)

    def removeprunedfunds(self, txid):  # 40
        return self._node._rpc.call("removeprunedfunds", txid)

    def rescanblockchain(self, start_height=0, stop_height=None):  # 41
        start_height = 0 if start_height is None else start_height
        return self._node._rpc.call("rescanblockchain", start_height, stop_height)

    def sendmany(self, dummy, amounts, minconf=1, comment="", subtractfeefrom=[], replaceable=False,
                 conf_target=1, estimate_mode="UNSET"):  # 42
        return self._node._rpc.call("sendmany", dummy, amounts, minconf, comment, subtractfeefrom, replaceable,
                                    conf_target, estimate_mode)

    def sendtoaddress(self, address, amount, comment="", comment_to="", subtractfeefromamount=False,
                      replaceable=False, conf_target=1, estimate_mode="UNSET", avoid_reuse=True):  # 43
        return self._node._rpc.call("sendtoaddress", address, amount, comment, comment_to, subtractfeefromamount,
                                    replaceable, conf_target, estimate_mode, avoid_reuse)

    def sethdseed(self, newkeypool=True, seed=None):  # 44
        return self._node._rpc.call("sethdseed", newkeypool, seed)

    def setlabel(self, address, label):  # 45
        return self._node._rpc.call("setlabel", address, label)

    def settxfee(self, amount):  # 46
        return self._node._rpc.call("settxfee", amount)

    def setwalletflag(self, flag, value):  # 47
        return self._node._rpc.call("setwalletflag", flag, value)

    def signmessage(self, address, message):  # 48
        return self._node._rpc.call("signmessage", address, message)

    def signrawtransactionwithwallet(self, hexstring, prevtxs=[], sighashtype="ALL"):  # 49
        return self._node._rpc.call("signrawtransactionwithwallet", hexstring, prevtxs, sighashtype)

    def unloadwallet(self, wallet_name=None):  # 50
        return self._node._rpc.call("unloadwallet", wallet_name)

    def walletcreatefundedpsbt(self, inputs, outputs, locktime=0, changeAddress=None, changePosition=None,
                               change_type=None, includeWatching=True, lockUnspents=False, feeRate=None,
                               subtractFeeFromOutputs=None, replaceable=None, conf_target=None, estimate_mode=None,
                               bip32derivs=False):  # 51
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
        return self._node._rpc.call("walletcreatefundedpsbt", inputs, outputs, locktime, options.build(), bip32derivs)

    def walletlock(self):  # 52
        return self._node._rpc.call("walletlock")

    def walletpassphrase(self, passphrase, timeout):  # 53
        return self._node._rpc.call("walletpassphrase", passphrase, timeout)

    def walletpassphrasechange(self, oldpassphrase, newpassphrase):  # 54
        return self._node._rpc.call("walletpassphrasechange", oldpassphrase, newpassphrase)

    def walletprocesspsbt(self, psbt, sign=True, sighashtype="ALL", bip32derivs=False):  # 55
        return self._node._rpc.call("walletprocesspsbt", psbt, sign, sighashtype, bip32derivs)
