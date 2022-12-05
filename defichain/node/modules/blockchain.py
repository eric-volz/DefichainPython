class Blockchain:
    def __init__(self, node):
        self._node = node

    def clearmempool(self) -> []:  # 01
        """
        Clears the memory pool and returns a list of the removed transactions.

        :return: [...] (array) -- returns list of removed transactions

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

        :return: "hash" (string) -- the block hash, hex-encoded

        :example:

            >>> node.blockchain.getbestblockhash()
        """
        return self._node._rpc.call("getbestblockhash")

    def getblock(self, blockhash: str, verbosity: int = 1) -> str or {}:  # 03
        """
        If verbosity is 0, returns a string that is serialized, hex-encoded data for block 'hash'.

        If verbosity is 1, returns an Object with information about block <hash>.

        If verbosity is 2, returns an Object with information about block <hash> and information about each transaction.

        :param blockhash: (required) The block hash
        :type blockhash: str
        :param verbosity: (optional) 0 for hex-encoded data, 1 for a json object, and 2 for json object with transaction data
        :type verbosity: int
        :return: "hex" (string) if verbosity == 0 | {...} (json) if verbosity == 1

            **Result (for verbosity = 0):**

            "hex" (string) -- A string that is serialized, hex-encoded data for block 'hash'.

            **Result (for verbosity = 1):**

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

        :return: {...} (json) -- returns blockchain information

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

        :return: n (numeric) -- The current block count

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
        :return: {...} (json) -- returns block filter

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
        :return: "hash" (string) -- The block hash

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
        :return: {...} (json) -- if verbose == true | "hex" (string) -- if verbose == false

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
            "hex" (string) -- A string that is serialized, hex-encoded data for block 'hash'.

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
        :return: {...} (json) -- returns block stats

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

        :return: {...} (json) -- returns information abaut knows tips in a block

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

    def getchaintxstats(self, nblocks: int = 86400, blockhash: str = None) -> {}:  # 11
        """
        Compute statistics about the total number and rate of transactions in the chain.

        :param nblocks: (optional) Size of the window in number of blocks
        :type nblocks: int
        :param blockhash: (optional) The hash of the block that ends the window.
        :type blockhash: str
        :return: {...} (json) -- returns statistics about the rate of transactions in the chain

            .. code-block:: text

                {
                    "time": xxxxx,                         (numeric) The timestamp for the final block in the window in UNIX format.
                    "txcount": xxxxx,                      (numeric) The total number of transactions in the chain up to that point.
                    "window_final_block_hash": "...",      (string) The hash of the final block in the window.
                    "window_final_block_height": xxxxx,    (numeric) The height of the final block in the window.
                    "window_block_count": xxxxx,           (numeric) Size of the window in number of blocks.
                    "window_tx_count": xxxxx,              (numeric) The number of transactions in the window. Only returned if "window_block_count" is > 0.
                    "window_interval": xxxxx,              (numeric) The elapsed time in the window in seconds. Only returned if "window_block_count" is > 0.
                    "txrate": x.xx,                        (numeric) The average rate of transactions per second in the window. Only returned if "window_interval" is > 0.
                }

        :example:

            >>> node.blockchain.getchaintxstats()
        """
        return self._node._rpc.call("getchaintxstats", nblocks, blockhash)

    def getdifficulty(self) -> float:  # 12
        """
        Returns the proof-of-work difficulty as a multiple of the minimum difficulty.

        :return: n.nnn (numeric) -- the proof-of-work difficulty as a multiple of the minimum difficulty.

        :example:

            >>> node.blockchain.getdifficulty()
        """
        return self._node._rpc.call("getdifficulty")

    def getgov(self, name: str) -> {}:  # 13
        """
        Returns information about governance variable:

        ATTRIBUTES, ICX_TAKERFEE_PER_BTC, LP_DAILY_LOAN_TOKEN_REWARD, LP_LOAN_TOKEN_SPLITS, LP_DAILY_DFI_REWARD,
        LOAN_LIQUIDATION_PENALTY, LP_SPLITS, ORACLE_BLOCK_INTERVAL, ORACLE_DEVIATION

        :param name: (optional) Variable name
        :type name: str
        :return: {id:{...}} (json) -- Json object with variable information

        :example:

            >>> node.blockchain.getgov("LP_SPLITS")
        """
        return self._node._rpc.call("getgov", name)

    def getmempoolancestors(self, txid: str, verbose: bool = False) -> []:  # 14
        """
        If txid is in the mempool, returns all in-mempool ancestors.

        :param txid: (required) The transaction id (must be in mempool)
        :type txid: str
        :param verbose: (optional) True for a json object, false for array of transaction ids
        :type verbose: bool
        :return: [...] (array) if verbose == false | {...} (json) -- if verbose == true

            **Result (for verbose = false):**

            .. code-block:: text

                [                       (json array of strings)
                "transactionid"           (string) The transaction id of an in-mempool ancestor transaction
                ,...
                ]

            **Result (for verbose = true):**

            .. code-block:: text

                {                           (json object)
                    "transactionid" : {     (json object)
                        "vsize" : n,            (numeric) virtual transaction size as defined in BIP 141. This is different from actual serialized size for witness transactions as witness data is discounted.
                        "size" : n,             (numeric) (DEPRECATED) same as vsize. Only returned if defid is started with -deprecatedrpc=size size will be completely removed in v0.20.
                        "weight" : n,           (numeric) transaction weight as defined in BIP 141.
                        "fee" : n,              (numeric) transaction fee in DFI (DEPRECATED)
                        "modifiedfee" : n,      (numeric) transaction fee with fee deltas used for mining priority (DEPRECATED)
                        "time" : n,             (numeric) local time transaction entered pool in seconds since 1 Jan 1970 GMT
                        "height" : n,           (numeric) block height when transaction entered pool
                        "descendantcount" : n,  (numeric) number of in-mempool descendant transactions (including this one)
                        "descendantsize" : n,   (numeric) virtual transaction size of in-mempool descendants (including this one)
                        "descendantfees" : n,   (numeric) modified fees (see above) of in-mempool descendants (including this one) (DEPRECATED)
                        "ancestorcount" : n,    (numeric) number of in-mempool ancestor transactions (including this one)
                        "ancestorsize" : n,     (numeric) virtual transaction size of in-mempool ancestors (including this one)
                        "ancestorfees" : n,     (numeric) modified fees (see above) of in-mempool ancestors (including this one) (DEPRECATED)
                        "wtxid" : hash,         (string) hash of serialized transaction, including witness data
                        "fees" : {
                            "base" : n,         (numeric) transaction fee in DFI
                            "modified" : n,     (numeric) transaction fee with fee deltas used for mining priority in DFI
                            "ancestor" : n,     (numeric) modified fees (see above) of in-mempool ancestors (including this one) in DFI
                            "descendant" : n,   (numeric) modified fees (see above) of in-mempool descendants (including this one) in DFI
                        }
                    "depends" : [           (array) unconfirmed transactions used as inputs for this transaction
                        "transactionid",    (string) parent transaction id
                    ... ]
                    "spentby" : [           (array) unconfirmed transactions spending outputs from this transaction
                        "transactionid",    (string) child transaction id
                    ... ]
                    "bip125-replaceable" : true|false,  (boolean) Whether this transaction could be replaced due to BIP125 (replace-by-fee)
                    }, ...
                }

        :example:

            >>> node.blockchain.getmempoolancestors(txid)
        """
        return self._node._rpc.call("getmempoolancestors", txid, verbose)

    def getmempooldescendants(self, txid: str, verbose: bool = False) -> []:  # 15
        """
        If txid is in the mempool, returns all in-mempool descendants.

        :param txid: (required) The transaction id (must be in mempool)
        :type txid: str
        :param verbose: (optional) True for a json object, false for array of transaction ids
        :type verbose: bool
        :return: [...] (array) if verbose == false | {...} (json) -- if verbose == true

            **Result (for verbose = false):**

            .. code-block:: text

                [                       (json array of strings)
                "transactionid"           (string) The transaction id of an in-mempool ancestor transaction
                ,...
                ]

            **Result (for verbose = true):**

            .. code-block:: text

                {                           (json object)
                    "transactionid" : {     (json object)
                        "vsize" : n,            (numeric) virtual transaction size as defined in BIP 141. This is different from actual serialized size for witness transactions as witness data is discounted.
                        "size" : n,             (numeric) (DEPRECATED) same as vsize. Only returned if defid is started with -deprecatedrpc=size size will be completely removed in v0.20.
                        "weight" : n,           (numeric) transaction weight as defined in BIP 141.
                        "fee" : n,              (numeric) transaction fee in DFI (DEPRECATED)
                        "modifiedfee" : n,      (numeric) transaction fee with fee deltas used for mining priority (DEPRECATED)
                        "time" : n,             (numeric) local time transaction entered pool in seconds since 1 Jan 1970 GMT
                        "height" : n,           (numeric) block height when transaction entered pool
                        "descendantcount" : n,  (numeric) number of in-mempool descendant transactions (including this one)
                        "descendantsize" : n,   (numeric) virtual transaction size of in-mempool descendants (including this one)
                        "descendantfees" : n,   (numeric) modified fees (see above) of in-mempool descendants (including this one) (DEPRECATED)
                        "ancestorcount" : n,    (numeric) number of in-mempool ancestor transactions (including this one)
                        "ancestorsize" : n,     (numeric) virtual transaction size of in-mempool ancestors (including this one)
                        "ancestorfees" : n,     (numeric) modified fees (see above) of in-mempool ancestors (including this one) (DEPRECATED)
                        "wtxid" : hash,         (string) hash of serialized transaction, including witness data
                        "fees" : {
                            "base" : n,         (numeric) transaction fee in DFI
                            "modified" : n,     (numeric) transaction fee with fee deltas used for mining priority in DFI
                            "ancestor" : n,     (numeric) modified fees (see above) of in-mempool ancestors (including this one) in DFI
                            "descendant" : n,   (numeric) modified fees (see above) of in-mempool descendants (including this one) in DFI
                        }
                    "depends" : [           (array) unconfirmed transactions used as inputs for this transaction
                        "transactionid",    (string) parent transaction id
                    ... ]
                    "spentby" : [           (array) unconfirmed transactions spending outputs from this transaction
                        "transactionid",    (string) child transaction id
                    ... ]
                    "bip125-replaceable" : true|false,  (boolean) Whether this transaction could be replaced due to BIP125 (replace-by-fee)
                    }, ...
                }

        :example:

            >>> node.blockchain.getmempooldescendants(txid)
        """
        return self._node._rpc.call("getmempooldescendants", txid, verbose)

    def getmempoolentry(self, txid: str) -> {}:  # 16
        """
        Returns mempool data for given transaction

        :param txid: (required) The transaction id (must be in mempool)
        :type txid: str
        :return: {...} (json) -- returns data of mempool transaction

            .. code-block:: text

                {                           (json object)
                    "vsize" : n,            (numeric) virtual transaction size as defined in BIP 141. This is different from actual serialized size for witness transactions as witness data is discounted.
                    "size" : n,             (numeric) (DEPRECATED) same as vsize. Only returned if defid is started with -deprecatedrpc=size size will be completely removed in v0.20.
                    "weight" : n,           (numeric) transaction weight as defined in BIP 141.
                    "fee" : n,              (numeric) transaction fee in DFI (DEPRECATED)
                    "modifiedfee" : n,      (numeric) transaction fee with fee deltas used for mining priority (DEPRECATED)
                    "time" : n,             (numeric) local time transaction entered pool in seconds since 1 Jan 1970 GMT
                    "height" : n,           (numeric) block height when transaction entered pool
                    "descendantcount" : n,  (numeric) number of in-mempool descendant transactions (including this one)
                    "descendantsize" : n,   (numeric) virtual transaction size of in-mempool descendants (including this one)
                    "descendantfees" : n,   (numeric) modified fees (see above) of in-mempool descendants (including this one) (DEPRECATED)
                    "ancestorcount" : n,    (numeric) number of in-mempool ancestor transactions (including this one)
                    "ancestorsize" : n,     (numeric) virtual transaction size of in-mempool ancestors (including this one)
                    "ancestorfees" : n,     (numeric) modified fees (see above) of in-mempool ancestors (including this one) (DEPRECATED)
                    "wtxid" : hash,         (string) hash of serialized transaction, including witness data
                    "fees" : {
                        "base" : n,         (numeric) transaction fee in DFI
                        "modified" : n,     (numeric) transaction fee with fee deltas used for mining priority in DFI
                        "ancestor" : n,     (numeric) modified fees (see above) of in-mempool ancestors (including this one) in DFI
                        "descendant" : n,   (numeric) modified fees (see above) of in-mempool descendants (including this one) in DFI
                    }
                    "depends" : [           (array) unconfirmed transactions used as inputs for this transaction
                        "transactionid",    (string) parent transaction id
                    ... ]
                    "spentby" : [           (array) unconfirmed transactions spending outputs from this transaction
                        "transactionid",    (string) child transaction id
                    ... ]
                    "bip125-replaceable" : true|false,  (boolean) Whether this transaction could be replaced due to BIP125 (replace-by-fee)
                }

        :example:

            >>> node.blockchain.getmempoolentry(txid)
        """
        return self._node._rpc.call("getmempoolentry", txid)

    def getmempoolinfo(self) -> {}:  # 17
        """
        Returns details on the active state of the TX memory pool.

        :return: {...} (json) -- returns details on the active state of the TX memory pool

            .. code-block:: text

                {
                    "loaded": true|false         (boolean) True if the mempool is fully loaded
                    "size": xxxxx,               (numeric) Current tx count
                    "bytes": xxxxx,              (numeric) Sum of all virtual transaction sizes as defined in BIP 141. Differs from actual serialized size because witness data is discounted
                    "usage": xxxxx,              (numeric) Total memory usage for the mempool
                    "maxmempool": xxxxx,         (numeric) Maximum memory usage for the mempool
                    "mempoolminfee": xxxxx       (numeric) Minimum fee rate in DFI/kB for tx to be accepted. Is the maximum of minrelaytxfee and minimum mempool fee
                    "minrelaytxfee": xxxxx       (numeric) Current minimum relay fee for transactions
                }

        :example:

            >>> node.blockchain.getmempoolinfo()
        """
        return self._node._rpc.call("getmempoolinfo")

    def getrawmempool(self, verbose: bool = False) -> []:  # 18
        """
        Returns all transaction ids in memory pool as a json array of string transaction ids.

        Hint: use getmempoolentry to fetch a specific transaction from the mempool.

        :param verbose: (optional) True for a json object, false for array of transaction ids
        :type verbose: bool
        :return: [...] (array) if verbose == false | {...} (json) -- if verbose == true

            **Result (for verbose = false):**

            .. code-block:: text

                [                     (json array of string)
                "transactionid"     (string) The transaction id
                ,...
                ]

            **Result (for verbose = true):**

            .. code-block:: text

                {                           (json object)
                    "transactionid" : {       (json object)
                        "vsize" : n,            (numeric) virtual transaction size as defined in BIP 141. This is different from actual serialized size for witness transactions as witness data is discounted.
                        "size" : n,             (numeric) (DEPRECATED) same as vsize. Only returned if defid is started with -deprecatedrpc=size size will be completely removed in v0.20.
                        "weight" : n,           (numeric) transaction weight as defined in BIP 141.
                        "fee" : n,              (numeric) transaction fee in DFI (DEPRECATED)
                        "modifiedfee" : n,      (numeric) transaction fee with fee deltas used for mining priority (DEPRECATED)
                        "time" : n,             (numeric) local time transaction entered pool in seconds since 1 Jan 1970 GMT
                        "height" : n,           (numeric) block height when transaction entered pool
                        "descendantcount" : n,  (numeric) number of in-mempool descendant transactions (including this one)
                        "descendantsize" : n,   (numeric) virtual transaction size of in-mempool descendants (including this one)
                        "descendantfees" : n,   (numeric) modified fees (see above) of in-mempool descendants (including this one) (DEPRECATED)
                        "ancestorcount" : n,    (numeric) number of in-mempool ancestor transactions (including this one)
                        "ancestorsize" : n,     (numeric) virtual transaction size of in-mempool ancestors (including this one)
                        "ancestorfees" : n,     (numeric) modified fees (see above) of in-mempool ancestors (including this one) (DEPRECATED)
                        "wtxid" : hash,         (string) hash of serialized transaction, including witness data
                        "fees" : {
                            "base" : n,         (numeric) transaction fee in DFI
                            "modified" : n,     (numeric) transaction fee with fee deltas used for mining priority in DFI
                            "ancestor" : n,     (numeric) modified fees (see above) of in-mempool ancestors (including this one) in DFI
                            "descendant" : n,   (numeric) modified fees (see above) of in-mempool descendants (including this one) in DFI
                        }
                        "depends" : [           (array) unconfirmed transactions used as inputs for this transaction
                            "transactionid",    (string) parent transaction id
                        ... ]
                        "spentby" : [           (array) unconfirmed transactions spending outputs from this transaction
                            "transactionid",    (string) child transaction id
                        ... ]
                        "bip125-replaceable" : true|false,  (boolean) Whether this transaction could be replaced due to BIP125 (replace-by-fee)
                    }, ...
                }

        :example:

            >>> node.blockchain.getrawmempool(False)
        """
        return self._node._rpc.call("getrawmempool", verbose)

    def gettxout(self, txid:str, n: int, include_mempool:bool = True) -> {}:  # 19
        """
        Returns details about an unspent transaction output.

        :param txid: (required) The transaction id
        :type txid: str
        :param n: (required) vout number
        :type n: int
        :param include_mempool: (optional) Whether to include the mempool. Note that an unspent output that is spent in the mempool won't appear
        :type include_mempool: bool
        :return: {...} (json) -- detatils about unsepent transactions

            .. code-block:: text

                {
                    "bestblock":  "hash",    (string) The hash of the block at the tip of the chain
                    "confirmations" : n,       (numeric) The number of confirmations
                    "value" : x.xxx,           (numeric) The transaction value in DFI
                    "scriptPubKey" : {         (json object)
                        "asm" : "code",       (string)
                        "hex" : "hex",        (string)
                        "reqSigs" : n,          (numeric) Number of required signatures
                        "type" : "pubkeyhash", (string) The type, eg pubkeyhash
                        "addresses" : [          (array of string) array of defi addresses
                            "address"     (string) defi address
                            ,...
                        ]
                    },
                    "coinbase" : true|false   (boolean) Coinbase or not
                }

        :example:

            >>> node.blockchain.gettxout(txid, 1, True)
        """
        return self._node._rpc.call("gettxout", txid, n, include_mempool)

    def gettxoutproof(self, txids: [], blockhash: str = None) -> str:  # 20
        """
        Returns a hex-encoded proof that "txid" was included in a block.

        NOTE: By default this function only works sometimes. This is when there is an
        unspent output in the utxo for this transaction. To make it always work,
        you need to maintain a transaction index, using the -txindex command line option or
        specify the block in which the transaction is included manually (by blockhash).

        :param txids: (required) A json array of txids to filter

            .. code-block:: text

                [
                    "txid",    (string) A transaction hash
                    ...
                ]

        :type txids: json array
        :param blockhash: (optional) If specified, looks for txid in the block with this hash
        :type blockhash: str
        :return: "hex" (string) -- A string that is a serialized, hex-encoded data for the proof.

        :example:

            >>> node.blockchain.gettxoutproof([txid], blockhash)
        """
        return self._node._rpc.call("gettxoutproof", txids, blockhash)

    def gettxoutsetinfo(self) -> {}:  # 21
        """
        Returns statistics about the unspent transaction output set.

        Note this call may take some time.

        :return: {...} (json) -- returns statistics about the unspent transaction output set

            .. code-block:: text

                {
                    "height":n,     (numeric) The current block height (index)
                    "bestblock": "hex",   (string) The hash of the block at the tip of the chain
                    "transactions": n,      (numeric) The number of transactions with unspent outputs
                    "txouts": n,            (numeric) The number of unspent transaction outputs
                    "bogosize": n,          (numeric) A meaningless metric for UTXO set size
                    "hash_serialized_2": "hash", (string) The serialized hash
                    "disk_size": n,         (numeric) The estimated size of the chainstate on disk
                    "total_amount": x.xxx          (numeric) The total amount
                }

        :example:

            >>> node.blockchain.gettxoutsetinfo()
        """
        return self._node._rpc.call("gettxoutsetinfo")

    def isappliedcustomtx(self, txid: str, blockHeight: int) -> bool:  # 22
        """
        Checks that custom transaction was affected on chain

        :param txid: (required) A transaction hash
        :type txid: str
        :param blockHeight: (required) The height of block which contain tx
        :type blockHeight: int
        :return: bool -- The boolean indicate that custom transaction was affected on chain

        :example:

            >>> node.blockchain.isappliedcustomtx(txid, blockHeight)
        """
        return self._node._rpc.call("isappliedcustomtx", txid, blockHeight)

    def listgovs(self, prefix: str = None) -> []:  # 23
        """
        Returns information about all governance variables including pending changes

        :param prefix: (optional) One of all, gov, attrs, live. Defaults to the all view. Any other string is treated as a prefix of attributes to filter with. `v0/` is assumed if not explicitly provided.
        :type prefix: str
        :return: [[{id:{...}},{height:{...}},...], ...] (array) -- Json array with JSON objects with variable information

        :example:

            >>> node.blockchain.listgovs("gov")
        """
        return self._node._rpc.call("listgovs", prefix)

    def listsmartcontracts(self) -> []:
        """
        Returns information on smart contracts

        :return: [{...}] -- information about smart contracts

            .. code-block:: text

                [           (array) JSON array with smart contract information
                    {
                            "name":"name"         smart contract name
                            "address":"address"   smart contract address
                            "token id":x.xxxxxxxx   smart contract balance per token
                    }
                    ...
                ]

        :example:

            >>> node.blockchain.listsmartcontracts()
        """
        return self._node._rpc.call("listsmartcontracts")  # 24

    def preciousblock(self, blockhash: str) -> None:  # 25
        """
        Treats a block as if it were received before others with the same work.

        A later preciousblock call can override the effect of an earlier one.

        The effects of preciousblock are not retained across restarts.

        :param blockhash: (required) the hash of the block to mark as precious
        :type blockhash: str
        :return: None

        :example:

            >>> node.blockchain.preciousblock(blockhash)
        """
        return self._node._rpc.call("preciousblock", blockhash)

    def pruneblockchain(self, height: int) -> int:  # 26
        """
        pruneblockchain height

        :param height: (required) The block height to prune up to. May be set to a discrete height, or a unix timestamp
            to prune blocks whose block time is at least 2 hours older than the provided timestamp.
        :type height: int
        :return: n (numeric) -- Height of the last block pruned

        :example:

            >>> node.blockchain.pruneblockchain(1000)
        """
        return self._node._rpc.call("pruneblockchain", height)

    def savemempool(self) -> None:  # 27
        """
        Dumps the mempool to disk. It will fail until the previous dump is fully loaded.

        :return: None
        :example:

            >>> node.blockchain.savemempool()
        """
        return self._node._rpc.call("savemempool")

    def scantxoutset(self, action: str, scanobjects: [{}]) -> {}:  # 28
        """
        EXPERIMENTAL warning: this call may be removed or changed in future releases.

        Scans the unspent transaction output set for entries that match certain output descriptors.

        Examples of output descriptors are:

            addr(<address>)                      Outputs whose scriptPubKey corresponds to the specified address (does not include P2PK)

            raw(<hex script>)                    Outputs whose scriptPubKey equals the specified hex scripts

            combo(<pubkey>)                      P2PK, P2PKH, P2WPKH, and P2SH-P2WPKH outputs for the given pubkey

            pkh(<pubkey>)                        P2PKH outputs for the given pubkey

            sh(multi(<n>,<pubkey>,<pubkey>,...)) P2SH-multisig outputs for the given threshold and pubkeys

        In the above, <pubkey> either refers to a fixed public key in hexadecimal notation, or to an xpub/xprv optionally followed by one
        or more path elements separated by "/", and optionally ending in "/\*" (unhardened), or "/\*'" or "/\*h" (hardened) to specify all
        unhardened or hardened child keys.

        In the latter case, a range needs to be specified by below if different from 1000.
        For more information on output descriptors, see the documentation in the doc/descriptors.md file.

        :param action: (required) The action to execute

                                  "start" for starting a scan

                                  "abort" for aborting the current scan (returns true when abort was successful)

                                  "status" for progress report (in %) of the current scan
        :type action: str
        :param scanobjects: (required) Every scan object is either a string descriptor or an object:

            .. code-block:: text

                [
                    "descriptor",             (string) An output descriptor
                    {                         (json object) An object with output descriptor and metadata
                    "desc": "str",          (string, required) An output descriptor
                    "range": n or [n,n],    (numeric or array, optional, default=1000) The range of HD chain indexes to explore (either end or [begin,end])
                    },
                    ...
                ]

        :type scanobjects: [{}]
        :return: {...} (json) -- returns entries that match certain output descriptors

            .. code-block:: text

                {
                    "unspents": [
                        {
                        "txid" : "transactionid",     (string) The transaction id
                        "vout": n,                    (numeric) the vout value
                        "scriptPubKey" : "script",    (string) the script key
                        "desc" : "descriptor",        (string) A specialized descriptor for the matched scriptPubKey
                        "amount" : x.xxx,             (numeric) The total amount in DFI of the unspent output
                        "height" : n,                 (numeric) Height of the unspent transaction output
                        }
                    ,...],
                    "total_amount" : x.xxx,          (numeric) The total amount of all found unspent outputs in DFI
                }
        """
        return self._node._rpc.call("scantxoutset", action, scanobjects)

    def setgov(self, variables: {}, inputs: [{}] = None) -> str:  # 29
        """
        Set special 'governance' variables:: ATTRIBUTES, ICX_TAKERFEE_PER_BTC, LP_LOAN_TOKEN_SPLITS, LP_SPLITS, ORACLE_BLOCK_INTERVAL, ORACLE_DEVIATION

        :param variables: (required) Object with variables

            .. code-block:: text

                {
                    "name": "str",      (string, required) Variable's name is the key, value is the data. Exact data type depends on variable's name.
                }

        :type variables: {}
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: [{}]
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.blockchain.setgov({"LP_SPLITS": {"2":0.2,"3":0.8})
        """
        return self._node._rpc.call("setgov", variables, inputs)

    def setgovheight(self, variables: {}, height: int, inputs: [{}] = None):  # 30
        """
        Change governance variable at height: ATTRIBUTES, ICX_TAKERFEE_PER_BTC, LP_LOAN_TOKEN_SPLITS, LP_SPLITS, ORACLE_DEVIATION

        :param variables: (required) Object with variable

            .. code-block:: text

                {
                    "name": "str",      (string, required)  Variable name is the key, value is the data. Exact data type depends on variable name.
                }

        :type variables: {}
        :param height: (required) Start height for the changes to take effect.
        :type height: int
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: [{}]
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.blockchain.setgovheight({"LP_SPLITS": {"2":0.2,"3":0.8}, 3000000)
        """
        return self._node._rpc.call("setgovheight", variables, height, inputs)

    def unsetgov(self, variables: {}, inputs: [{}] = None) -> str:  # 31
        """
        Unset special 'governance' variables:: ATTRIBUTES, ICX_TAKERFEE_PER_BTC, LP_LOAN_TOKEN_SPLITS, LP_SPLITS,
        ORACLE_BLOCK_INTERVAL, ORACLE_DEVIATION

        :param variables: (required) Object with variables; Variable's name is the key
        :type variables: json
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: [{}]
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.blockchain.unsetgov({"LP_SPLITS": ["2","3"]})
        """
        return self._node._rpc.call("unsetgov", variables, inputs)

    def verifychain(self, checklevel: int = 3, nblocks: int = 6) -> bool:  # 32
        """
        Verifies blockchain database.

        :param checklevel: (optional, range=0-4) How thorough the block verification is
        :type checklevel: int
        :param nblocks: (optional, 0=all) The number of blocks to check
        :type nblocks: int
        :return: true|false (boolean) -- Verified or not

        :example:

            >>> node.blockchain.verifychain()
        """
        return self._node._rpc.call("verifychain", checklevel, nblocks)

    def verifytxoutproof(self, proof: str) -> [str]:  # 33
        """
        Verifies that a proof points to a transaction in a block, returning the transaction it commits to
        and throwing an RPC error if the block is not in our best chain

        :param proof: (required) The hex-encoded proof generated by gettxoutproof
        :type proof: str
        :return: [...] (array, strings) -- The txid(s) which the proof commits to, or empty array if the proof can not be validated
        """
        return self._node._rpc.call("verifytxoutproof", proof)
