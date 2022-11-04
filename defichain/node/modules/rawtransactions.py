from ..util import BuildJson


class Rawtransactions:
    def __init__(self, node):
        self._node = node

    def analyzepsbt(self, psbt: str) -> {}:  # 01
        """
        Analyzes and provides information about the current status of a PSBT and its inputs

        :param psbt: (required) A base64 string of a PSBT
        :type psbt: str
        :return: {...} (json) -- returns information about the current status of a PSBT and its inputs

            .. code-block:: text

                {
                    "inputs" : [                            (array of json objects)
                        {
                            "has_utxo" : true|false         (boolean) Whether a UTXO is provided
                            "is_final" : true|false         (boolean) Whether the input is finalized
                            "missing" : {                   (json object, optional) Things that are missing that are required to complete this input
                                "pubkeys" : [               (array, optional)
                                    "keyid"                 (string) Public key ID, hash160 of the public key, of a public key whose BIP 32 derivation path is missing
                                ]
                                "signatures" : [            (array, optional)
                                    "keyid"                 (string) Public key ID, hash160 of the public key, of a public key whose signature is missing
                                ]
                                "redeemscript" : "hash"     (string, optional) Hash160 of the redeemScript that is missing
                                "witnessscript" : "hash"    (string, optional) SHA256 of the witnessScript that is missing
                            }
                            "next" : "role"                 (string, optional) Role of the next person that this input needs to go to
                        }
                        ,...
                    ]
                    "estimated_vsize" : vsize               (numeric, optional) Estimated vsize of the final signed transaction
                    "estimated_feerate" : feerate           (numeric, optional) Estimated feerate of the final signed transaction in DFI/kB. Shown only if all UTXO slots in the PSBT have been filled.
                    "fee" : fee                             (numeric, optional) The transaction fee paid. Shown only if all UTXO slots in the PSBT have been filled.
                    "next" : "role"                         (string) Role of the next person that this psbt needs to go to
                }

        :example:

            >>> node.rawtransactions.analyzepsbt("psbt")
        """
        return self._node._rpc.call("analyzepsbt", psbt)

    def combinepsbt(self, txs: []) -> str:  # 02
        """
        Combine multiple partially signed Defi transactions into one transaction.
        Implements the Combiner role.

        :param txs: (required) A json array of base64 strings of partially signed transactions
        :type txs: array
        :return: [...] (array) A json array of base64 strings of partially signed transactions

        :example:

            >>> node.rawtransactions.combinepsbt(["mybase64_1", "mybase64_2", "mybase64_3"])
        """
        return self._node._rpc.call("combinepsbt", txs)

    def combinerawtransaction(self, txs: []) -> str:  # 03
        """
        Combine multiple partially signed transactions into one transaction

        The combined transaction may be another partially signed transaction or a
        fully signed transaction

        :param txs: (required) A json array of hex strings of partially signed transactions
        :type txs: array
        :return: "hex" (string) -- The hex-encoded raw transaction with signature(s)

        :example:

            >>> node.rawtransactions.combinerawtransaction(["myhex1", "myhex2", "myhex3"])
        """
        return self._node._rpc.call("combinerawtransaction", txs)

    def converttopsbt(self, hexstring: str, permitsigdata: bool = False, iswitness: bool = None) -> str:  # 04
        """
        Converts a network serialized transaction to a PSBT. This should be used only with createrawtransaction and fundrawtransaction
        createpsbt and walletcreatefundedpsbt should be used for new applications.

        :param hexstring: (required)
        :type hexstring: str
        :param permitsigdata: (optional)
        :type permitsigdata: bool
        :param iswitness: (optional)
        :type iswitness: bool
        :return: "psbt" (string) -- The resulting raw transaction (base64-encoded string)

        :example:

            >>> node.rawtransactions.createrawtransaction("rawtransaction")
        """
        return self._node._rpc.call("converttopsbt", hexstring, permitsigdata, iswitness)

    def createpsbt(self, inputs: [], outputs: [], locktime: int = 0, replaceable: bool = False) -> str:  # 05
        """

        :param inputs: (required) A json array of json objects

            .. code-block:: text

                [
                    {                         (json object)
                        "txid": "hex",        (string, required) The transaction id
                        "vout": n,            (numeric, required) The output number
                        "sequence": n,        (numeric, optional, default=depends on the value of the 'replaceable' and 'locktime' arguments) The sequence number
                    },
                    ...
                ]

        :type inputs: json array
        :param outputs: (required) a json array with outputs (key-value pairs), where none of the keys are duplicated

            That is, each address can only appear once and there can only be one 'data' object.

            For compatibility reasons, a dictionary, which holds the key-value pairs directly, is also
            accepted as second parameter.

            .. code-block:: text

                [
                    {                         (json object)
                        "address": amount,    (numeric or string, required) A key-value pair. The key (string) is the DFI address, the value (float or string) is the amount in DFI
                    },
                    {                         (json object)
                        "data": "hex",        (string, required) A key-value pair. The key must be "data", the value is hex-encoded data
                    },
                    ...
                ]

        :type outputs: json array
        :param locktime: (optional) Raw locktime. Non-0 value also locktime-activates inputs
        :type locktime: int
        :param replaceable: (optional) Marks this transaction as BIP125 replaceable

            Allows this transaction to be replaced by a transaction with higher fees. If provided, it is an error
            if explicit sequence numbers are incompatible.
        :type replaceable: bool
        :return: "psbt" (string) -- The resulting raw transaction (base64-encoded string)

        :example:

            >>> node.rawtransactions.createpsbt([{\"txid\":\"myid\",\"vout\":0}], [{\"data\":\"00010203\"}])
        """
        return self._node._rpc.call("createpsbt", inputs, outputs, locktime, replaceable)

    def createrawtransaction(self, inputs: [], outputs: [], locktime: int = 0, replaceable: bool = False):  # 06
        """

        :param inputs: (required) A json array of json objects

            .. code-block:: text

                [
                    {                         (json object)
                        "txid": "hex",        (string, required) The transaction id
                        "vout": n,            (numeric, required) The output number
                        "sequence": n,        (numeric, optional, default=depends on the value of the 'replaceable' and 'locktime' arguments) The sequence number
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
                    {                         (json object)
                        "address": amount,    (numeric or string, required) A key-value pair. The key (string) is the DFI address, the value (float or string) is the amount in DFI
                    },
                    {                         (json object)
                        "data": "hex",        (string, required) A key-value pair. The key must be "data", the value is hex-encoded data
                    },
                    ...
                ]

        :type outputs: json array
        :param locktime: (optional) Raw locktime. Non-0 value also locktime-activates inputs
        :type locktime: int
        :param replaceable: (optional) arks this transaction as BIP125-replaceable.

            Allows this transaction to be replaced by a transaction with higher fees.
            If provided, it is an error if explicit sequence numbers are incompatible.
        :type replaceable: bool
        :return: "hex" (string) -- hex string of the transaction
        """
        return self._node._rpc.call("createrawtransaction", inputs, outputs, locktime, replaceable)

    def decodepsbt(self, psbt: str) -> {}:  # 07
        """
        Return a JSON object representing the serialized, base64-encoded partially signed Defi transaction.

        :param psbt: (required) The PSBT base64 string
        :type psbt: str
        :return: {...} (json) -- returns json object

            .. code-block:: text

                {
                    "tx" : {                   (json object) The decoded network-serialized unsigned transaction.
                        ...                                      The layout is the same as the output of decoderawtransaction.
                    },
                    "unknown" : {                (json object) The unknown global fields
                        "key" : "value"            (key-value pair) An unknown key-value pair
                        ...
                    },
                    "inputs" : [                 (array of json objects)
                        {
                            "non_witness_utxo" : {   (json object, optional) Decoded network transaction for non-witness UTXOs
                            ...
                            },
                            "witness_utxo" : {            (json object, optional) Transaction output for witness UTXOs
                                "amount" : x.xxx,           (numeric) The value in DFI
                                "scriptPubKey" : {          (json object)
                                    "asm" : "asm",            (string) The asm
                                    "hex" : "hex",            (string) The hex
                                    "type" : "pubkeyhash",    (string) The type, eg 'pubkeyhash'
                                    "address" : "address"     (string) Defi address if there is one
                                }
                            },
                            "partial_signatures" : {             (json object, optional)
                                "pubkey" : "signature",           (string) The public key and signature that corresponds to it.
                            ,...
                            }
                            "sighash" : "type",                  (string, optional) The sighash type to be used
                            "redeem_script" : {       (json object, optional)
                                "asm" : "asm",            (string) The asm
                                "hex" : "hex",            (string) The hex
                                "type" : "pubkeyhash",    (string) The type, eg 'pubkeyhash'
                            }
                            "witness_script" : {       (json object, optional)
                                "asm" : "asm",            (string) The asm
                                "hex" : "hex",            (string) The hex
                                "type" : "pubkeyhash",    (string) The type, eg 'pubkeyhash'
                            }
                            "bip32_derivs" : {          (json object, optional)
                                "pubkey" : {                     (json object, optional) The public key with the derivation path as the value.
                                    "master_fingerprint" : "fingerprint"     (string) The fingerprint of the master key
                                    "path" : "path",                         (string) The path
                                }
                                ,...
                            }
                            "final_scriptsig" : {       (json object, optional)
                                "asm" : "asm",            (string) The asm
                                "hex" : "hex",            (string) The hex
                            }
                            "final_scriptwitness": ["hex", ...] (array of string) hex-encoded witness data (if any)
                            "unknown" : {                (json object) The unknown global fields
                                "key" : "value"            (key-value pair) An unknown key-value pair
                                ...
                            },
                        }
                        ,...
                    ]
                    "outputs" : [                 (array of json objects)
                        {
                            "redeem_script" : {       (json object, optional)
                                "asm" : "asm",            (string) The asm
                                "hex" : "hex",            (string) The hex
                                "type" : "pubkeyhash",    (string) The type, eg 'pubkeyhash'
                            }
                            "witness_script" : {       (json object, optional)
                                "asm" : "asm",            (string) The asm
                                "hex" : "hex",            (string) The hex
                                "type" : "pubkeyhash",    (string) The type, eg 'pubkeyhash'
                            }
                            "bip32_derivs" : [          (array of json objects, optional)
                                {
                                "pubkey" : "pubkey",                     (string) The public key this path corresponds to
                                "master_fingerprint" : "fingerprint"     (string) The fingerprint of the master key
                                "path" : "path",                         (string) The path
                                }
                                }
                                ,...
                            ],
                            "unknown" : {                (json object) The unknown global fields
                            "key" : "value"            (key-value pair) An unknown key-value pair
                            ...
                            },
                        }
                        ,...
                    ]
                    "fee" : fee                      (numeric, optional) The transaction fee paid if all UTXOs slots in the PSBT have been filled.
                }

        :example:

            >>> node.rawtransactions.decodepsbt("psbt")
        """
        return self._node._rpc.call("decodepsbt", psbt)

    def decoderawtransaction(self, hexstring: str, iswitness: bool = None) -> {}:  # 08
        """
        Return a JSON object representing the serialized, hex-encoded transaction

        :param hexstring: (required) The transaction hex string
        :type hexstring: str
        :param iswitness: (optional) Whether the transaction hex is a serialized witness transaction.

            If iswitness is not present, heuristic tests will be used in decoding.

            If true, only witness deserialization will be tried.

            If false, only non-witness deserialization will be tried.

            This boolean should reflect whether the transaction has inputs

            (e.g. fully valid, or on-chain transactions), if known by the caller.
        :type iswitness: bool
        :return: {...} (json) -- returns decodes raw transaction

            .. code-block:: text

                {
                    "txid" : "id",        (string) The transaction id
                    "hash" : "id",        (string) The transaction hash (differs from txid for witness transactions)
                    "size" : n,             (numeric) The transaction size
                    "vsize" : n,            (numeric) The virtual transaction size (differs from size for witness transactions)
                    "weight" : n,           (numeric) The transaction's weight (between vsize*4 - 3 and vsize*4)
                    "version" : n,          (numeric) The version
                    "locktime" : ttt,       (numeric) The lock time
                    "vin" : [               (array of json objects)
                        {
                            "txid": "id",    (string) The transaction id
                            "vout": n,         (numeric) The output number
                            "scriptSig": {     (json object) The script
                            "asm": "asm",  (string) asm
                            "hex": "hex"   (string) hex
                        },
                            "txinwitness": ["hex", ...] (array of string) hex-encoded witness data (if any)
                            "sequence": n     (numeric) The script sequence number
                        }
                        ,...
                    ],
                    "vout" : [             (array of json objects)
                        {
                            "value" : x.xxx,            (numeric) The value in DFI
                            "n" : n,                    (numeric) index
                            "scriptPubKey" : {          (json object)
                                "asm" : "asm",          (string) the asm
                                "hex" : "hex",          (string) the hex
                                "reqSigs" : n,            (numeric) The required sigs
                                "type" : "pubkeyhash",  (string) The type, eg 'pubkeyhash'
                                "addresses" : [           (json array of string)
                                    "12tvKAXCxZjSmdNbao16dKXC8tRWfcF5oc"   (string) defi address
                                    ,...
                                ]
                            }
                        }
                        ,...
                    ],
                }

        :example:

            >>> node.rawtransactions.decoderawtransaction("hexstring")
        """
        return self._node._rpc.call("decoderawtransaction", hexstring, iswitness)

    def decodescript(self, hexstring: str) -> {}:  # 09
        """
        Decode a hex-encoded script

        :param hexstring: (required) the hex-encoded script
        :type hexstring: str
        :return: {...} (json) -- returns the decodes script

            .. code-block:: text

                {
                    "asm":"asm",          (string) Script public key
                    "type":"type",        (string) The output type (e.g. nonstandard, pubkey, pubkeyhash, scripthash, multisig, nulldata, witness_v0_scripthash, witness_v0_keyhash, witness_unknown)
                    "reqSigs": n,         (numeric) The required signatures
                    "addresses": [        (json array of string)
                        "address"          (string) defi address
                        ,...
                    ],
                    "p2sh":"str"          (string) address of P2SH script wrapping this redeem script (not returned if the script is already a P2SH).
                    "segwit": {           (json object) Result of a witness script public key wrapping this redeem script (not returned if the script is a P2SH or witness).
                        "asm":"str",        (string) String representation of the script public key
                        "hex":"hexstr",     (string) Hex string of the script public key
                        "type":"str",       (string) The type of the script public key (e.g. witness_v0_keyhash or witness_v0_scripthash)
                        "reqSigs": n,       (numeric) The required signatures (always 1)
                        "addresses": [      (json array of string) (always length 1)
                            "address"         (string) segwit address
                            ,...
                        ],
                        "p2sh-segwit":"str" (string) address of the P2SH script wrapping this witness redeem script.
                    }
                }

        :example:

            >>> node.rawtransactions.decodescript("hexstring")
        """
        return self._node._rpc.call("decodescript", hexstring)

    def finalizepsbt(self, psbt: str, extract: bool = True) -> {}:  # 10
        """
        Finalize the inputs of a PSBT. If the transaction is fully signed, it will produce a
        network serialized transaction which can be broadcast with sendrawtransaction. Otherwise a PSBT will be
        created which has the final_scriptSig and final_scriptWitness fields filled for inputs that are complete.
        Implements the Finalizer and Extractor roles.

        :param psbt: (required) A base64 string of a PSBT
        :type psbt: str
        :param extract: (optional) If true and the transaction is complete, extract and return the complete transaction
            in normal network serialization instead of the PSBT.
        :type extract: bool
        :return: {...} (json) -- returns a finalized psbt

            .. code-block:: text

                {
                    "psbt" : "value",          (string) The base64-encoded partially signed transaction if not extracted
                    "hex" : "value",           (string) The hex-encoded network transaction if extracted
                    "complete" : true|false,   (boolean) If the transaction has a complete set of signatures
                }

        :example:

            >>> node.rawtransactions.finalizepsbt("psbt")
        """
        return self._node._rpc.call("finalizepsbt", psbt, extract)

    def fundrawtransaction(self, hexstring: str, changeAddress: str = None, changePosition: int = None,
                           change_type: str = None, includeWatching: bool = True, lockUnspents: bool = False,
                           feeRate: float = None, subtractFeeFromOutputs: [] = None, replaceable: bool = None,
                           conf_target: int = None, estimate_mode: str = None, iswitness: bool = None) -> {}:  # 11
        """
        Add inputs to a transaction until it has enough in value to meet its out value.

        This will not modify existing inputs, and will add at most one change output to the outputs.

        No existing outputs will be modified unless "subtractFeeFromOutputs" is specified.

        Note that inputs which were signed may need to be resigned after completion since in/outputs have been added.

        The inputs added will not be signed, use signrawtransactionwithkey or signrawtransactionwithwallet for that.

        Note that all existing inputs must have their previous output transaction be in the wallet.

        Note that all inputs selected must be of standard form and P2SH scripts must be
        in the wallet using importaddress or addmultisigaddress (to calculate fees).
        You can see whether this is the case by checking the "solvable" field in the listunspent output.

        Only pay-to-pubkey, multisig, and P2SH versions thereof are currently supported for watch-only.

        :param hexstring: (required) The hex string of the raw transaction
        :type hexstring: str
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
        :param subtractFeeFromOutputs: (optional) A json array of integers

            .. code-block:: text

                [
                                    The fee will be equally deducted from the amount of each specified output.
                                    Those recipients will receive less defis than you enter in their corresponding amount field.
                                    If no outputs are specified here, the sender pays the fee.
                vout_index,         (numeric) The zero-based output index, before a change output is added.
                    ...
                ]

        :type subtractFeeFromOutputs: json array
        :param replaceable: (optional)  Marks this transaction as BIP125 replaceable
        :type replaceable: bool
        :param conf_target: (optional) Confirmation target (in blocks)
        :type conf_target: int
        :param estimate_mode: (optional) The fee estimate mode, must be one of:

                                      "UNSET"

                                      "ECONOMICAL"

                                      "CONSERVATIVE"
        :type estimate_mode: str
        :param iswitness: (optional) Whether the transaction hex is a serialized witness transaction

            If iswitness is not present, heuristic tests will be used in decoding.

            If true, only witness deserialization will be tried.

            If false, only non-witness deserialization will be tried.

            This boolean should reflect whether the transaction has inputs

            (e.g. fully valid, or on-chain transactions), if known by the caller
        :type iswitness: bool
        :return: {...} (json) -- returns json with transaction hex and extra parameters

            .. code-block:: text

                {
                    "hex":       "value",   (string)  The resulting raw transaction (hex-encoded string)
                    "fee":       n,         (numeric) Fee in DFI the resulting transaction pays
                    "changepos": n          (numeric) The position of the added change output, or -1
                }

        :example:

            >>> node.rawtransactions.fundrawtransaction("rawtransactionhex")
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
        return self._node._rpc.call("fundrawtransaction", hexstring, options.build(), iswitness)

    def getrawtransaction(self, txid: str, verbose: bool = False, blockhash: str = None) -> {}:  # 12
        """
        Return the raw transaction data.

        By default this function only works for mempool transactions. When called with a blockhash
        argument, getrawtransaction will return the transaction if the specified block is available and
        the transaction is found in that block. When called without a blockhash argument, getrawtransaction
        will return the transaction if it is in the mempool, or if -txindex is enabled and the transaction
        is in a block in the blockchain.

        Hint: Use gettransaction for wallet transactions.

        If verbose is 'true', returns an Object with information about 'txid'.

        If verbose is 'false' or omitted, returns a string that is serialized, hex-encoded data for 'txid'.

        :param txid: (required) The transaction id
        :type txid: str
        :param verbose: (optional) If false, return a string, otherwise return a json object
        :type verbose: bool
        :param blockhash: (optional) The block in which to look for the transaction
        :type blockhash: str
        :return: hex (string) if verbose == true | {...} (json) -- if verbose == flase

            **Result (for verbose = true):**

            "hex" (string) -- The serialized, hex-encoded data for 'txid'

            **Result (for verbose = false):**

            .. code-block:: text

                {
                    "in_active_chain": b, (bool) Whether specified block is in the active chain or not (only present with explicit "blockhash" argument)
                    "hex" : "data",       (string) The serialized, hex-encoded data for 'txid'
                    "txid" : "id",        (string) The transaction id (same as provided)
                    "hash" : "id",        (string) The transaction hash (differs from txid for witness transactions)
                    "size" : n,             (numeric) The serialized transaction size
                    "vsize" : n,            (numeric) The virtual transaction size (differs from size for witness transactions)
                    "weight" : n,           (numeric) The transaction's weight (between vsize*4-3 and vsize*4)
                    "version" : n,          (numeric) The version
                    "locktime" : ttt,       (numeric) The lock time
                    "vin" : [               (array of json objects)
                        {
                            "txid": "id",    (string) The transaction id
                            "vout": n,         (numeric)
                            "scriptSig": {     (json object) The script
                                "asm": "asm",  (string) asm
                                "hex": "hex"   (string) hex
                            },
                            "sequence": n      (numeric) The script sequence number
                            "txinwitness": ["hex", ...] (array of string) hex-encoded witness data (if any)
                        }
                        ,...
                    ],
                    "vout" : [              (array of json objects)
                        {
                            "value" : x.xxx,            (numeric) The value in DFI
                            "n" : n,                    (numeric) index
                            "scriptPubKey" : {          (json object)
                                "asm" : "asm",          (string) the asm
                                "hex" : "hex",          (string) the hex
                                "reqSigs" : n,            (numeric) The required sigs
                                "type" : "pubkeyhash",  (string) The type, eg 'pubkeyhash'
                                "addresses" : [           (json array of string)
                                    "address"        (string) defi address
                                ,...
                                ]
                            }
                        }
                        ,...
                    ],
                    "blockhash" : "hash",   (string) the block hash
                    "confirmations" : n,      (numeric) The confirmations
                    "blocktime" : ttt         (numeric) The block time in seconds since epoch (Jan 1 1970 GMT)
                    "time" : ttt,             (numeric) Same as "blocktime"
                }
        :example:

            >>> node.rawtransactions.getrawtransaction("txid")
        """
        return self._node._rpc.call("getrawtransaction", txid, verbose, blockhash)

    def joinpsbts(self, txs: []) -> str:  # 13
        """
        Joins multiple distinct PSBTs with different inputs and outputs into one PSBT with inputs and outputs from
        all of the PSBTs.

        No input in any of the PSBTs can be in more than one of the PSBTs.

        :param txs: (required) A json array of base64 strings of partially signed transactions
        :type txs: array
        :return: "psbt" (string) -- The base64-encoded partially signed transaction

        :example:

            >>> node.rawtransactions.joinpsbts(["psbt"])
        """
        return self._node._rpc.call("joinpsbts", txs)

    def sendrawtransaction(self, hexstring: str, maxfeerate: float = 0.10) -> str:  # 14
        """
        Submit a raw transaction (serialized, hex-encoded) to local node and network.

        Note that the transaction will be sent unconditionally to all peers, so using this
        for manual rebroadcast may degrade privacy by leaking the transaction's origin, as
        nodes will normally not rebroadcast non-wallet transactions already in their mempool.

        Also see createrawtransaction and signrawtransactionwithkey calls.

        :param hexstring: (required) The hex string of the raw transaction
        :type hexstring: str
        :param maxfeerate: (optional) Reject transactions whose fee rate is higher than the specified value, expressed in DFI/kB.
            Set to 0 to accept any fee rate
        :type maxfeerate: float
        :return: "hex" (string) -- The transaction hash in hex

        :example:

            >>> node.rawtransactions.sendrawtransaction("signedhex")
        """
        return self._node._rpc.call("sendrawtransaction", hexstring, maxfeerate)

    def signrawtransactionwithkey(self, hexstring: str, privatekey: [], prevtxs: [] = [], sighashtype: str = "ALL") -> {}:  # 15
        """
        Sign inputs for raw transaction (serialized, hex-encoded).

        The second argument is an array of base58-encoded private
        keys that will be the only keys used to sign the transaction.

        The third optional argument (may be null) is an array of previous transaction outputs that
        this transaction depends on but may not yet be in the block chain.

        :param hexstring: (required) The transaction hex string
        :type hexstring: str
        :param privatekey: (required) A json array of base58-encoded private keys for signing

            .. code-block:: text

                [
                    "privatekey",                (string) private key in base58-encoding
                    ...
                ]

        :type privatekey: array
        :param prevtxs: (optional) A json array of previous dependent transaction outputs

            .. code-block:: text

                [
                    {                              (json object)
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
        :param sighashtype: (optional) The signature hash type.

            Must be one of:

            "ALL"

            "NONE"

            "SINGLE"

            "ALL|ANYONECANPAY"

            "NONE|ANYONECANPAY"

            "SINGLE|ANYONECANPAY"

        :type sighashtype: str
        :return: {...} (json) -- returns json with signed transaction

            .. code-block:: text

                {
                    "hex" : "value",                      (string) The hex-encoded raw transaction with signature(s)
                    "complete" : true|false,              (boolean) If the transaction has a complete set of signatures
                    "errors" : [                          (json array of objects) Script verification errors (if there are any)
                        {
                            "txid" : "hash",              (string) The hash of the referenced, previous transaction
                            "vout" : n,                   (numeric) The index of the output to spent and used as input
                            "scriptSig" : "hex",          (string) The hex-encoded signature script
                            "sequence" : n,               (numeric) Script sequence number
                            "error" : "text"              (string) Verification or signing error related to the input
                        }
                        ,...
                    ]
                }

        :example:

            >>> node.rawtransactions.signrawtransactionwithkey("hex", ["key"])
        """
        return self._node._rpc.call("signrawtransactionwithkey", hexstring, privatekey, prevtxs, sighashtype)

    def testmempoolaccept(self, rawtxs: [], maxfeerate: float = 0.10) -> [{}]:  # 16
        """

        :param rawtxs: (required) An array of hex strings of raw transactions
        :type rawtxs: array
        :param maxfeerate: (optional) Reject transactions whose fee rate is higher than the specified value,
            expressed in DFI/kB
        :type maxfeerate: float
        :return: [{...}] (json array) -- The result of the mempool acceptance test for each raw transaction in the input array.

            .. code-block:: text

                [                           (array) The result of the mempool acceptance test for each raw transaction in the input array.
                                            Length is exactly one for now.
                    {
                        "txid"              (string) The transaction hash in hex
                        "allowed"           (boolean) If the mempool allows this tx to be inserted
                        "reject-reason"     (string) Rejection string (only present when 'allowed' is false)
                    }
                ]

        :example:

            >>> node.rawtransactions.testmempoolaccept(["signedhex"])
        """
        return self._node._rpc.call("testmempoolaccept", rawtxs, maxfeerate)

    def utxoupdatepsbt(self, psbt: str, descriptors: [{}] = None) -> str:  # 17
        """
        Updates all segwit inputs and outputs in a PSBT with data from output descriptors, the UTXO set or the mempool.

        :param psbt: (required) A base64 string of a PSBT
        :type psbt: str
        :param descriptors: (optional) An array of either strings or objects

            .. code-block:: text

                [
                    "",                         (string) An output descriptor
                    {                           (json object) An object with an output descriptor and extra information
                        "desc": "str",          (string, required) An output descriptor
                        "range": n or [n,n],    (numeric or array, optional, default=1000) Up to what index HD chains should be explored (either end or [begin,end])
                    },
                    ...
                ]

        :type descriptors: json array
        :return: "psbt" (string) -- The base64-encoded partially signed transaction with inputs updated

        :example:

            >>> node.rawtransactions.utxoupdatepsbt("psbt")
        """
        return self._node._rpc.call("utxoupdatepsbt", psbt, descriptors)
