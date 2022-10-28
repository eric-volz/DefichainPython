class Mining:
    def __init__(self, node):
        self._node = node

    def getblocktemplate(self, template_request: {} = {}) -> {}:  # 01
        """
        If the request parameters include a 'mode' key, that is used to explicitly select between the default 'template' request or a 'proposal'.
        It returns data needed to construct a block to work on.
        For full specification, see BIPs 22, 23, 9, and 145:

        https://github.com/bitcoin/bips/blob/master/bip-0022.mediawiki

        https://github.com/bitcoin/bips/blob/master/bip-0023.mediawiki

        https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki#getblocktemplate_changes

        https://github.com/bitcoin/bips/blob/master/bip-0145.mediawiki

        :param template_request: (optional) A json object in the following spec

            .. code-block:: text

                {
                    "mode": "str",       (string, optional) This must be set to "template", "proposal" (see BIP 23), or omitted
                    "capabilities": [    (json array, optional) A list of strings
                        "support",         (string) client side supported feature, 'longpoll', 'coinbasetxn', 'coinbasevalue', 'proposal', 'serverlist', 'workid'
                        ...
                    ],
                    "rules": [           (json array, required) A list of strings
                    "support",         (string) client side supported softfork deployment
                    ...
                    ],
                }

        :type template_request: json
        :return: {...} (json) -- returns block template

            .. code-block:: text

                {
                    "version" : n,                    (numeric) The preferred block version
                    "rules" : [ "rulename", ... ],    (array of strings) specific block rules that are to be enforced
                    "vbavailable" : {                 (json object) set of pending, supported versionbit (BIP 9) softfork deployments
                        "rulename" : bitnumber        (numeric) identifies the bit number as indicating acceptance and readiness for the named softfork rule
                        ,...
                    },
                    "vbrequired" : n,                 (numeric) bit mask of versionbits the server requires set in submissions
                    "previousblockhash" : "xxxx",     (string) The hash of current highest block
                    "transactions" : [                (array) contents of non-coinbase transactions that should be included in the next block
                        {
                            "data" : "xxxx",          (string) transaction data encoded in hexadecimal (byte-for-byte)
                            "txid" : "xxxx",          (string) transaction id encoded in little-endian hexadecimal
                            "hash" : "xxxx",          (string) hash encoded in little-endian hexadecimal (including witness data)
                            "depends" : [             (array) array of numbers
                                n                     (numeric) transactions before this one (by 1-based index in 'transactions' list) that must be present in the final block if this one is
                                ,...
                            ],
                            "fee": n,                 (numeric) difference in value between transaction inputs and outputs (in satoshis); for coinbase transactions, this is a negative Number of the total collected block fees (ie, not including the block subsidy); if key is not present, fee is unknown and clients MUST NOT assume there isn't one
                            "sigops" : n,             (numeric) total SigOps cost, as counted for purposes of block limits; if key is not present, sigop cost is unknown and clients MUST NOT assume it is zero
                            "weight" : n,             (numeric) total transaction weight, as counted for purposes of block limits
                        }
                        ,...
                    ],
                    "coinbaseaux" : {                 (json object) data that should be included in the coinbase's scriptSig content
                        "flags" : "xx"                (string) key name is to be ignored, and value included in scriptSig
                    },
                    "coinbasevalue" : n,              (numeric) maximum allowable input to coinbase transaction, including the generation award and transaction fees (in satoshis)
                    "coinbasetxn" : { ... },          (json object) information for coinbase transaction
                    "target" : "xxxx",                (string) The hash target
                    "mintime" : xxx,                  (numeric) The minimum timestamp appropriate for next block time in seconds since epoch (Jan 1 1970 GMT)
                    "mutable" : [                     (array of string) list of ways the block template may be changed
                        "value"                       (string) A way the block template may be changed, e.g. 'time', 'transactions', 'prevblock'
                        ,...
                    ],
                    "noncerange" : "00000000ffffffff",(string) A range of valid nonces
                    "sigoplimit" : n,                 (numeric) limit of sigops in blocks
                    "sizelimit" : n,                  (numeric) limit of block size
                    "weightlimit" : n,                (numeric) limit of block weight
                    "curtime" : ttt,                  (numeric) current timestamp in seconds since epoch (Jan 1 1970 GMT)
                    "bits" : "xxxxxxxx",              (string) compressed target of next block
                    "height" : n                      (numeric) The height of the next block
                }

        :example:

            >>> node.mining.getblocktemplate({"rules": ["segwit"]})
        """
        return self._node._rpc.call("getblocktemplate", template_request)

    def getmininginfo(self) -> {}:  # 02
        """
        Returns a json object containing mining-related information for all local masternodes

        :return: {...} (json) -- returns mining info

            .. code-block:: text

                {
                    "blocks": nnn,             (numeric) The current block
                    "currentblockweight": nnn, (numeric, optional) The block weight of the last assembled block (only present if a block was ever assembled)
                    "currentblocktx": nnn,     (numeric, optional) The number of block transactions of the last assembled block (only present if a block was ever assembled)
                    "difficulty": xxx.xxxxx    (numeric) The current difficulty
                    "networkhashps": nnn,      (numeric) The network hashes per second
                    "pooledtx": n              (numeric) The size of the mempool
                    "chain": "xxxx",           (string)  current network name as defined in BIP70 (main, test, regtest)
                    "isoperator": true|false   (boolean) Local master nodes are available or not
                    "masternodes": []          (array)   an array of objects which includes each master node information
                    "warnings": "..."          (string)  any network and blockchain warnings
                }

        :example:

            >>> node.mining.getmininginfo()
        """
        return self._node._rpc.call("getmininginfo")

    def getmintinginfo(self) -> {}:  # 03
        """
        DEPRECATED. Prefer using getmininginfo.

        Returns a json object containing mining-related information.

        :return: {...} (json) -- returns minting info

            .. code-block:: text

                {
                    "blocks": nnn,             (numeric) The current block
                    "currentblockweight": nnn, (numeric, optional) The block weight of the last assembled block (only present if a block was ever assembled)
                    "currentblocktx": nnn,     (numeric, optional) The number of block transactions of the last assembled block (only present if a block was ever assembled)
                    "difficulty": xxx.xxxxx    (numeric) The current difficulty
                    "networkhashps": nnn,      (numeric) The network hashes per second
                    "pooledtx": n              (numeric) The size of the mempool
                    "chain": "xxxx",         (string)  current network name as defined in BIP70 (main, test, regtest)
                    "isoperator": true|false   (boolean) Local master nodes are available or not
                    "masternodes": []          (array)   an array of objects which includes each master node information
                    "warnings": "..."        (string)  any network and blockchain warnings
                }

        :example:

            >>> node.mining.getmintinginfo()
        """
        return self._node._rpc.call("getmintinginfo")

    def getnetworkhashps(self, nblocks: int = 120, height: int = -1) -> int:  # 04
        """
        Returns the estimated network hashes per second based on the last n blocks.

        Pass in [blocks] to override # of blocks, -1 specifies since last difficulty change.

        Pass in [height] to estimate the network speed at the time when a certain block was found.

        :param nblocks: (optional) The number of blocks, or -1 for blocks since last difficulty change
        :type nblocks: int
        :param height: (optional) To estimate at the time of the given height
        :type height: int
        :return: int -- Hashes per second estimated

        :example:

            >>> node.mining.getnetworkhashps()
        """
        return self._node._rpc.call("getnetworkhashps", nblocks, height)

    def prioritisetransaction(self, txid: str, fee_delta: int, dummy: float = 0) -> bool:  # 05
        """
        Accepts the transaction into mined blocks at a higher (or lower) priority

        :param txid: (required) The transaction id
        :type txid: str
        :param fee_delta: (optional) API-Compatibility for previous API. Must be zero or null.
            DEPRECATED. For forward compatibility use named arguments and omit this parameter.
        :type fee_delta: int
        :param dummy: (optional) The fee value (in satoshis) to add (or subtract, if negative).
            Note, that this value is not a fee rate. It is a value to modify absolute fee of the TX.
            The fee is not actually paid, only the algorithm for selecting transactions into a block
            considers the transaction as it would have paid a higher (or lower) fee.
        :type dummy: float
        :return: bool -- returns true

        :example:

            >>> node.mining.prioritisetransaction("txid", 0.0, 10000)
        """
        return self._node._rpc.call("prioritisetransaction", txid, dummy, fee_delta)

    def submitblock(self, hexdata: str, dummy: str = "ignored") -> None:  # 06
        """
        Attempts to submit new block to network.
        See https://en.bitcoin.it/wiki/BIP_0022 for full specification.

        :param hexdata: (required) the hex-encoded block data to submit
        :type hexdata: str
        :param dummy: (optional) dummy value, for compatibility with BIP22. This value is ignored
        :type dummy: str
        :return: None

        :example:

            >>> node.mining.submitblock("mydata")
        """
        return self._node._rpc.call("submitblock", hexdata, dummy)

    def submitheader(self, hexdata: str) -> None:  # 07
        """
        Decode the given hexdata as a header and submit it as a candidate chain tip if valid.
        Throws when the header is invalid.

        :param hexdata: (required) the hex-encoded block header data
        :type hexdata: str
        :return: None

        :example:

            >>> node.mining.submitheader("abc")
        """
        return self._node._rpc.call("submitheader", hexdata)
