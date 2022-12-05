from ..util import BuildJson


class Tokens:
    def __init__(self, node):
        self._node = node

    def burntokens(self, amounts: str, _from: str, context: str = None, inputs: [{}] = None) -> str:  # 01
        """
        Creates (and submits to local node and network) a transaction burning your token (for accounts and/or UTXOs).

        The second optional argument (may be empty array) is an array of specific UTXOs to spend. One of UTXO's must
        belong to the token's owner (collateral) address

        Requires wallet passphrase to be set with walletpassphrase call.

        :param amounts: (required) :ref:`Node Amount`
        :type amounts: str
        :param _from: (required) Address containing tokens to be burned
        :type _from: str
        :param context: (optional) Additional data necessary for specific burn type
        :type context: str
        :param inputs: :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.tokens.burntokens("10@BTC", "df1qpsg2v3fajhwfrc3dchsqpcwqfegdxpncwpcda2")
        """
        metadata = BuildJson()
        metadata.append("amounts", amounts)
        metadata.append("from", _from)
        metadata.append("context", context)
        return self._node._rpc.call("burntokens", metadata.build(), inputs)

    def createtoken(self, symbol: str, collateralAddress: str, name: str = None, isDAT: bool = None,
                    decimal: float = None, limit: int = None, mintable: bool = True, tradeable: bool = True,
                    inputs: [{}] = None) -> str:  # 02
        """
        Creates (and submits to local node and network) a token creation transaction with given metadata.
        The second optional argument (may be empty array) is an array of specific UTXOs to spend.

        :param symbol: (required) Token's symbol (unique), no longer than 8
        :type symbol: str
        :param collateralAddress: (required) Any valid destination for keeping collateral amount - used as token's owner auth
        :type collateralAddress: str
        :param name: (optional) Token's name, no longer than 128
        :type name: str
        :param isDAT: (optional) Token's 'isDAT' property, default is 'False'
        :type isDAT: bool
        :param decimal: (optional) Token's decimal places
        :type decimal: float
        :param limit: (optional) Token's total supply limit
        :type limit: int
        :param mintable: (optional) Token's 'Mintable' property
        :type mintable: bool
        :param tradeable: (optional) Token's 'Tradeable' property
        :type tradeable: bool
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.tokens.createtoken("MyToken", "df1qpsg2v3fajhwfrc3dchsqpcwqfegdxpncwpcda2")
        """
        metadata = BuildJson()
        metadata.append("symbol", symbol)
        metadata.append("collateralAddress", collateralAddress)
        metadata.append("name", name)
        metadata.append("isDAT", isDAT)
        metadata.append("decimal", decimal)
        metadata.append("limit", limit)
        metadata.append("mintable", mintable)
        metadata.append("tradeable", tradeable)
        return self._node._rpc.call("createtoken", metadata.build(), inputs)

    def decodecustomtx(self, hexstring: str, iswitness: bool = None) -> str:  # 03
        """
        Get detailed information about a DeFiChain custom transaction.

        :param hexstring: (required) The transaction hex string
        :type hexstring: str
        :param iswitness: (optional) Whether the transaction hex is a serialized witness transaction.

            If iswitness is not present, heuristic tests will be used in decoding.

            If true, only witness deserialization will be tried.

            If false, only non-witness deserialization will be tried.

            This boolean should reflect whether the transaction has inputs
            (e.g. fully valid, or on-chain transactions), if known by the caller.
        :type iswitness: bool
        :return: {...} (json) -- returns decoded custom transaction

            .. code-block:: text

                {
                    "txid":               (string) The transaction id.
                    "type":               (string) The transaction type.
                    "valid"               (bool) Whether the transaction was valid.
                    "results"             (json object) Set of results related to the transaction type
                }

        :example:

            >>> node.tokens.decodecustomtx("hexstring")
        """
        return self._node._rpc.call("decodecustomtx", hexstring, iswitness)

    def getcustomtx(self, txid: str, blockhash: str = None) -> {}:  # 04
        """
        Get detailed information about a DeFiChain custom transaction. Will search wallet transactions and mempool transaction,
        if a blockhash is provided and that block is available then details for that transaction can be returned.

        -txindex can be enabled to return details for any transaction.

        :param txid: (required) The transaction id
        :type txid: str
        :param blockhash: (optional) The block in which to look for the transaction
        :type blockhash: str
        :return: {...} (json) -- returns a custom transaction in json format

            .. code-block:: text

                {
                    "type":               (string) The transaction type.
                    "valid"               (bool) Whether the transaction was valid.
                    "results"             (json object) Set of results related to the transaction type
                    "block height"        (string) The block height containing the transaction.
                    "blockhash"           (string) The block hash containing the transaction.
                    "confirmations": n,   (numeric) The number of confirmations for the transaction.
                }

         :example:

            >>> node.tokens.getcustomtx("66ea2ac081e2917f075e2cca7c1c0baa12fb85c469f34561185fa64d7d2f9305")
        """
        return self._node._rpc.call("getcustomtx", txid, blockhash)

    def gettoken(self, key: str):  # 05
        """
        Returns information about token.

        :param key: (required) One of the keys may be specified (id/symbol/creationTx)
        :type key: str
        :return: {...} (json) -- json object with token information

        :example:

            >>> node.tokens.gettoken("DFI")
        """
        return self._node._rpc.call("gettoken", key)

    def listtokens(self, start: int = None, including_start: bool = None, limit: int = 100, verbose: bool = True) -> {}:  # 06
        """
        Returns information about tokens

        :param start:
        :type start: int
        :param including_start:
        :type including_start: bool
        :param limit:
        :type limit: int
        :param verbose:
        :type verbose: bool
        :return: [{...}] (json array) -- json object with token information

        :example:

            >>> node.tokens.listtokens()
        """
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listtokens", pagination.build(), verbose)

    def minttokens(self, amounts: str, inputs: [{}] = None) -> str:  # 07
        """
        Creates (and submits to local node and network) a transaction minting your token (for accounts and/or UTXOs).

        The second optional argument (may be empty array) is an array of specific UTXOs to spend. One of UTXO's
        must belong to the token's owner (collateral) address

        :param amounts: (required) Amount as json string, or array. Example: '[ "amount@token" ]'
        :type amounts: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.tokens.minttokens("10@MyToken")
        """
        return self._node._rpc.call("minttokens", amounts, inputs)

    def updatetoken(self, token: str, symbol: str = None, name: str = None, isDAT: bool = False, mintable: bool = None,
                    tradeable: bool = None, finalize: bool = None, inputs: [{}] = None) -> str:  # 08
        """
        Creates (and submits to local node and network) a transaction of token promotion to isDAT or demotion from
        isDAT. Collateral will be unlocked.

        The second optional argument (may be empty array) is an array of specific UTXOs to spend. One of UTXO's must
        belong to the token's owner (collateral) address

        :param token: (required) The tokens's symbol, id or creation tx
        :type token: str
        :param symbol: (optional) New token's symbol, no longer than 8
        :type symbol: str
        :param name: (optional)  New token's name, no longer than 128
        :type name: str
        :param isDAT: (optional) Token's 'isDAT' property, default is 'False'
        :type isDAT: bool
        :param mintable: (optional) Token's 'Mintable' property
        :type mintable: bool
        :param tradeable: (optional) Token's 'Tradeable' property
        :type tradeable: bool
        :param finalize: (optional) Lock token properties forever
        :type finalize: bool
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.tokens.updatetoken("MyToken", isDAT=True)
        """
        metadata = BuildJson()
        metadata.append("symbol", symbol)
        metadata.append("name", name)
        metadata.append("isDAT", isDAT)
        metadata.append("mintable", mintable)
        metadata.append("tradeable", tradeable)
        metadata.append("finalize", finalize)
        return self._node._rpc.call("updatetoken", token, metadata.build(), inputs)
