class Blockchain:
    def __init__(self, node):
        self._node = node

    def clearmempool(self) -> ["str"]:  # 01
        """
        Clears the memory pool and returns a list of the removed transactions.

        :return:

            .. code-block:: text

                [               (json array of string)
                    "hash"      (string) The transaction hash
                    ,...
                ]

        :example:

            >>> node.blockchain.clearmempool()
        """
        return self._node._rpc.call("clearmempool")

    def getbestblockhash(self) -> str:  # 02
        """
        Returns the hash of the best (tip) block in the most-work fully-validated chain.

        :return: "hex" (string) the block hash, hex-encoded

        :example:

            >>> node.blockchain.getbestblockhash()
        """
        return self._node._rpc.call("getbestblockhash")

    def getblock(self, blockhash: str, verbosity: int = 1) -> str:  # 03
        """
        If verbosity is 0, returns a string that is serialized, hex-encoded data for block 'hash'.

        If verbosity is 1, returns an Object with information about block <hash>.

        If verbosity is 2, returns an Object with information about block <hash> and information about each transaction.

        :param blockhash: (required) The block hash
        :type blockhash: str
        :param verbosity: (optional) 0 for hex-encoded data, 1 for a json object, and 2 for json object with transaction data
        :type verbosity: int
        :return:

            **Result (for verbosity = 0):** \n
            "data" (string) A string that is serialized, hex-encoded data for block 'hash'.

            **Result (for verbosity = 1):** \n

            .. code-block:: text

                {
                    "hash" : "hash",     (string) the block hash (same as provided)
                    "confirmations" : n,   (numeric) The number of confirmations, or -1 if the block is not on the main chain
                    "size" : n,            (numeric) The block size
                    "strippedsize" : n,    (numeric) The block size excluding witness data
                    "weight" : n           (numeric) The block weight as defined in BIP 141
                    "height" : n,          (numeric) The block height or index
                    "version" : n,         (numeric) The block version
                    "versionHex" : "00000000", (string) The block version formatted in hexadecimal
                    "merkleroot" : "xxxx", (string) The merkle root
                    "nonutxo" : [,         (array of string) Non-UTXO coinbase rewards
                    "type" n.nnnnnnnn   (numeric) Reward type and amount
                    ],
                    "tx" : [               (array of string) The transaction ids
                    "transactionid"     (string) The transaction id
                    ,...
                    ],
                    "time" : ttt,          (numeric) The block time in seconds since epoch (Jan 1 1970 GMT)
                    "mediantime" : ttt,    (numeric) The median block time in seconds since epoch (Jan 1 1970 GMT)
                    "nonce" : n,           (numeric) The nonce
                    "bits" : "1d00ffff", (string) The bits
                    "difficulty" : x.xxx,  (numeric) The difficulty
                    "chainwork" : "xxxx",  (string) Expected number of hashes required to produce the chain up to this block (in hex)
                    "nTx" : n,             (numeric) The number of transactions in the block.
                    "previousblockhash" : "hash",  (string) The hash of the previous block
                    "nextblockhash" : "hash"       (string) The hash of the next block
                }

            **Result (for verbosity = 2):** \n

            .. code-block:: text

                {
                    ...,            Same output as verbosity = 1.
                    "tx" : [        (array of Objects) The transactions in the format of the getrawtransaction RPC. Different from verbosity = 1 "tx" result.
                    ,...
                    ],
                    ,...            Same output as verbosity = 1.
                }

        :example:

            >>> node.blockchain.getblock("ffa579106ef8d396223c616b9a77b8dab22656648b55965fc9e541e864f0f9fd", 1)
        """
        return self._node._rpc.call("getblock", blockhash, verbosity)

    def getblockchaininfo(self) -> {}:  # 04
        """
        Returns an object containing various state info regarding blockchain processing.

        :return:

            .. code-block:: text

                {
                    "chain": "xxxx",              (string) current network name as defined in BIP70 (main, test, regtest)
                    "blocks": xxxxxx,             (numeric) the height of the most-work fully-validated chain. The genesis block has height 0
                    "headers": xxxxxx,            (numeric) the current number of headers we have validated
                    "bestblockhash": "...",       (string) the hash of the currently best block
                    "difficulty": xxxxxx,         (numeric) the current difficulty
                    "mediantime": xxxxxx,         (numeric) median time for the current best block
                    "verificationprogress": xxxx, (numeric) estimate of verification progress [0..1]
                    "initialblockdownload": xxxx, (bool) (debug information) estimate of whether this node is in Initial Block Download mode.
                    "chainwork": "xxxx"           (string) total amount of work in active chain, in hexadecimal
                    "size_on_disk": xxxxxx,       (numeric) the estimated size of the block and undo files on disk
                    "pruned": xx,                 (boolean) if the blocks are subject to pruning
                    "pruneheight": xxxxxx,        (numeric) lowest-height complete block stored (only present if pruning is enabled)
                    "automatic_pruning": xx,      (boolean) whether automatic pruning is enabled (only present if pruning is enabled)
                    "prune_target_size": xxxxxx,  (numeric) the target size used by pruning (only present if automatic pruning is enabled)
                    "softforks": {                (object) status of softforks
                        "xxxx" : {                 (string) name of the softfork
                            "type": "xxxx",         (string) one of "buried", "bip9"
                            "bip9": {               (object) status of bip9 softforks (only for "bip9" type)
                                "status": "xxxx",    (string) one of "defined", "started", "locked_in", "active", "failed"
                                "bit": xx,           (numeric) the bit (0-28) in the block version field used to signal this softfork (only for "started" status)
                                "startTime": xx,     (numeric) the minimum median time past of a block at which the bit gains its meaning
                                "timeout": xx,       (numeric) the median time past of a block at which the deployment is considered failed if not yet locked in
                                "since": xx,         (numeric) height of the first block to which the status applies
                                "statistics": {      (object) numeric statistics about BIP9 signalling for a softfork
                                    "period": xx,     (numeric) the length in blocks of the BIP9 signalling period
                                    "threshold": xx,  (numeric) the number of blocks with the version bit set required to activate the feature
                                    "elapsed": xx,    (numeric) the number of blocks elapsed since the beginning of the current period
                                    "count": xx,      (numeric) the number of blocks with the version bit set in the current period
                                    "possible": xx    (boolean) returns false if there are not enough blocks left in this period to pass activation threshold
                                }
                            },
                                "height": "xxxxxx",     (numeric) height of the first block which the rules are or will be enforced (only for "buried" type, or "bip9" type with "active" status)
                                "active": xx,           (boolean) true if the rules are enforced for the mempool and the next block
                        }
                    }
                    "warnings" : "...",           (string) any network and blockchain warnings.
                }

        :example:

            >>> node.blockchain.getblockchaininfo()

        """
        return self._node._rpc.call("getblockchaininfo")

    def getblockcount(self) -> int:  # 05
        """
        Returns the height of the most-work fully-validated chain.
        The genesis block has height 0.

        :return: n (numeric) The current block count

        :example:

            >>> node.blockchain.getblockcount()
        """
        return self._node._rpc.call("getblockcount")

    def getblockfilter(self, blockhash: str, filtertype: str ="basic") -> {}:  # 06
        """
        Retrieve a BIP 157 content filter for a particular block.

        :param blockhash: (required) The hash of the block
        :type blockhash: str
        :param filtertype: (optional) The type name of the filter
        :type filtertype: str
        :return:

            .. code-block:: text

                {
                    "filter" : (string) the hex-encoded filter data
                    "header" : (string) the hex-encoded filter header
                }

        :example:

            >>> node.blockchain.getblockfilter("ffa579106ef8d396223c616b9a77b8dab22656648b55965fc9e541e864f0f9fd", "basic")
        """
        return self._node._rpc.call("getblockfilter", blockhash, filtertype)

    def getblockhash(self, height: int) -> str:  # 07
        """
        Returns hash of block in best-block-chain at height provided.

        :param height: (required) The height index
        :type height: int
        :return: "hash" (string) The block hash

        :example:

            >>> node.blockchain.getblockhash(0)
        """
        return self._node._rpc.call("getblockhash", height)

    def getblockheader(self, blockhash: str, verbose: bool = True):  # 08
        """
        If verbose is false, returns a string that is serialized, hex-encoded data for blockheader 'hash'.

        If verbose is true, returns an Object with information about blockheader <hash>.

        :param blockhash: (required) The block hash
        :type blockhash: str
        :param verbose: (optional) true for a json object, false for the hex-encoded data
        :type verbose: bool
        :return:

            **Result (for verbose = true):**

            .. code-block:: text

                {
                    "hash" : "hash",     (string) the block hash (same as provided)
                    "confirmations" : n,   (numeric) The number of confirmations, or -1 if the block is not on the main chain
                    "height" : n,          (numeric) The block height or index
                    "version" : n,         (numeric) The block version
                    "versionHex" : "00000000", (string) The block version formatted in hexadecimal
                    "merkleroot" : "xxxx", (string) The merkle root
                    "time" : ttt,          (numeric) The block time in seconds since epoch (Jan 1 1970 GMT)
                    "mediantime" : ttt,    (numeric) The median block time in seconds since epoch (Jan 1 1970 GMT)
                    "nonce" : n,           (numeric) The nonce
                    "bits" : "1d00ffff", (string) The bits
                    "difficulty" : x.xxx,  (numeric) The difficulty
                    "chainwork" : "0000...1f3"     (string) Expected number of hashes required to produce the current chain (in hex)
                    "nTx" : n,             (numeric) The number of transactions in the block.
                    "previousblockhash" : "hash",  (string) The hash of the previous block
                    "nextblockhash" : "hash",      (string) The hash of the next block
                }

            **Result (for verbose = false):**
            "data" (string) A string that is serialized, hex-encoded data for block 'hash'.

        :example:

            >>> node.blockchain.getblockheader("ffa579106ef8d396223c616b9a77b8dab22656648b55965fc9e541e864f0f9fd", True)
        """
        return self._node._rpc.call("getblockheader", blockhash, verbose)

    def getblockstats(self, hash_or_height: str or int, stats: [] = None) -> {}:  # 09
        """
        Compute per block statistics for a given window. All amounts are in satoshis.

        It won't work for some heights with pruning.

        :param hash_or_height: (required) The block hash or height of the target block
        :type hash_or_height: str or int
        :param stats: (optional) Values to plot (see result below)

            .. code-block:: text

                [
                    "height",     (string) Selected statistic
                    "time",       (string) Selected statistic
                    ...
                ]
        :type stats: array
        :return:

            .. code-block:: text

                {                             (json object)
                    "avgfee": xxxxx,          (numeric) Average fee in the block
                    "avgfeerate": xxxxx,      (numeric) Average feerate (in satoshis per virtual byte)
                    "avgtxsize": xxxxx,       (numeric) Average transaction size
                    "blockhash": xxxxx,       (string) The block hash (to check for potential reorgs)
                    "feerate_percentiles": [  (array of numeric) Feerates at the 10th, 25th, 50th, 75th, and 90th percentile weight unit (in satoshis per virtual byte)
                        "10th_percentile_feerate",      (numeric) The 10th percentile feerate
                        "25th_percentile_feerate",      (numeric) The 25th percentile feerate
                        "50th_percentile_feerate",      (numeric) The 50th percentile feerate
                        "75th_percentile_feerate",      (numeric) The 75th percentile feerate
                        "90th_percentile_feerate",      (numeric) The 90th percentile feerate
                    ],
                    "height": xxxxx,          (numeric) The height of the block
                    "ins": xxxxx,             (numeric) The number of inputs (excluding coinbase)
                    "maxfee": xxxxx,          (numeric) Maximum fee in the block
                    "maxfeerate": xxxxx,      (numeric) Maximum feerate (in satoshis per virtual byte)
                    "maxtxsize": xxxxx,       (numeric) Maximum transaction size
                    "medianfee": xxxxx,       (numeric) Truncated median fee in the block
                    "mediantime": xxxxx,      (numeric) The block median time past
                    "mediantxsize": xxxxx,    (numeric) Truncated median transaction size
                    "minfee": xxxxx,          (numeric) Minimum fee in the block
                    "minfeerate": xxxxx,      (numeric) Minimum feerate (in satoshis per virtual byte)
                    "mintxsize": xxxxx,       (numeric) Minimum transaction size
                    "outs": xxxxx,            (numeric) The number of outputs
                    "subsidy": xxxxx,         (numeric) The block subsidy
                    "swtotal_size": xxxxx,    (numeric) Total size of all segwit transactions
                    "swtotal_weight": xxxxx,  (numeric) Total weight of all segwit transactions divided by segwit scale factor (4)
                    "swtxs": xxxxx,           (numeric) The number of segwit transactions
                    "time": xxxxx,            (numeric) The block time
                    "total_out": xxxxx,       (numeric) Total amount in all outputs (excluding coinbase and thus reward [ie subsidy + totalfee])
                    "total_size": xxxxx,      (numeric) Total size of all non-coinbase transactions
                    "total_weight": xxxxx,    (numeric) Total weight of all non-coinbase transactions divided by segwit scale factor (4)
                    "totalfee": xxxxx,        (numeric) The fee total
                    "txs": xxxxx,             (numeric) The number of transactions (excluding coinbase)
                    "utxo_increase": xxxxx,   (numeric) The increase/decrease in the number of unspent outputs
                    "utxo_size_inc": xxxxx,   (numeric) The increase/decrease in size for the utxo index (not discounting op_return and similar)
                }

        :example:

            >>> node.blockchain.getblockstats("ffa579106ef8d396223c616b9a77b8dab22656648b55965fc9e541e864f0f9fd", ["height", time])
        """
        return self._node._rpc.call("getblockstats", hash_or_height, stats)

    def getchaintips(self) -> {}:  # 10
        """
        Return information about all known tips in the block tree, including the main chain as well as orphaned branches.

        :return:

            .. code-block:: text

                [
                    {
                        "height": xxxx,         (numeric) height of the chain tip
                        "hash": "xxxx",         (string) block hash of the tip
                        "branchlen": 0          (numeric) zero for main chain
                        "status": "active"      (string) "active" for the main chain
                    },
                    {
                        "height": xxxx,
                        "hash": "xxxx",
                        "branchlen": 1          (numeric) length of branch connecting the tip to the main chain
                        "status": "xxxx"        (string) status of the chain (active, valid-fork, valid-headers, headers-only, invalid)
                    }
                ]

            **Possible values for status:**

            1. "invalid"               This branch contains at least one invalid block
            2. "headers-only"          Not all blocks for this branch are available, but the headers are valid
            3. "valid-headers"         All blocks are available for this branch, but they were never fully validated
            4. "valid-fork"            This branch is not part of the active chain, but is fully validated
            5. "active"


        :example:

            >>> node.blockchain.getchaintips()
        """
        return self._node._rpc.call("getchaintips")

    def getchaintxstats(self, nblocks=86400, blockhash=None):  # 11
        return self._node._rpc.call("getchaintxstats", nblocks, blockhash)

    def getdifficulty(self):  # 12
        return self._node._rpc.call("getdifficulty")

    def getgov(self, name):  # 13
        return self._node._rpc.call("getgov", name)

    def getmempoolancestors(self, txid, verbose=False):  # 14
        return self._node._rpc.call("getmempoolancestors", txid, verbose)

    def getmempooldescendants(self, txid, verbose=False):  # 15
        return self._node._rpc.call("getmempooldescendants", txid, verbose)

    def getmempoolentry(self, txid):  # 16
        return self._node._rpc.call("getmempoolentry", txid)

    def getmempoolinfo(self):  # 17
        return self._node._rpc.call("getmempoolinfo")

    def getrawmempool(self, verbose=False):  # 18
        return self._node._rpc.call("getrawmempool", verbose)

    def gettxout(self, txid, n, include_mempool=True):  # 19
        return self._node._rpc.call("gettxout", txid, n, include_mempool)

    def gettxoutproof(self, txids, blockhash=None):  # 20
        return self._node._rpc.call("gettxoutproof", txids, blockhash)

    def gettxoutsetinfo(self):  # 21
        return self._node._rpc.call("gettxoutsetinfo")

    def isappliedcustomtx(self, txid, blockHeight):  # 22
        return self._node._rpc.call("isappliedcustomtx", txid, blockHeight)

    def listgovs(self, prefix=None):  # 23
        return self._node._rpc.call("listgovs", prefix)

    def listsmartcontracts(self):
        return self._node._rpc.call("listsmartcontracts")  # 24

    def preciousblock(self, blockhash):  # 25
        return self._node._rpc.call("preciousblock", blockhash)

    def pruneblockchain(self, height):  # 26
        return self._node._rpc.call("pruneblockchain", height)

    def savemempool(self):  # 27
        return self._node._rpc.call("savemempool")

    def scantxoutset(self, action, scanobjects):  # 28
        return self._node._rpc.call("scantxoutset", action, scanobjects)

    def setgov(self, variables, inputs=None):  # 29
        return self._node._rpc.call("setgov", variables, inputs)

    def setgovheight(self, variables, height, inputs=None):  # 30
        return self._node._rpc.call("setgovheight", variables, height, inputs)

    def verifychain(self, checklevel=3, nblocks=6):  # 31
        return self._node._rpc.call("verifychain", checklevel, nblocks)

    def verifytxoutproof(self, proof):  # 32
        return self._node._rpc.call("verifytxoutproof", proof)
