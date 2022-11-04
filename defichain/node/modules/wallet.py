from ..util import BuildJson


class Wallet:
    def __init__(self, node):
        self._node = node

    def abandontransaction(self, txid: str) -> None:  # 01
        """
        Mark in-wallet transaction as abandoned

        This will mark this transaction and all its in-wallet descendants as abandoned which will allow
        for their inputs to be respent.  It can be used to replace "stuck" or evicted transactions.

        It only works on transactions which are not included in a block and are not currently in the mempool.

        It has no effect on transactions which are already abandoned.

        :param txid: (required) The transaction id
        :type txid: str
        :return: None

        :example:

            >>> node.wallet.abandontransaction("1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d")
        """
        return self._node._rpc.call("abandontransaction", txid)

    def abortrescan(self) -> None:  # 02
        """
        Stops current wallet rescan triggered by an RPC call, e.g. by an importprivkey call.

        Note: Use "getwalletinfo" to query the scanning progress.

        :return: None

        :example:

            >>> node.wallet.abortrescan()
        """
        return self._node._rpc.call("abortrescan")

    def addmultisigaddress(self, nrequired: int, keys: [], label: str = "", address_type: str = None) -> {}:  # 03
        """
        Add a nrequired-to-sign multisignature address to the wallet. Requires a new wallet backup.

        Each key is a Defi address or hex-encoded public key.

        This functionality is only intended for use with non-watchonly addresses.

        See `importaddress` for watchonly p2sh address support.

        If 'label' is specified, assign address to that label.

        :param nrequired: (required) The number of required signatures out of the n keys or addresses
        :type nrequired: int
        :param keys: (required) A json array of defi addresses or hex-encoded public keys
        :type keys: array
        :param label: (optional) A label to assign the addresses to
        :type label: str
        :param address_type: (optional) The address type to use. Options are "legacy", "p2sh-segwit", and "bech32"
        :type address_type: str
        :return: {...} (json) -- returns the multisigaddress and redeemScript

            .. code-block:: text

                {
                    "address":"multisigaddress",    (string) The value of the new multisig address.
                    "redeemScript":"script"         (string) The string value of the hex-encoded redemption script.
                }

        :example:

            >>> node.wallet.addmultisigaddress(2, ["16sSauSf5pF2UkUwvKGq4qjNRzBZYqgEL5", "171sgjn4YtPu27adkKGrdDwzRTxnRkBfKV"])
        """
        return self._node._rpc.call("addmultisigaddress", nrequired, keys, label, address_type)

    def backupwallet(self, destination: str) -> None:  # 04
        """
        Safely copies current wallet file to destination, which can be a directory or a path with filename

        :param destination: (required) The destination directory or file
        :type destination: str
        :return: None

        :example:

            >>> node.wallet.backupwallet("backup.dat")
        """
        return self._node._rpc.call("backupwallet", destination)

    def bumpfee(self, txid: str, confTarget: int = None, totalFee: int = None, replaceable: bool = True,
                estimate_mode: str = "UNSET") -> {}:  # 05
        """
        Bumps the fee of an opt-in-RBF transaction T, replacing it with a new transaction B.

        An opt-in RBF transaction with the given txid must be in the wallet.

        The command will pay the additional fee by reducing change outputs or adding inputs when necessary. It may
        add a new change output if one does not already exist.

        If `totalFee` (DEPRECATED) is given, adding inputs is not supported, so there must be a single change output
        that is big enough or it will fail.

        All inputs in the original transaction will be included in the replacement transaction.

        The command will fail if the wallet or mempool contains a transaction that spends one of T's outputs.

        By default, the new fee will be calculated automatically using estimatesmartfee.

        The user can specify a confirmation target for estimatesmartfee.

        Alternatively, the user can specify totalFee (DEPRECATED), or use RPC settxfee to set a higher fee rate.

        At a minimum, the new fee rate must be high enough to pay an additional new relay fee (incrementalfee
        returned by getnetworkinfo) to enter the node's mempool.

        :param txid: (required) The txid to be bumped
        :type txid: str
        :param confTarget: (optional) Confirmation target (in blocks)
        :type confTarget: int
        :param totalFee: (optional) Total fee (NOT feerate) to pay, in satoshis. (DEPRECATED)
            In rare cases, the actual fee paid might be slightly higher than the specified
            totalFee if the tx change output has to be removed because it is too close to
            the dust threshold.
        :type totalFee: int
        :param replaceable: (optional) Whether the new transaction should still be
            marked bip-125 replaceable. If true, the sequence numbers in the transaction will
            be left unchanged from the original. If false, any input sequence numbers in the
            original transaction that were less than 0xfffffffe will be increased to 0xfffffffe
            so the new transaction will not be explicitly bip-125 replaceable (though it may
            still be replaceable in practice, for example if it has unconfirmed ancestors which
            are replaceable).
        :type replaceable: bool
        :param estimate_mode: (optional) The fee estimate mode, must be one of:
            "UNSET",
            "ECONOMICAL",
            "CONSERVATIVE"
        :type estimate_mode: str
        :return: {...} (json) -- returns txid and information about the bumped fee

            .. code-block:: text

                {
                    "txid":    "value",     (string)  The id of the new transaction
                    "origfee":  n,          (numeric) Fee of the replaced transaction
                    "fee":      n,          (numeric) Fee of the new transaction
                    "errors":  [ str... ]   (json array of strings) Errors encountered during processing (may be empty)
                }

        :example:

            >>> node.wallet.bumpfee("e6ade425016b5c7025bc8a31b41e476f092eaeaeed6b69ac28d7ce988a499d18")
        """
        options = BuildJson()
        options.append("confTarget", confTarget)
        options.append("totalFee", totalFee)
        options.append("replaceable", replaceable)
        options.append("estimate_mode", estimate_mode)
        return self._node._rpc.call("bumpfee", txid, options.build())

    def createwallet(self, wallet_name: str, disable_private_keys: bool = False, blank: bool = False,
                     passphrase: str = "", avoid_reuse: bool = False) -> {}:  # 06
        """
        Creates and loads a new wallet.

        :param wallet_name: (required) The name for the new wallet. If this is a path, the wallet will be created at
            the path location
        :type wallet_name: str
        :param disable_private_keys: (optional) Disable the possibility of private keys
        :type disable_private_keys: bool
        :param blank: (optional) Create a blank wallet. A blank wallet has no keys or HD seed. One can be set using sethdseed.
        :type blank: bool
        :param passphrase: (optional) Encrypt the wallet with this passphrase
        :type passphrase: str
        :param avoid_reuse: (optional) Keep track of coin reuse, and treat dirty and clean coins differently with
            privacy considerations in mind
        :type avoid_reuse: bool
        :return: {...} (json) -- returns information about the created wallet

            .. code-block:: text

                {
                    "name" :    <wallet_name>,        (string) The wallet name if created successfully. If the wallet was created using a full path, the wallet_name will be the full path.
                    "warning" : <warning>,            (string) Warning message if wallet was not loaded cleanly.
                }

        :example:

            >>> node.wallet.createwallet("new_wallet")
        """
        return self._node._rpc.call("createwallet", wallet_name, disable_private_keys, blank, passphrase, avoid_reuse)

    def dumpprivkey(self, address: str) -> str:  # 07
        """
        Reveals the private key corresponding to 'address'.
        Then the importprivkey can be used with this output

        :param address: (required) The DFI address for the private key
        :type address: str
        :return: "key" (string) -- the private key

        :example:

            >>> node.wallet.dumpprivkey("myaddress")
        """
        return self._node._rpc.call("dumpprivkey", address)

    def dumpwallet(self, filename: str) -> {}:  # 08
        """
        Dumps all wallet keys in a human-readable format to a server-side file. This does not allow overwriting existing files.

        Imported scripts are included in the dumpfile, but corresponding BIP173 addresses, etc. may not be added automatically by importwallet.

        Note that if your wallet contains keys which are not derived from your HD seed (e.g. imported keys), these are not covered by
        only backing up the seed itself, and must be backed up too (e.g. ensure you back up the whole dumpfile).

        :param filename: (required) The filename with path (either absolute or relative to defid)
        :type filename: str
        :return: {...} (json) -- returns filename

            .. code-block:: text

                {
                    "filename": (string) The filename with full absolute path
                }

        :example:

            >>> node.wallet.dumpwallet("test")
        """
        return self._node._rpc.call("dumpwallet", filename)

    def encryptwallet(self, passphrase: str) -> None:  # 09
        """
        Encrypts the wallet with 'passphrase'. This is for first time encryption.

        After this, any calls that interact with private keys such as sending or signing
        will require the passphrase to be set prior the making these calls.

        Use the walletpassphrase call for this, and then walletlock call.

        If the wallet is already encrypted, use the walletpassphrasechange call.

        :param passphrase: (required) The pass phrase to encrypt the wallet with. It must be at least 1 character,
            but should be long.
        :type passphrase: str
        :return: None

        :example:

            >>> node.wallet.encryptwallet("passphrase")
        """
        return self._node._rpc.call("encryptwallet", passphrase)

    def getaddressesbylabel(self, label: str) -> {}:  # 10
        """
        Returns the list of addresses assigned the specified label.

        :param label: (required) the label
        :type label: str
        :return: {...} (json) -- returns addresses with a given label

            .. code-block:: text

                { (json object with addresses as keys)
                    "address": { (json object with information about address)
                        "purpose": "string" (string)  Purpose of address ("send" for sending address, "receive" for receiving address)
                    },...
                }

        :example:

            >>> node.wallet.getaddressesbylabel("label")
        """
        return self._node._rpc.call("getaddressesbylabel", label)

    def getaddressinfo(self, address: str) -> {}:  # 11
        """
        Return information about the given defi address. Some information requires the address
        to be in the wallet.

        :param address: (required) The defi address to get the information of
        :type address: str
        :return: {...} (json) -- return information about the given defi address

            .. code-block:: text

                {
                    "address" : "address",        (string) The defi address validated
                    "scriptPubKey" : "hex",       (string) The hex-encoded scriptPubKey generated by the address
                    "ismine" : true|false,        (boolean) If the address is yours or not
                    "iswatchonly" : true|false,   (boolean) If the address is watchonly
                    "solvable" : true|false,      (boolean) Whether we know how to spend coins sent to this address, ignoring the possible lack of private keys
                    "desc" : "desc",            (string, optional) A descriptor for spending coins sent to this address (only when solvable)
                    "isscript" : true|false,      (boolean) If the key is a script
                    "ischange" : true|false,      (boolean) If the address was used for change output
                    "iswitness" : true|false,     (boolean) If the address is a witness address
                    "witness_version" : version   (numeric, optional) The version number of the witness program
                    "witness_program" : "hex"     (string, optional) The hex value of the witness program
                    "script" : "type"             (string, optional) The output script type. Only if "isscript" is true and the redeemscript is known. Possible types: nonstandard, pubkey, pubkeyhash, scripthash, multisig, nulldata, witness_v0_keyhash, witness_v0_scripthash, witness_unknown
                    "hex" : "hex",                (string, optional) The redeemscript for the p2sh address
                    "pubkeys"                     (string, optional) Array of pubkeys associated with the known redeemscript (only if "script" is "multisig")
                    [
                        "pubkey"
                        ,...
                    ]
                    "sigsrequired" : xxxxx        (numeric, optional) Number of signatures required to spend multisig output (only if "script" is "multisig")
                    "pubkey" : "publickeyhex",    (string, optional) The hex value of the raw public key, for single-key addresses (possibly embedded in P2SH or P2WSH)
                    "embedded" : {...},           (object, optional) Information about the address embedded in P2SH or P2WSH, if relevant and known. It includes all getaddressinfo output fields for the embedded address, excluding metadata ("timestamp", "hdkeypath", "hdseedid") and relation to the wallet ("ismine", "iswatchonly").
                    "iscompressed" : true|false,  (boolean, optional) If the pubkey is compressed
                    "label" :  "label"         (string) The label associated with the address, "" is the default label
                    "timestamp" : timestamp,      (number, optional) The creation time of the key if available in seconds since epoch (Jan 1 1970 GMT)
                    "hdkeypath" : "keypath"       (string, optional) The HD keypath if the key is HD and available
                    "hdseedid" : "<hash160>"      (string, optional) The Hash160 of the HD seed
                    "hdmasterfingerprint" : "<hash160>" (string, optional) The fingperint of the master key.
                    "labels"                      (object) Array of labels associated with the address.
                    [
                        { (json object of label data)
                            "name": "labelname" (string) The label
                            "purpose": "string" (string) Purpose of address ("send" for sending address, "receive" for receiving address)
                        },...
                    ]
                }

        :example:

            >>> node.wallet.getaddressinfo("1PSSGeFHDnKNxiEyFrD1wcEaHr9hrQDDWc")
        """
        return self._node._rpc.call("getaddressinfo", address)

    def getbalance(self, dummy: str = "*", minconf: int = 0, include_watchonly: bool = True, avoid_reuse: bool = True,
                   with_tokens: bool = False) -> {}:  # 12
        """
        Returns the total available balance.

        The available balance is what the wallet considers currently spendable, and is
        thus affected by options which limit spendability such as -spendzeroconfchange.

        :param dummy: (optional) Remains for backward compatibility. Must be excluded or set to "*"
        :type dummy: str
        :param minconf: (optional) Only include transactions confirmed at least this many times
        :type minconf: int
        :param include_watchonly: (optional) Also include balance in watch-only addresses (see 'importaddress')
        :type include_watchonly: bool
        :param avoid_reuse: (optional) Do not include balance in dirty outputs; addresses are considered dirty if they
            have previously been used in a transaction
        :type avoid_reuse: bool
        :param with_tokens: (optional) Include tokens balances; Default is 'false' for backward compatibility
        :type with_tokens: bool
        :return: {...} (json) -- amount (int) if with_tokens == false | {tokenId: amount,...} (json) if with_tokens == true

            .. code-block:: text

                {
                    "mine": {                          (object) balances from outputs that the wallet can sign
                        "trusted": xxx                 (numeric) trusted balance (outputs created by the wallet or confirmed outputs)
                        "untrusted_pending": xxx       (numeric) untrusted pending balance (outputs created by others that are in the mempool)
                        "immature": xxx                (numeric) balance from immature coinbase outputs
                        "used": xxx                    (numeric) (only present if avoid_reuse is set) balance from coins sent to addresses that were previously spent from (potentially privacy violating)
                    },
                    "watchonly": {                     (object) watchonly balances (not present if wallet does not watch anything)
                        "trusted": xxx                 (numeric) trusted balance (outputs created by the wallet or confirmed outputs)
                        "untrusted_pending": xxx       (numeric) untrusted pending balance (outputs created by others that are in the mempool)
                        "immature": xxx                (numeric) balance from immature coinbase outputs
                    },
                }

        :example:

            >>> node.wallet.getbalance("*")
        """
        return self._node._rpc.call("getbalance", dummy, minconf, include_watchonly, avoid_reuse, with_tokens)

    def getbalances(self, with_tokens: bool = None) -> {}:  # 13
        """
        Returns an object with all balances in DFI.

        :param with_tokens: (optional) Include tokens balances; Default is 'false' for backward compatibility
        :type with_tokens: bool
        :return: {...} (json) -- returns object with all balances in DFI

        :example:

            >>> node.wallet.getbalances()
        """
        return self._node._rpc.call("getbalances", with_tokens)

    def getnewaddress(self, label: str = "", address_type: str = None) -> str:  # 14
        """
        Returns a new Defi address for receiving payments.

        If 'label' is specified, it is added to the address book
        so payments received with the address will be associated with 'label'.

        :param label: (optional) The label name for the address to be linked to. It can also be set to the empty
            string "" to represent the default label. The label does not need to exist, it will be created if
            there is no label by the given name
        :type label: str
        :param address_type: (optional) The address type to use. Options are "legacy", "p2sh-segwit", and "bech32".
        :type address_type: str
        :return: "address" (string) -- The new defi address

        :example:

            >>> node.wallet.getnewaddress()
        """
        return self._node._rpc.call("getnewaddress", label, address_type)

    def getrawchangeaddress(self, address_type: str = None) -> str:  # 15
        """
        Returns a new Defi address, for receiving change.

        This is for use with raw transactions, NOT normal use.

        :param address_type: (optional) The address type to use. Options are "legacy", "p2sh-segwit", and "bech32".
        :type address_type: str
        :return: "address" (string) -- The address

        :example:

            >>> node.wallet.getrawchangeaddress()
        """
        return self._node._rpc.call("getrawchangeaddress", address_type)

    def getreceivedbyaddress(self, address: str, minconf: int = 1) -> float:  # 16
        """
        Returns the total amount received by the given address in transactions with at least minconf confirmations.

        :param address: (required) The defi address for transactions
        :type address: str
        :param minconf: (optional) Only include transactions confirmed at least this many times
        :type minconf: int
        :return: amount (float) -- returns the total amount in DFI received at this address

        :example:

            >>> node.wallet.getreceivedbyaddress("1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX")
        """
        return self._node._rpc.call("getreceivedbyaddress", address, minconf)

    def getreceivedbylabel(self, label: str, minconf: int = 1) -> float:  # 17
        """
        Returns the total amount received by addresses with <label> in transactions with at least [minconf]
        confirmations.

        :param label: (required) The selected label, may be the default label using ""
        :type label: str
        :param minconf: (optional) Only include transactions confirmed at least this many times
        :type minconf: int
        :return: amount (float) -- returns the total amount in DFI received at this label

        :example:

            >>> node.wallet.getreceivedbylabel("")
        """
        return self._node._rpc.call("getreceivedbylabel", label, minconf)

    def gettransaction(self, txid: str, include_watchonly: bool = True) -> {}:  # 18
        """
        Get detailed information about in-wallet transaction

        :param txid: (required) The transaction id
        :type txid: str
        :param include_watchonly: (optional) Whether to include watch-only addresses in balance calculation and details[]
        :type include_watchonly: bool
        :return: {...} (json) -- returns information about transaction

            .. code-block:: text

                {
                    "amount" : x.xxx,                           (numeric) The transaction amount in DFI
                    "fee": x.xxx,                               (numeric) The amount of the fee in DFI. This is negative and only available for the
                                                                'send' category of transactions.
                "confirmations" : n,                            (numeric) The number of confirmations
                    "blockhash" : "hash",                       (string) The block hash
                    "blockindex" : xx,                          (numeric) The index of the transaction in the block that includes it
                    "blocktime" : ttt,                          (numeric) The time in seconds since epoch (1 Jan 1970 GMT)
                    "txid" : "transactionid",                   (string) The transaction id.
                "time" : ttt,                                   (numeric) The transaction time in seconds since epoch (1 Jan 1970 GMT)
                    "timereceived" : ttt,                       (numeric) The time received in seconds since epoch (1 Jan 1970 GMT)
                    "bip125-replaceable": "yes|no|unknown",     (string) Whether this transaction could be replaced due to BIP125 (replace-by-fee);
                                                                may be unknown for unconfirmed transactions not in the mempool
                    "details" : [
                        {
                        "address" : "address",                  (string) The defi address involved in the transaction
                        "category" :                            (string) The transaction category.
                            "send"                              Transactions sent.
                            "receive"                           Non-coinbase transactions received.
                            "generate"                          Coinbase transactions received with more than 100 confirmations.
                            "immature"                          Coinbase transactions received with 100 or fewer confirmations.
                            "orphan"                            Orphaned coinbase transactions received.
                        "amount" : x.xxx,                       (numeric) The amount in DFI
                        "label" : "label",                      (string) A comment for the address/transaction, if any
                        "vout" : n,                             (numeric) the vout value
                        "fee": x.xxx,                           (numeric) The amount of the fee in DFI. This is negative and only available for the
                        'send' category of transactions.
                        "abandoned": xxx                        (bool) 'true' if the transaction has been abandoned (inputs are respendable). Only available for the
                        'send' category of transactions.
                        }
                        ,...
                    ],
                    "hex" : "data"                              (string) Raw data for transaction
                }

        :example:

            >>> node.wallet.gettransaction("1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d")
        """
        return self._node._rpc.call("gettransaction", txid, include_watchonly)

    def getunconfirmedbalance(self, with_tokens: bool = False) -> float:  # 19
        """
        DEPRECATED
        Identical to getbalances().mine.untrusted_pending

        :param with_tokens: (optional)
        :type with_tokens: bool
        :return: amount (float) -- returns the unconfirmed amount of UTXO or token

        :example:

            >>> node.wallet.getunconfirmedbalance()
        """
        return self._node._rpc.call("getunconfirmedbalance", with_tokens)

    def getwalletinfo(self, with_tokens: bool = False) -> {}:  # 20
        """
        Returns an object containing various wallet state info.

        :param with_tokens: (optional) Include tokens balances; Default is 'false' for backward compatibility
        :type with_tokens: bool
        :return: {...} (json) -- returns information about the wallet state

            .. code-block:: text

                {
                    "walletname": xxxxx,               (string) the wallet name
                    "walletversion": xxxxx,            (numeric) the wallet version
                    "balance": xxxxxxx,                (numeric) DEPRECATED. Identical to getbalances().mine.trusted
                    "unconfirmed_balance": xxx,        (numeric) DEPRECATED. Identical to getbalances().mine.untrusted_pending
                    "immature_balance": xxxxxx,        (numeric) DEPRECATED. Identical to getbalances().mine.immature
                    "txcount": xxxxxxx,                (numeric) the total number of transactions in the wallet
                    "keypoololdest": xxxxxx,           (numeric) the timestamp (seconds since Unix epoch) of the oldest pre-generated key in the key pool
                    "keypoolsize": xxxx,               (numeric) how many new keys are pre-generated (only counts external keys)
                    "keypoolsize_hd_internal": xxxx,   (numeric) how many new keys are pre-generated for internal use (used for change outputs, only appears if the wallet is using this feature, otherwise external keys are used)
                    "unlocked_until": ttt,             (numeric) the timestamp in seconds since epoch (midnight Jan 1 1970 GMT) that the wallet is unlocked for transfers, or 0 if the wallet is locked
                    "paytxfee": x.xxxx,                (numeric) the transaction fee configuration, set in DFI/kB
                    "hdseedid": "<hash160>"            (string, optional) the Hash160 of the HD seed (only present when HD is enabled)
                    "private_keys_enabled": true|false (boolean) false if privatekeys are disabled for this wallet (enforced watch-only wallet)
                    "avoid_reuse": true|false          (boolean) whether this wallet tracks clean/dirty coins in terms of reuse
                    "scanning":                        (json object) current scanning details, or false if no scan is in progress
                    {
                        "duration" : xxxx              (numeric) elapsed seconds since scan start
                        "progress" : x.xxxx,           (numeric) scanning progress percentage [0.0, 1.0]
                    }
                }

        :example:

            >>> node.wallet.getwalletinfo()
        """
        return self._node._rpc.call("getwalletinfo", with_tokens)

    def importaddress(self, address: str, label: str = "", rescan: bool = True, p2sh: bool = False) -> None:  # 21
        """
        Adds an address or script (in hex) that can be watched as if it were in your wallet but cannot be used to spend. Requires a new wallet backup.

        Note: This call can take over an hour to complete if rescan is true, during that time, other rpc calls
        may report that the imported address exists but related transactions are still missing, leading to temporarily
        incorrect/bogus balances and unspent outputs until rescan completes.

        If you have the full public key, you should call importpubkey instead of this.

        Hint: use importmulti to import more than one address.

        Note: If you import a non-standard raw script in hex form, outputs sending to it will be treated
        as change, and not show up in many RPCs.

        Note: Use "getwalletinfo" to query the scanning progress.

        :param address: (required) The DFI address
        :type address: str
        :param label: (optional) An optional label
        :type label: str
        :param rescan: (optional) Rescan the wallet for transactions
        :type rescan: bool
        :param p2sh: (optional) Add the P2SH version of the script as well
        :type p2sh: bool
        :return: None

        :example:

            >>> node.wallet.importaddress("address")
        """
        return self._node._rpc.call("importaddress", address, label, rescan, p2sh)

    def importmulti(self, requests: {}, rescan: bool = True) -> [{}]:  # 22
        """
        Import addresses/scripts (with private or public keys, redeem script (P2SH)), optionally rescanning the
        blockchain from the earliest creation time of the imported scripts. Requires a new wallet backup.

        If an address/script is imported without all of the private keys required to spend from that address, it
        will be watchonly. The 'watchonly' option must be set to true in this case or a warning will be returned.

        Conversely, if all the private keys are provided and the address/script is spendable, the watchonly option
        must be set to false, or a warning will be returned.

        Note: This call can take over an hour to complete if rescan is true, during that time, other rpc calls
        may report that the imported keys, addresses or scripts exist but related transactions are still missing.

        Note: Use "getwalletinfo" to query the scanning progress.

        :param requests: (required) Data to be imported

            .. code-block:: text

                [
                    {                                                           (json object)
                        "desc": "str",                                              (string) Descriptor to import. If using descriptor, do not also provide address/scriptPubKey, scripts, or pubkeys
                        "scriptPubKey": "<script>" | { "address":"<address>" },     (string / json, required) Type of scriptPubKey (string for script, json for address). Should not be provided if using a descriptor
                        "timestamp": timestamp | "now",                             (integer / string, required) Creation time of the key in seconds since epoch (Jan 1 1970 GMT),
                                                                                    or the string "now" to substitute the current synced blockchain time. The timestamp of the oldest
                                                                                    key will determine how far back blockchain rescans need to begin for missing wallet transactions.
                                                                                    "now" can be specified to bypass scanning, for keys which are known to never have been used, and
                                                                                    0 can be specified to scan the entire blockchain. Blocks up to 2 hours before the earliest key
                                                                                    creation time of all keys being imported by the importmulti call will be scanned.
                        "redeemscript": "str",                                      (string) Allowed only if the scriptPubKey is a P2SH or P2SH-P2WSH address/scriptPubKey
                        "witnessscript": "str",                                     (string) Allowed only if the scriptPubKey is a P2SH-P2WSH or P2WSH address/scriptPubKey
                        "pubkeys": [                                                (json array, optional, default=empty array) Array of strings giving pubkeys to import. They must occur in P2PKH or P2WPKH scripts. They are not required when the private key is also provided (see the "keys" argument).
                            "pubKey",                                               (string)
                            ...
                        ],
                        "keys": [                                                   (json array, optional, default=empty array) Array of strings giving private keys to import. The corresponding public keys must occur in the output or redeemscript.
                            "key",                                                  (string)
                            ...
                        ],
                        "range": n or [n,n],                                       (numeric or array) If a ranged descriptor is used, this specifies the end or the range (in the form [begin,end]) to import
                        "internal": bool,                                          (boolean, optional, default=false) Stating whether matching outputs should be treated as not incoming payments (also known as change)
                        "watchonly": bool,                                         (boolean, optional, default=false) Stating whether matching outputs should be considered watchonly.
                        "label": "str",                                            (string, optional, default='') Label to assign to the address, only allowed with internal=false
                        "keypool": bool,                                           (boolean, optional, default=false) Stating whether imported public keys should be added to the keypool for when users request new addresses. Only allowed when wallet private keys are disabled
                    },
                    ...
                ]

        :type requests: json array
        :param rescan: (optional) Stating if should rescan the blockchain after all imports
        :type rescan: bool
        :return: [{...}] (json array) -- Response is an array with the same size as the input that has the execution result

            .. code-block::

                [{"success": true}, {"success": true, "warnings": ["Ignoring irrelevant private key"]},
                {"success": false, "error": {"code": -1, "message": "Internal Server Error"}}, ...]

        :example:

            >>> node.wallet.importmulti([{ "scriptPubKey": { "address": "<my address>" }, "timestamp":1455191478 }, { "scriptPubKey": { "address": "<my 2nd address>" }, "label": "example 2", "timestamp": 1455191480 }])
        """
        options = BuildJson()
        options.append("rescan", rescan)
        return self._node._rpc.call("importmulti", requests, rescan)

    def importprivkey(self, privkey: str, label: str = "", rescan: bool = True) -> None:  # 23
        """

        :param privkey: (required) The private key (see dumpprivkey)
        :type privkey: str
        :param label: (optional) An optional label
        :type label: str
        :param rescan: (optional) Rescan the wallet for transactions
        :type rescan: bool
        :return: None

        :example:

            >>> node.wallet.importprivkey("mykey")
        """
        return self._node._rpc.call("importprivkey", privkey, label, rescan)

    def importprunedfunds(self, rawtransaction: str, txoutproof: str) -> None:  # 24
        """
        Imports funds without rescan. Corresponding address or script must previously be included in wallet.
        Aimed towards pruned wallets.
        The end-user is responsible to import additional transactions that subsequently spend the imported outputs or
        rescan after the point in the blockchain the transaction is included.

        :param rawtransaction: (required) A raw transaction in hex funding an already-existing address in wallet
        :type rawtransaction: str
        :param txoutproof: (required) The hex output from gettxoutproof that contains the transaction
        :type txoutproof: str
        :return: None

        :example:

            >>> node.wallet.importprunedfunds("rawtransaction", "txoutproof")
        """
        return self._node._rpc.call("importprunedfunds", rawtransaction, txoutproof)

    def importpubkey(self, pubkey: str, label: str = "", rescan: bool = True) -> None:  # 25
        """
        Adds a public key (in hex) that can be watched as if it were in your wallet but cannot be used to spend. Requires a new wallet backup.

        Hint: use importmulti to import more than one public key.

        Note: This call can take over an hour to complete if rescan is true, during that time, other rpc calls
        may report that the imported pubkey exists but related transactions are still missing, leading to temporarily
        incorrect/bogus balances and unspent outputs until rescan completes.

        Note: Use "getwalletinfo" to query the scanning progress.

        :param pubkey: (required) The hex-encoded public key
        :type pubkey: str
        :param label: (optional) An optional label
        :type label: str
        :param rescan: (optional) Rescan the wallet for transactions
        :type rescan: bool
        :return: None

        :example:

            >>> node.wallet.importpubkey("mypubkey")
        """
        return self._node._rpc.call("importpubkey", pubkey, label, rescan)

    def importwallet(self, filename: str) -> None:  # 26
        """
        Imports keys from a wallet dump file (see dumpwallet). Requires a new wallet backup to include imported keys.

        Note: Use "getwalletinfo" to query the scanning progress.

        :param filename: (required) the wallet file
        :type filename: str
        :return: None

        :example:

            >>> node.wallet.importwallet("new_wallet")
        """
        return self._node._rpc.call("importwallet", filename)

    def keypoolrefill(self, newsize: int = 100) -> None:  # 27
        """
        Fills the keypool.

        Requires wallet passphrase to be set with walletpassphrase call.

        :param newsize: (optional) The new keypool size
        :type newsize: int
        :return: None

        :example:

            >>> node.wallet.keypoolrefill()
        """
        return self._node._rpc.call("keypoolrefill", newsize)

    def listaddressgroupings(self) -> [{}]:  # 28
        """
        Lists groups of addresses which have had their common ownership
        made public by common use as inputs or as the resulting change
        in past transactions

        :return: [{...}] (json array) -- returns a list of used addresses in a wallet

            .. code-block:: text

                [
                    [
                        [
                            "address",            (string) The defi address
                            amount,                 (numeric) The amount in DFI
                            "label"               (string, optional) The label
                        ]
                        ,...
                    ]
                    ,...
                ]

        :example:

            >>> node.wallet.listaddressgroupings()
        """
        return self._node._rpc.call("listaddressgroupings")

    def listlabels(self, purpose: str = None) -> []:  # 29
        """
        Returns the list of all labels, or labels that are assigned to addresses with a specific purpose.

        :param purpose: (optional) Address purpose to list labels for ('send','receive'). An empty string is the same
            as not providing this argument.
        :type purpose: str
        :return: [...] (array) -- returns a list of labels

            .. code-block:: text

                [                   (json array of string)
                    "label",        (string) Label name
                    ...
                ]

        :example:

            >>> node.wallet.listlabels()
        """
        return self._node._rpc.call("listlabels", purpose)

    def listlockunspent(self) -> [{}]:  # 30
        """
        Returns list of temporarily unspendable outputs.

        See the lockunspent call to lock and unlock transactions for spending.

        :return: [{...}] (json array) -- returns list of temporarily unspendable outputs

             .. code-block:: text

                [
                    {
                        "txid" : "transactionid",       (string) The transaction id locked
                        "vout" : n                      (numeric) The vout value
                    }
                    ,...
                ]

        :example:

            >>> node.wallet.listlockunspent()

        """
        return self._node._rpc.call("listlockunspent")

    def listreceivedbyaddress(self, minconf: int = 1, include_empty: bool = False, include_watchonly: bool = True, address_filter: str = None) -> [{}]:  # 31
        """
        List balances by receiving address

        :param minconf: (optional) The minimum number of confirmations before payments are included
        :type minconf: int
        :param include_empty: (optional) Whether to include addresses that haven't received any payments
        :type include_empty: bool
        :param include_watchonly: (optional)  Whether to include watch-only addresses (see 'importaddress')
        :type include_watchonly: bool
        :param address_filter: (optional) If present, only return information on this address
        :type address_filter: str
        :return: [{...}] (json array) -- returns balances of receiving addresses

            .. code-block:: text

                [
                    {
                        "involvesWatchonly" : true,         (bool) Only returned if imported addresses were involved in transaction
                        "address" : "receivingaddress",     (string) The receiving address
                        "amount" : x.xxx,                   (numeric) The total amount in DFI received by the address
                        "confirmations" : n,                (numeric) The number of confirmations of the most recent transaction included
                        "label" : "label",                  (string) The label of the receiving address. The default label is "".
                        "txids": [
                            "txid",                         (string) The ids of transactions received with the address
                            ...
                        ]
                    }
                    ,...
                ]

        :example:

            >>> node.wallet.listreceivedbyaddress()
        """
        return self._node._rpc.call("listreceivedbyaddress", minconf, include_empty, include_watchonly, address_filter)

    def listreceivedbylabel(self, minconf: int = 1, include_empty: bool = False, include_watchonly: bool = True) -> [{}]:  # 32
        """
        List received transactions by label

        :param minconf: (optional) The minimum number of confirmations before payments are included
        :type minconf: int
        :param include_empty: (optional) Whether to include labels that haven't received any payments
        :type include_empty: bool
        :param include_watchonly: (optional) Whether to include watch-only addresses (see 'importaddress')
        :type include_watchonly: bool
        :return: [{...}] (json array) -- returns a list of receiving addresses by label

            .. code-block:: text

                [
                    {
                        "involvesWatchonly" : true,   (bool) Only returned if imported addresses were involved in transaction
                        "amount" : x.xxx,             (numeric) The total amount received by addresses with this label
                        "confirmations" : n,          (numeric) The number of confirmations of the most recent transaction included
                        "label" : "label"           (string) The label of the receiving address. The default label is "".
                    }
                    ,...
                ]

        :example:

            >>> node.wallet.listreceivedbylabel()
        """
        return self._node._rpc.call("listreceivedbylabel", minconf, include_empty, include_watchonly)

    def listsinceblock(self, blockhash: str = "", target_confirmations: int = 1, include_watchonly: bool = True, include_removed: bool = True) -> {}:  # 33
        """
        Get all transactions in blocks since block [blockhash], or all transactions if omitted.

        If "blockhash" is no longer a part of the main chain, transactions from the fork point onward are included.

        Additionally, if include_removed is set, transactions affecting the wallet which were removed are returned in
        the "removed" array.

        :param blockhash: (optional) If set, the block hash to list transactions since, otherwise list all transactions
        :type blockhash: str
        :param target_confirmations: (optional) Return the nth block hash from the main chain. e.g. 1 would mean the
            best block hash. Note: this is not used as a filter, but only affects [lastblock] in the return value
        :type target_confirmations: int
        :param include_watchonly: (optional) Include transactions to watch-only addresses (see 'importaddress')
        :type include_watchonly: bool
        :param include_removed: (optional) Show transactions that were removed due to a reorg in the "removed" array
            (not guaranteed to work on pruned nodes)
        :type include_removed: bool
        :return: {...} (json) -- returns all transactions in blocks since a specific block

            .. code-block:: text

                {
                    "transactions": [
                        "address":"address",        (string) The defi address of the transaction.
                        "category":                 (string) The transaction category.
                            "send"                  Transactions sent.
                            "receive"               Non-coinbase transactions received.
                            "generate"              Coinbase transactions received with more than 100 confirmations.
                            "immature"              Coinbase transactions received with 100 or fewer confirmations.
                            "orphan"                Orphaned coinbase transactions received.
                        "amount": x.xxx,            (numeric) The amount in DFI. This is negative for the 'send' category, and is positive
                                                    for all other categories
                        "vout" : n,                 (numeric) the vout value
                        "fee": x.xxx,               (numeric) The amount of the fee in DFI. This is negative and only available for the 'send' category of transactions.
                        "confirmations": n,         (numeric) The number of confirmations for the transaction.
                                                    When it's < 0, it means the transaction conflicted that many blocks ago.
                        "blockhash": "hashvalue",   (string) The block hash containing the transaction.
                        "blockindex": n,            (numeric) The index of the transaction in the block that includes it.
                        "blocktime": xxx,           (numeric) The block time in seconds since epoch (1 Jan 1970 GMT).
                        "txid": "transactionid",    (string) The transaction id.
                        "time": xxx,                (numeric) The transaction time in seconds since epoch (Jan 1 1970 GMT).
                        "timereceived": xxx,        (numeric) The time received in seconds since epoch (Jan 1 1970 GMT).
                        "bip125-replaceable":       "yes|no|unknown",  (string) Whether this transaction could be replaced due to BIP125 (replace-by-fee);
                                                           may be unknown for unconfirmed transactions not in the mempool
                        "abandoned": xxx,           (bool) 'true' if the transaction has been abandoned (inputs are respendable). Only available for the 'send' category of transactions.
                        "comment": "...",           (string) If a comment is associated with the transaction.
                        "label" : "label"           (string) A comment for the address/transaction, if any
                        "to": "...",                (string) If a comment to is associated with the transaction.
                    ],
                    "removed": [
                        <structure is the same as "transactions" above, only present if include_removed=true>
                        Note: transactions that were re-added in the active chain will appear as-is in this array, and may thus have a positive confirmation count.
                    ],
                    "lastblock": "lastblockhash"    (string) The hash of the block (target_confirmations-1) from the best block on the main chain. This is typically used to feed back into listsinceblock the next time you call it. So you would generally use a target_confirmations of say 6, so you will be continually re-notified of transactions until they've reached 6 confirmations plus any new ones
                }

        :example:

            >>> node.wallet.listsinceblock()
        """
        return self._node._rpc.call("listsinceblock", blockhash, target_confirmations, include_watchonly, include_removed)

    def listtransactions(self, label: str = "*", count: int = 10, skip: int = 0, include_watchonly: bool = True, exclude_custom_tx: bool = False) -> [{}]:  # 34
        """
        If a label name is provided, this will return only incoming transactions paying to addresses with the specified label.

        Returns up to 'count' most recent transactions skipping the first 'from' transactions.

        :param label: (optional) If set, should be a valid label name to return only incoming transactions
            with the specified label, or "*" to disable filtering and return all transactions.
        :type label: str
        :param count: (optional) The number of transactions to return
        :type count: int
        :param skip: (optional) The number of transactions to skip
        :type skip: int
        :param include_watchonly: (optional) Include transactions to watch-only addresses (see 'importaddress')
        :type include_watchonly: bool
        :param exclude_custom_tx: (optional) Exclude custom transactions
        :type exclude_custom_tx: bool
        :return: [{...}] (json array) -- returns transactions of the wallet

            .. code-block:: text

                [
                    {
                        "address":"address",        (string) The defi address of the transaction.
                        "category":                 (string) The transaction category.
                            "send"                  Transactions sent.
                            "receive"               Non-coinbase transactions received.
                            "generate"              Coinbase transactions received with more than 100 confirmations.
                            "immature"              Coinbase transactions received with 100 or fewer confirmations.
                            "orphan"                Orphaned coinbase transactions received.
                        "amount": x.xxx,            (numeric) The amount in DFI. This is negative for the 'send' category, and is positive
                                                    for all other categories
                        "label": "label",           (string) A comment for the address/transaction, if any
                        "vout": n,                  (numeric) the vout value
                        "fee": x.xxx,               (numeric) The amount of the fee in DFI. This is negative and only available for the
                                                    'send' category of transactions.
                        "confirmations": n,         (numeric) The number of confirmations for the transaction. Negative confirmations indicate the
                                                    transaction conflicts with the block chain
                        "trusted": xxx,             (bool) Whether we consider the outputs of this unconfirmed transaction safe to spend.
                        "blockhash": "hashvalue",   (string) The block hash containing the transaction.
                        "blockindex": n,            (numeric) The index of the transaction in the block that includes it.
                        "blocktime": xxx,           (numeric) The block time in seconds since epoch (1 Jan 1970 GMT).
                        "txid": "transactionid",    (string) The transaction id.
                        "time": xxx,                (numeric) The transaction time in seconds since epoch (midnight Jan 1 1970 GMT).
                        "timereceived": xxx,        (numeric) The time received in seconds since epoch (midnight Jan 1 1970 GMT).
                        "comment": "...",           (string) If a comment is associated with the transaction.
                        "bip125-replaceable":       "yes|no|unknown",  (string) Whether this transaction could be replaced due to BIP125 (replace-by-fee);
                                                     may be unknown for unconfirmed transactions not in the mempool
                        "abandoned": xxx            (bool) 'true' if the transaction has been abandoned (inputs are respendable). Only available for the
                                                    'send' category of transactions.
                    }
                ]

        :example:

            >>> node.wallet.listtransactions()
        """
        return self._node._rpc.call("listtransactions", label, count, skip, include_watchonly, exclude_custom_tx)

    def listunspent(self, mincof: int = 1, maxcof: int = 9999999, addresses: [] = [], include_unsafe: bool = True,
                    minimumAmount: float = 0, maximumAmount: float = None, maximumCount: float = None,
                    minimumSumAmount: float = None, tokenId: str = None) -> [{}]:  # 35
        """
        Returns array of unspent transaction outputs

        with between minconf and maxconf (inclusive) confirmations.

        Optionally filter to only include txouts paid to specified addresses.

        :param mincof: (optional) The minimum confirmations to filter
        :type mincof: int
        :param maxcof: (optional) The maximum confirmations to filter
        :type maxcof: int
        :param addresses: (optional)  A json array of defi addresses to filter
        :type addresses: json array
        :param include_unsafe: (optional) Include outputs that are not safe to spend.
            See description of "safe" attribute below.
        :type include_unsafe: bool
        :param minimumAmount: (optional) Minimum value of each UTXO in DFI
        :type minimumAmount: float
        :param maximumAmount: (optional) Maximum value of each UTXO in DFI
        :type maximumAmount: float
        :param maximumCount: (optional) Maximum number of UTXOs
        :type maximumCount: float
        :param minimumSumAmount: (optional) Minimum sum value of all UTXOs in DFI
        :type minimumSumAmount: float
        :param tokenId: (optional)  Filter by token (id/symbol/creationTx)
        :type tokenId: str
        :return: [{...}] (json array) -- returns array of unspent transaction outputs

            .. code-block:: text

                [                                   (array of json object)
                    {
                        "txid" : "txid",            (string) the transaction id
                        "vout" : n,                 (numeric) the vout value
                        "address" : "address",      (string) the defi address
                        "label" : "label",          (string) The associated label, or "" for the default label
                        "scriptPubKey" : "key",     (string) the script key
                        "amount" : x.xxx,           (numeric) the transaction output amount in DFI
                        "tokenId" : n,              (numeric) the transaction output token Id
                        "confirmations" : n,        (numeric) The number of confirmations
                        "redeemScript" : "script"   (string) The redeemScript if scriptPubKey is P2SH
                        "witnessScript" : "script"  (string) witnessScript if the scriptPubKey is P2WSH or P2SH-P2WSH
                        "spendable" : xxx,          (bool) Whether we have the private keys to spend this output
                        "solvable" : xxx,           (bool) Whether we know how to spend this output, ignoring the lack of keys
                        "reused" : xxx,             (bool) (only present if avoid_reuse is set) Whether this output is reused/dirty (sent to an address that was previously spent from)
                        "desc" : xxx,               (string, only when solvable) A descriptor for spending this output
                        "safe" : xxx                (bool) Whether this output is considered safe to spend. Unconfirmed transactions
                                                    from outside keys and unconfirmed replacement transactions are considered unsafe
                                                    and are not eligible for spending by fundrawtransaction and sendtoaddress.
                    }
                    ,...
                ]

        :example:

            >>> node.wallet.listunspent()
        """
        query_options = BuildJson()
        query_options.append("minimumAmount", minimumAmount)
        query_options.append("maximumAmount", maximumAmount)
        query_options.append("maximumCount", maximumCount)
        query_options.append("minimumSumAmount", minimumSumAmount)
        query_options.append("tokenId", tokenId)
        return self._node._rpc.call("listunspent", mincof, maxcof, addresses, include_unsafe, query_options.build())

    def listwalletdir(self) -> {}:  # 36
        """
        Returns a list of wallets in the wallet directory

        :return: {...} (json) -- returns list of wallets and their directory's

            .. code- block:: text

                {
                    "wallets" : [                   (json array of objects)
                        {
                            "name" : "name"         (string) The wallet name
                        }
                        ,...
                    ]
                }

        :example:

            >>> node.wallet.listwalletdir()
        """
        return self._node._rpc.call("listwalletdir")

    def listwallets(self) -> []:  # 37
        """
        Returns a list of currently loaded wallets.

        For full information on the wallet, use "getwalletinfo"

        :return: [...] (array) -- returns a list of currently loaded wallets

            .. code-block:: text

                [                   (json array of strings)
                    "walletname"    (string) the wallet name
                    ...
                ]

        :example:

            >>> node.wallet.listwallets()
        """
        return self._node._rpc.call("listwallets")

    def loadwallet(self, filename: str) -> {}:  # 38
        """
        Loads a wallet from a wallet file or directory.

        Note that all wallet command-line options used when starting defid will be
        applied to the new wallet (eg -zapwallettxes, upgradewallet, rescan, etc).

        :param filename: (required) The wallet directory or .dat file
        :type filename: str
        :return: {...} (json) -- returns information about the loaded wallet

            .. code-block:: text

                {
                    "name" :    <wallet_name>,        (string) The wallet name if loaded successfully.
                    "warning" : <warning>,            (string) Warning message if wallet was not loaded cleanly.
                }

        :example:

            >>> node.wallet.loadwallet("test.dat")
        """
        return self._node._rpc.call("loadwallet", filename)

    def lockunspent(self, unlock: bool, transactions: [{}] = None) -> bool:  # 39
        """
        Updates list of temporarily unspendable outputs.

        Temporarily lock (unlock=false) or unlock (unlock=true) specified transaction outputs.

        If no transaction outputs are specified when unlocking then all current locked transaction outputs are unlocked.

        A locked transaction output will not be chosen by automatic coin selection, when spending defis.

        Locks are stored in memory only. Nodes start with zero locked outputs, and the locked output list
        is always cleared (by virtue of process exit) when a node stops or fails.

        Also see the listunspent call

        :param unlock: (required) Whether to unlock (true) or lock (false) the specified transactions
        :type unlock: bool
        :param transactions: (optional) A json array of objects. Each object the txid (string) vout (numeric)

            .. code-block:: text

                [
                    {                       (json object)
                        "txid": "hex",      (string, required) The transaction id
                        "vout": n,          (numeric, required) The output number
                    },
                    ...
                ]
        :type transactions: json array
        :return: true|false (bool) -- Whether the command was successful or not

        :example:

            >>> node.wallet.lockunspent(True)
        """
        return self._node._rpc.call("lockunspent", unlock, transactions)

    def removeprunedfunds(self, txid: str) -> None:  # 40
        """
        Deletes the specified transaction from the wallet. Meant for use with pruned wallets and as a companion to
        importprunedfunds. This will affect wallet balances.

        :param txid: (required) The hex-encoded id of the transaction you are deleting
        :type txid: str
        :return: None

        :example:

            >>> node.wallet.removeprunedfunds("a8d0c0184dde994a09ec054286f1ce581bebf46446a512166eae7628734ea0a5")
        """
        return self._node._rpc.call("removeprunedfunds", txid)

    def rescanblockchain(self, start_height: int = 0, stop_height: int = None) -> {}:  # 41
        """
        Rescan the local blockchain for wallet related transactions.

        Note: Use "getwalletinfo" to query the scanning progress.

        :param start_height: (optional) block height where the rescan should start
        :type start_height: int
        :param stop_height: (optional) the last block height that should be scanned. If none is provided it will rescan up to the tip at return time of this call
        :type stop_height: int
        :return: {...} (json) -- returns start and stop height

            .. code-block:: text

                {
                    "start_height"     (numeric) The block height where the rescan started (the requested height or 0)
                    "stop_height"      (numeric) The height of the last rescanned block. May be null in rare cases if there was a reorg and the call didn't scan any blocks because they were already scanned in the background.
                }

        :example:

            >>> node.wallet.rescanblockchain(1000000, 2000000)
        """
        return self._node._rpc.call("rescanblockchain", start_height, stop_height)

    def sendmany(self, dummy: str, amounts: {}, minconf: int = 1, comment: str = "", subtractfeefrom: [] = [],
                 replaceable: bool = False, conf_target: int = 1, estimate_mode: str = "UNSET") -> str:  # 42
        """
        Send multiple times. Amounts are double-precision floating point numbers.

        Requires wallet passphrase to be set with walletpassphrase call.

        :param dummy: (required) Must be set to "" for backwards compatibility
        :type dummy: str
        :param amounts: (required) :ref:`Node Address Amount`
        :type amounts: json
        :param minconf: (optional) Ignored dummy value
        :type minconf: int
        :param comment: (optional) A comment
        :type comment: str
        :param subtractfeefrom: (optional) A json array with addresses.
             The fee will be equally deducted from the amount of each selected address.
             Those recipients will receive less defis than you enter in their corresponding amount field.
             If no addresses are specified here, the sender pays the fee.

             .. code-block:: text

                [
                    "address",            (string) Subtract fee from this address
                    ...
                ]
        :type subtractfeefrom: array
        :param replaceable: (optional) Allow this transaction to be replaced by a transaction with higher fees via BIP 125
        :type replaceable: bool
        :param conf_target: (optional) Confirmation target (in blocks)
        :type conf_target: int
        :param estimate_mode: (optional) The fee estimate mode, must be one of:
             "UNSET",
             "ECONOMICAL",
             "CONSERVATIVE"
        :type estimate_mode: str
        :return: "txid" (string) -- The transaction id for the send. Only 1 transaction is created regardless of the number of addresses.

        :example:

            >>> node.wallet.sendmany("", {"1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX":0.01,"1353tsE8YMTA4EuV7dgUXGjNFf9KpVvKHz":0.02})
        """
        return self._node._rpc.call("sendmany", dummy, amounts, minconf, comment, subtractfeefrom, replaceable,
                                    conf_target, estimate_mode)

    def sendtoaddress(self, address: str, amount: float, comment: str = "", comment_to: str = "",
                      subtractfeefromamount: bool = False, replaceable: bool = False, conf_target: int = 1,
                      estimate_mode: str = "UNSET", avoid_reuse: bool = None) -> str:  # 43
        """
        Send an amount to a given address.

        :param address: (required) The defi address to send to
        :type address: str
        :param amount: (required) The amount in DFI to send. eg 0.1
        :type amount: float
        :param comment: (optional) A comment used to store what the transaction is for.
            This is not part of the transaction, just kept in your wallet.
        :type comment: str
        :param comment_to: (optional) A comment to store the name of the person or organization
            to which you're sending the transaction.
            This is not part of the transaction, just kept in your wallet.
        :type comment_to: str
        :param subtractfeefromamount: (optional) The fee will be deducted from the amount being sent.
            The recipient will receive less defis than you enter in the amount field.
        :type subtractfeefromamount: bool
        :param replaceable: (optional) Allow this transaction to be replaced by a transaction with higher fees via BIP 125
        :type replaceable: bool
        :param conf_target: (optional) Confirmation target (in blocks)
        :type conf_target: int
        :param estimate_mode: (optional) The fee estimate mode, must be one of:
            "UNSET",
            "ECONOMICAL",
            "CONSERVATIVE"
        :type estimate_mode: str
        :param avoid_reuse: (optional) Avoid spending from dirty addresses; addresses are considered
            dirty if they have previously been used in a transaction.
        :type avoid_reuse: bool
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.wallet.sendtoaddress("1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.1)

        """
        return self._node._rpc.call("sendtoaddress", address, amount, comment, comment_to, subtractfeefromamount,
                                    replaceable, conf_target, estimate_mode, avoid_reuse)

    def sethdseed(self, newkeypool: bool = True, seed: str = None) -> None:  # 44
        """
        Set or generate a new HD wallet seed. Non-HD wallets will not be upgraded to being a HD wallet. Wallets that are already
        HD will have a new HD seed set so that new keys added to the keypool will be derived from this new seed.

        Note that you will need to MAKE A NEW BACKUP of your wallet after setting the HD wallet seed.
        Requires wallet passphrase to be set with walletpassphrase call.

        :param newkeypool: (optional)Whether to flush old unused addresses, including change addresses, from the keypool and regenerate it.
             If true, the next address from getnewaddress and change address from getrawchangeaddress will be from this new seed.
             If false, addresses (including change addresses if the wallet already had HD Chain Split enabled) from the existing
             keypool will be used until it has been depleted.
        :type newkeypool: bool
        :param seed: (optional) The WIF private key to use as the new HD seed.
             The seed value can be retrieved using the dumpwallet command. It is the private key marked hdseed=1
        :type seed: str
        :return: None

        :example:

            >>> node.wallet.sethdseed()
        """
        return self._node._rpc.call("sethdseed", newkeypool, seed)

    def setlabel(self, address: str, label: str) -> None:  # 45
        """
        Sets the label associated with the given address

        :param address: (required) The defi address to be associated with a label
        :type address: str
        :param label: (required) The label to assign to the address
        :type label: str
        :return: None

        :example:

            >>> node.wallet.setlabel("1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX", "teddy")
        """
        return self._node._rpc.call("setlabel", address, label)

    def settxfee(self, amount: float) -> bool:  # 46
        """
        Set the transaction fee per kB for this wallet. Overrides the global -paytxfee command line parameter

        :param amount: (required) The transaction fee in DFI/kB
        :type amount: float
        :return: true|false (bool) -- returns true if successful

        :example:

            >>> node.wallet.settxfee(0.00001)
        """
        return self._node._rpc.call("settxfee", amount)

    def setwalletflag(self, flag: str, value: bool = True) -> {}:  # 47
        """
        Change the state of the given wallet flag for a wallet

        :param flag: (required) The name of the flag to change. Current available flags: avoid_reuse
        :type flag: str
        :param value: (optional) The new state
        :type value: bool
        :return: {...} (json) -- returns information about the wallet flags

        :example:

            >>> node.wallet.setwalletflag("avoid_reuse")
        """
        return self._node._rpc.call("setwalletflag", flag, value)

    def signmessage(self, address: str, message: str) -> str:  # 48
        """
        Sign a message with the private key of an address

        :param address: (required) The defi address to use for the private key
        :type address: str
        :param message: (required) The message to create a signature of
        :type message: str
        :return: "signature" (string) -- The signature of the message encoded in base 64

        :example:

            >>> node.wallet.signmessage("1D1ZrZNe3JUo7ZycKEYQQiQAWd9y54F4XX", "my message")
        """
        return self._node._rpc.call("signmessage", address, message)

    def signrawtransactionwithwallet(self, hexstring: str, prevtxs: [] = [], sighashtype: str = "ALL") -> {}:  # 49
        """
        Sign inputs for raw transaction (serialized, hex-encoded).

        The second optional argument (may be null) is an array of previous transaction outputs that
        this transaction depends on but may not yet be in the block chain.

        Requires wallet passphrase to be set with walletpassphrase call.

        :param hexstring: (required) The transaction hex string
        :type hexstring: str
        :param prevtxs: (optional) A json array of previous dependent transaction outputs

            .. code-block:: text

                [
                    {                            (json object)
                        "txid": "hex",             (string, required) The transaction id
                        "vout": n,                 (numeric, required) The output number
                        "scriptPubKey": "hex",     (string, required) script key
                        "redeemScript": "hex",     (string) (required for P2SH) redeem script
                        "witnessScript": "hex",    (string) (required for P2WSH or P2SH-P2WSH) witness script
                        "amount": amount,          (numeric or string) (required for Segwit inputs) the amount spent
                    },
                    ...
                ]
        :type prevtxs: json array
        :param sighashtype: (optional) The signature hash type. Must be one of:
            "ALL",
            "NONE",
            "SINGLE",
            "ALL|ANYONECANPAY",
            "NONE|ANYONECANPAY",
            "SINGLE|ANYONECANPAY"
        :type sighashtype: str
        :return: {...} (json) -- returns a json with the signed hexstring

            .. code-block:: text

                {
                    "hex" : "value",                (string) The hex-encoded raw transaction with signature(s)
                    "complete" : true|false,        (boolean) If the transaction has a complete set of signatures
                    "errors" : [                    (json array of objects) Script verification errors (if there are any)
                        {
                            "txid" : "hash",        (string) The hash of the referenced, previous transaction
                            "vout" : n,             (numeric) The index of the output to spent and used as input
                            "scriptSig" : "hex",    (string) The hex-encoded signature script
                            "sequence" : n,         (numeric) Script sequence number
                            "error" : "text"        (string) Verification or signing error related to the input
                        }
                        ,...
                    ]
                }

        :example:

            >>> node.wallet.signrawtransactionwithwallet("hex")
        """
        return self._node._rpc.call("signrawtransactionwithwallet", hexstring, prevtxs, sighashtype)

    def unloadwallet(self, wallet_name: str = None) -> None:  # 50
        """
        Unloads the wallet referenced by the request endpoint otherwise unloads the wallet specified in the argument.

        Specifying the wallet name on a wallet endpoint is invalid.

        :param wallet_name: (optional) The name of the wallet to unload
        :type wallet_name: str
        :return: None

        :example:

            >>> node.wallet.unloadwallet()
        """
        return self._node._rpc.call("unloadwallet", wallet_name)

    def walletcreatefundedpsbt(self, inputs: [{}], outputs: [{}], locktime: int = 0, changeAddress: str = None,
                               changePosition: int = None, change_type: str = None, includeWatching: bool = True,
                               lockUnspents: bool = False, feeRate: float = None, subtractFeeFromOutputs: [] = None,
                               replaceable: bool = None, conf_target: int = None, estimate_mode: str = None,
                               bip32derivs: bool = False) -> {}:  # 51
        """
        Creates and funds a transaction in the Partially Signed Transaction format.

        Inputs will be added if supplied inputs are not enough
        Implements the Creator and Updater roles.

        :param inputs: (required) A json array of json objects

            .. code-block:: text

                [
                    {                         (json object)
                        "txid": "hex",        (string, required) The transaction id
                        "vout": n,            (numeric, required) The output number
                        "sequence": n,        (numeric, required) The sequence number
                    },
                    ...
                ]

        :type inputs: json array
        :param outputs: (required) a json array with outputs (key-value pairs), where none of the keys are duplicated.
            That is, each address can only appear once and there can only be one 'data' object.
            For compatibility reasons, a dictionary, which holds the key-value pairs directly, is also
            accepted as second parameter.

            .. code-block:: text

                [
                    {                             (json object)
                        "address": amount,        (numeric or string, required) A key-value pair. The key (string) is the defi address, the value (float or string) is the amount in DFI
                    },
                    {                             (json object)
                        "data": "hex",            (string, required) A key-value pair. The key must be "data", the value is hex-encoded data
                    },
                    ...
                ]

        :type outputs: json array
        :param locktime: (optional) Raw locktime. Non-0 value also locktime-activates inputs
        :type locktime: int
        :param changeAddress: (optional) The defi address to receive the change
        :type changeAddress: str
        :param changePosition: (optional) The index of the change output
        :type changePosition: int
        :param change_type: (optional) The output type to use. Only valid if changeAddress is not specified. Options
            are "legacy", "p2sh-segwit", and "bech32".
        :type change_type: str
        :param includeWatching: (optional) Also select inputs which are watch only
        :type includeWatching: bool
        :param lockUnspents: (optional) Lock selected unspent outputs
        :type lockUnspents: bool
        :param feeRate: (optional) Set a specific fee rate in DFI/kB
        :type feeRate: float
        :param subtractFeeFromOutputs: (optional) A json array of integers.
            The fee will be equally deducted from the amount of each specified output.
            Those recipients will receive less defis than you enter in their corresponding amount field.
            If no outputs are specified here, the sender pays the fee.

            .. code-block:: text

                [
                    vout_index,     (numeric) The zero-based output index, before a change output is added.
                    ...
                ]
        :type subtractFeeFromOutputs: json array
        :param replaceable: (optional) Marks this transaction as BIP125 replaceable
            Allows this transaction to be replaced by a transaction with higher fees
        :type replaceable: bool
        :param conf_target: (optional) Confirmation target (in blocks)
        :type conf_target: int
        :param estimate_mode: (optional) The fee estimate mode, must be one of:
            "UNSET",
            "ECONOMICAL",
            "CONSERVATIVE"
        :type estimate_mode: str
        :param bip32derivs: (optional) If true, includes the BIP 32 derivation paths for public keys if we know them
        :type bip32derivs: bool
        :return: {...} (json) -- returns an json with the partially signed transaction

            .. code-block:: text

                {
                    "psbt": "value",        (string)  The resulting raw transaction (base64-encoded string)
                    "fee":       n,         (numeric) Fee in DFI the resulting transaction pays
                    "changepos": n          (numeric) The position of the added change output, or -1
                }

        :example:

            >>> node.wallet.walletcreatefundedpsbt([{"txid":"myid","vout":0}]" "[{"data":"00010203"}])
        """
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

    def walletlock(self) -> None:  # 52
        """
        Removes the wallet encryption key from memory, locking the wallet.

        After calling this method, you will need to call walletpassphrase again
        before being able to call any methods which require the wallet to be unlocked.

        :return: None

        :example:

            >>> node.wallet.walletlock()
        """
        return self._node._rpc.call("walletlock")

    def walletpassphrase(self, passphrase: str, timeout: int) -> None:  # 53
        """
        Stores the wallet decryption key in memory for 'timeout' seconds.
        This is needed prior to performing transactions related to private keys such as sending defis

        Note:
        Issuing the walletpassphrase command while the wallet is already unlocked will set a new unlock
        time that overrides the old one.

        :param passphrase: (required) The wallet passphrase
        :type passphrase: str
        :param timeout: (required) The time to keep the decryption key in seconds; capped at 100000000 (~3 years)
        :type timeout: int
        :return: None

        :example:

            >>> node.wallet.walletpassphrase("passphrase", 60)
        """
        return self._node._rpc.call("walletpassphrase", passphrase, timeout)

    def walletpassphrasechange(self, oldpassphrase: str, newpassphrase: str) -> None:  # 54
        """
        Changes the wallet passphrase from 'oldpassphrase' to 'newpassphrase'

        :param oldpassphrase: (required) The current passphrase
        :type oldpassphrase: str
        :param newpassphrase: (required) The new passphrase
        :type newpassphrase: str
        :return: None

        :example:

            >>> node.wallet.walletpassphrasechange("old", "new")
        """
        return self._node._rpc.call("walletpassphrasechange", oldpassphrase, newpassphrase)

    def walletprocesspsbt(self, psbt: str, sign: bool = True, sighashtype: str = "ALL", bip32derivs: bool = False) -> {}:  # 55
        """
        Update a PSBT with input information from our wallet and then sign inputs
        that we can sign for.

        Requires wallet passphrase to be set with walletpassphrase call.

        :param psbt: (required) The transaction base64 string
        :type psbt: str
        :param sign: (optional) Also sign the transaction when updating
        :type sign: bool
        :param sighashtype: (optional) The signature hash type to sign with if not specified by the PSBT. Must be one of
            "ALL",
            "NONE",
            "SINGLE",
            "ALL|ANYONECANPAY",
            "NONE|ANYONECANPAY",
            "SINGLE|ANYONECANPAY"
        :type sighashtype: str
        :param bip32derivs: (optional) If true, includes the BIP 32 derivation paths for public keys if we know them
        :type bip32derivs: bool
        :return: {...} (json) -- returns information about PSBT from the wallet

            .. code-block:: text

                {
                    "psbt" : "value",          (string) The base64-encoded partially signed transaction
                    "complete" : true|false,   (boolean) If the transaction has a complete set of signatures
                }

        :example:

            >>> node.wallet.walletprocesspsbt("psbt")

        """
        return self._node._rpc.call("walletprocesspsbt", psbt, sign, sighashtype, bip32derivs)
