from ..util import BuildJson


class Poolpair:
    def __init__(self, node):
        self._node = node

    def addpoolliquidity(self, _from: str, shareAddress: str, inputs: [{}] = None) -> str:  # 01
        """
        Creates (and submits to local node and network) a add pool liquidity transaction.

        The last optional argument (may be empty array) is an array of specific UTXOs to spend.

        Requires wallet passphrase to be set with walletpassphrase call.

        :param _from: (required) The defi address(es) is the key(s), the value(s) is amount in amount@token format. You
            should provide exectly two types of tokens for pool's 'token A' and 'token B' in any combinations.If
            multiple tokens from one address are to be transferred, specify an array ["amount1@t1", "amount2@t2"]

            If "from" obj contain only one amount entry with address-key: "*" (star), it's means auto-selection
            accounts from wallet.
        :type _from: str
        :param shareAddress: (required) The defi address for crediting tokens
        :type shareAddress: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.poolpair.addpoolliquidity({"df1qpsg2v3fajhwfrc3dchsqpcwqfegdxpncwpcda2": ["1.0@BTC", "1.0@DFI"]}, "df1qpsg2v3fajhwfrc3dchsqpcwqfegdxpncwpcda2")
        """
        return self._node._rpc.call("addpoolliquidity", _from, shareAddress, inputs)

    def compositeswap(self, _from: str, tokenFrom: str, amountFrom: float, to: str, tokenTo: str, maxPrice: float = None, inputs: [{}] = None) -> str:  # 02
        """
        Creates (and submits to local node and network) a composite swap (swap between multiple poolpairs) transaction with given metadata.

        :param _from: (required) Address of the owner of tokenA
        :type _from: str
        :param tokenFrom: (required) One of the keys may be specified (id/symbol)
        :type tokenFrom: str
        :param amountFrom: (required) tokenFrom coins amount
        :type amountFrom: float
        :param to: (required) Address of the owner of tokenB
        :type to: str
        :param tokenTo: (required) One of the keys may be specified (id/symbol)
        :type tokenTo: str
        :param maxPrice: (optional) Maximum acceptable price
        :type maxPrice: float
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.poolpair.compositeswap("df1qpsg2v3fajhwfrc3dchsqpcwqfegdxpncwpcda2", "BTC", 1, "df1qpsg2v3fajhwfrc3dchsqpcwqfegdxpncwpcda2", "DFI")
        """
        metadata = BuildJson()
        metadata.append("from", _from)
        metadata.append("tokenFrom", tokenFrom)
        metadata.append("amountFrom", amountFrom)
        metadata.append("to", to)
        metadata.append("tokenTo", tokenTo)
        metadata.append("maxPrice", maxPrice)
        return self._node._rpc.call("compositeswap", metadata.build(), inputs)

    def createpoolpair(self, tokenA: str, tokenB: str, commission: float, status: bool, ownerAddress: str,
                       customRewards: str = None, pairSymbol: str = None, inputs: [{}] = None) -> str:  # 03
        """
        Creates (and submits to local node and network) a poolpair transaction with given metadata.

        :param tokenA: (required) One of the keys may be specified (id/symbol)
        :type tokenA: str
        :param tokenB: (required) One of the keys may be specified (id/symbol)
        :type tokenB: str
        :param commission: (required) Pool commission, up to 10^-8
        :type commission: float
        :param status: (required) Pool Status: True is Active, False is Restricted
        :type status: bool
        :param ownerAddress: (required) Address of the pool owner
        :type ownerAddress: str
        :param customRewards: (optional) Token reward to be paid on each block, multiple can be specified
        :type customRewards: str
        :param pairSymbol: (optional) Pair symbol (unique), no longer than 8
        :type pairSymbol: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.poolpair.createpoolpair("BTC", "USDC", 0.5, True, "df1qpsg2v3fajhwfrc3dchsqpcwqfegdxpncwpcda2")
        """
        metadata = BuildJson()
        metadata.append("tokenA", tokenA)
        metadata.append("tokenB", tokenB)
        metadata.append("commission", commission)
        metadata.append("status", status)
        metadata.append("ownerAddress", ownerAddress)
        metadata.append("customRewards", customRewards)
        metadata.append("pairSymbol", pairSymbol)
        return self._node._rpc.call("createpoolpair", metadata.build(), inputs)

    def getpoolpair(self, key: str, verbose: bool = True) -> {}:  # 04
        """
        Returns information about pool.

        :param key: (required) One of the keys may be specified (id/symbol/creationTx)
        :type key: str
        :param verbose: (optional) Flag for verbose list (default = true), otherwise limited objects are listed
        :type verbose: bool
        :return: {id:{...}} (json) -- Json object with pool information

        :example:

            >>> node.poolpair.getpoolpair(4)
        """
        return self._node._rpc.call("getpoolpair", key, verbose)

    def listpoolpairs(self, start: int = None, including_start: bool = None, limit: int = 100, verbose: bool = True) -> {}:  # 05
        """
        Returns information about pools

        :param start: (optional) Optional first key to iterate from, in lexicographical order.
            Typically it's set to last ID from previous request
        :type start: int
        :param including_start: (optional) If true, then iterate including starting position
        :type including_start: bool
        :param limit: (optional) Maximum number of pools to return, 100 by default
        :type limit: int
        :param verbose: (optional) Flag for verbose list (default = true), otherwise only ids, symbols and names are listed
        :type verbose: bool
        :return: {id:{...}} (json) -- Json object with pool information

        :example:

            >>> node.poolpair.listpoolpairs()
        """
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listpoolpairs", pagination.build(), verbose)

    def listpoolshares(self, start: int = None, including_start: bool = None, limit: int = 100, verbose: bool = True, is_mine_only: bool = False) -> {}:  # 06
        """
        Returns information about pool shares

        :param start: (optional) Optional first key to iterate from, in lexicographical order
        :type start: int
        :param including_start: (optional) If true, then iterate including starting position
        :type including_start: bool
        :param limit: (optional) Maximum number of pools to return
        :type limit: int
        :param verbose: (optional) Flag for verbose list (default = true), otherwise only % are shown
        :type verbose: bool
        :param is_mine_only: (optional) Flag for verbose list (default = true), otherwise only % are shown
        :type is_mine_only: bool
        :return: {id:{...}} (json) -- Json object with pool information

        :example:

            >>> node.poolpair.listpoolshares()
        """
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listpoolshares", pagination.build(), verbose, is_mine_only)

    def poolswap(self, _from: str, tokenFrom: str, amountFrom: float, to: str, tokenTo: str, maxPrice: float = None, inputs: [{}] = None) -> str:  # 07
        """
        Creates (and submits to local node and network) a poolswap transaction with given metadata

        :param _from: (required) Address of the owner of tokenA
        :type _from: str
        :param tokenFrom: (required) One of the keys may be specified (id/symbol)
        :type tokenFrom: str
        :param amountFrom: (required) tokenFrom coins amount
        :type amountFrom: float
        :param to: (required) Address of the owner of tokenB
        :type to: str
        :param tokenTo: (required) One of the keys may be specified (id/symbol)
        :type tokenTo: str
        :param maxPrice: (optional) Maximum acceptable price
        :type maxPrice: float
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.poolpair.poolswap("df1qpsg2v3fajhwfrc3dchsqpcwqfegdxpncwpcda2", "BTC", 1, "df1qpsg2v3fajhwfrc3dchsqpcwqfegdxpncwpcda2", "DFI")
        """
        metadata = BuildJson()
        metadata.append("from", _from)
        metadata.append("tokenFrom", tokenFrom)
        metadata.append("amountFrom", amountFrom)
        metadata.append("to", to)
        metadata.append("tokenTo", tokenTo)
        metadata.append("maxPrice", maxPrice)
        return self._node._rpc.call("poolswap", metadata.build(), inputs)

    def removepoolliquidity(self, _from: str, amount: str, inputs: [{}] = None) -> str:  # 08
        """
        Creates (and submits to local node and network) a remove pool liquidity transaction

        :param _from: (required) The defi address which has tokens
        :type _from: str
        :param amount: (required) :ref:`Node Amount`
        :type amount: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.poolpair.removepoolliquidity("df1qpsg2v3fajhwfrc3dchsqpcwqfegdxpncwpcda2", "1.0@BTC-DFI")
        """
        return self._node._rpc.call("removepoolliquidity", _from, amount, inputs)

    def testpoolswap(self, _from: str, tokenFrom: str, amountFrom: float, to: str, tokenTo: str, maxPrice: float = None, path: str = "direct", verbose: bool = False) -> str:  # 09
        """
        Tests a poolswap transaction with given metadata and returns poolswap result

        :param _from: (required) Address of the owner of tokenA
        :type _from: str
        :param tokenFrom: (required) One of the keys may be specified (id/symbol)
        :type tokenFrom: str
        :param amountFrom: (required) tokenFrom coins amount
        :type amountFrom: float
        :param to: (required) Address of the owner of tokenB
        :type to: str
        :param tokenTo: (required) One of the keys may be specified (id/symbol)
        :type tokenTo: str
        :param maxPrice: (optional) Maximum acceptable price
        :type maxPrice: float
        :param path: (optional) One of auto/direct

            .. code-block:: text

                auto - automatically use composite swap or direct swap as needed
                direct - uses direct path only or fails
                composite - uses composite path only or fails

        :type path: str
        :param verbose: (optional) Returns estimated composite path when true
        :type verbose: bool
        :return: "amount@tokenId" (string) -- The string with amount result of poolswap in format AMOUNT@TOKENID

        :example:

            >>> node.poolpair.testpoolswap("df1qpsg2v3fajhwfrc3dchsqpcwqfegdxpncwpcda2", "BTC", 1, "df1qpsg2v3fajhwfrc3dchsqpcwqfegdxpncwpcda2", "DFI")
        """
        metadata = BuildJson()
        metadata.append("from", _from)
        metadata.append("tokenFrom", tokenFrom)
        metadata.append("amountFrom", amountFrom)
        metadata.append("to", to)
        metadata.append("tokenTo", tokenTo)
        metadata.append("maxPrice", maxPrice)
        return self._node._rpc.call("testpoolswap", metadata.build(), path, verbose)

    def updatepoolpair(self, pool: str, status: bool = None, commission: float = None, ownerAddress: str = None, customRewards: str = None, inputs: [{}] = None) -> str:  # 10
        """
        Creates (and submits to local node and network) a pool status update transaction

        :param pool: (required) The pool's symbol, id or creation tx
        :type pool: str
        :param status: (optional) Pool Status new property
        :type status: bool
        :param commission: (optional) Pool commission, up to 10^-8
        :type commission: float
        :param ownerAddress: (optional) Address of the pool owner
        :type ownerAddress: str
        :param customRewards: (optional) Token reward to be paid on each block, multiple can be specified
        :type customRewards: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.poolpair.updatepoolpair("BTC-DFI", True, "0.5")
        """
        metadata = BuildJson()
        metadata.append("pool", pool)
        metadata.append("status", status)
        metadata.append("commission", commission)
        metadata.append("ownerAddress", ownerAddress)
        metadata.append("customRewards", customRewards)
        return self._node._rpc.call("updatepoolpair", metadata.build(), inputs)
