from ..util import BuildJson


class Vault:
    def __init__(self, node):
        self._node = node

    def closevault(self, vaultId: str, to: str, inputs: [{}] = None) -> str:  # 01
        """
        Close vault transaction.

        :param vaultId: (required) Vault to be closed
        :type vaultId: str
        :param to: (required) Any valid address to receive collaterals and half fee back
        :type to: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.vault.closevault("84b22eee1964768304e624c416f29a91d78a01dc5e8e12db26bdac0670c67bb2", "mwSDMvn1Hoc8DsoB7AkLv7nxdrf5Ja4jsF")
        """
        return self._node._rpc.call("closevault", vaultId, to, inputs)

    def createvault(self, ownerAddress: str, loanSchemeId: str = "", inputs: [{}] = None) -> str:  # 02
        """
        Creates a vault transaction.

        :param ownerAddress: (required) Any valid address
        :type ownerAddress: str
        :param loanSchemeId: (optional) Unique identifier of the loan scheme (8 chars max).
            If empty, the default loan scheme will be selected
        :type loanSchemeId: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.vault.createvault("2MzfSNCkjgCbNLen14CYrVtwGomfDA5AGYv")
        """
        return self._node._rpc.call("createvault", ownerAddress, loanSchemeId, inputs)

    def deposittovault(self, vaultId: str, _from: str, amount: str, inputs: [{}] = None) -> str:  # 03
        """
        Deposit collateral token amount to vault.

        :param vaultId: (required) Vault id
        :type vaultId: str
        :param _from: (required) Address containing collateral
        :type _from: str
        :param amount: (required) Amount of collateral in amount@symbol format
        :type amount: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.vault.deposittovault("84b22eee1964768304e624c416f29a91d78a01dc5e8e12db26bdac0670c67bb2i", "mwSDMvn1Hoc8DsoB7AkLv7nxdrf5Ja4jsF", "1@DFI")
        """
        return self._node._rpc.call("deposittovault", vaultId, _from, amount, inputs)

    def estimatecollateral(self, loanAmounts: str, targetRatio: float, tokens: {} = None) -> str:  # 04
        """
        Returns amount of collateral tokens needed to take an amount of loan tokens for a target collateral ratio.

        :param loanAmounts: (required) Amount as json string, or array. Example: '[ "amount@token" ]'
        :type loanAmounts: str
        :param targetRatio: (required) Target collateral ratio
        :type targetRatio: float
        :param tokens: (optional) Object with collateral token as key and their percent split as value
        :type tokens: json

            .. code-block:: text

                {
                    "split": n,    (numeric, required) The percent split
                }

        :return: {...} (json) -- array of <amount@token> strings

        :example:

            >>> node.vault.estimatecollateral("1@DUSD", 200)
        """
        return self._node._rpc.call("estimatecollateral", loanAmounts, targetRatio, tokens)

    def estimateloan(self, vaultId: str, tokens: {}, targetRatio: int = None) -> {}:  # 05
        """
        Returns amount of loan tokens a vault can take depending on a target collateral ratio.

        :param vaultId: (required) vault hex id
        :type vaultId: str
        :param tokens: (required) Object with loans token as key and their percent split as value
        :type tokens: json
        :param targetRatio: (required) Target collateral ratio
        :type targetRatio: float
        :return: {...} (json) -- array of <amount@token> strings

        :example:

            >>> node.vault.estimateloan("5474b2e9bfa96446e5ef3c9594634e1aa22d3a0722cb79084d61253acbdf87bf", {"DUSD": 1}, 200)
        """
        return self._node._rpc.call("estimateloan", vaultId, tokens, targetRatio)

    def estimatevault(self, collateralAmounts: str, loanAmounts: str) -> {}:  # 06
        """
        Returns estimated vault for given collateral and loan amounts.

        :param collateralAmounts: (required) Collateral amounts as json string, or array. Example: '[ "amount@token" ]'
        :type collateralAmounts: str
        :param loanAmounts: (required) Loan amounts as json string, or array. Example: '[ "amount@token" ]'
        :type loanAmounts: str
        :return: {...} (json) -- returns estimate vault for given collateral and loan amounts

            .. code-block:: text

                {
                    "collateralValue" : n.nnnnnnnn,        (amount) The total collateral value in USD
                    "loanValue" : n.nnnnnnnn,              (amount) The total loan value in USD
                    "informativeRatio" : n.nnnnnnnn,       (amount) Informative ratio with 8 digit precision
                    "collateralRatio" : n,                 (uint) Ratio as unsigned int
                }

        :example:

            >>> node.vault.estimatevault(["1000.00000000@DFI"], ["10@DUSD"])
        """
        return self._node._rpc.call("estimatevault", collateralAmounts, loanAmounts)

    def getvault(self, vaultId: str, verbose: bool = False) -> {}:  # 07
        """
        Returns information about vault.

        :param vaultId: (required) vault hex id
        :type vaultId: str
        :param verbose: (optional) Verbose vault information
        :type verbose: bool
        :return: {...} (json) -- vault data in json form

        :example:

            >>> node.vault.getvault("5474b2e9bfa96446e5ef3c9594634e1aa22d3a0722cb79084d61253acbdf87bf")
        """
        return self._node._rpc.call("getvault", vaultId, verbose)

    def listauctionhistory(self, identifier: str = "mine", maxBlockHeight: int = None, vaultId: str = None,
                           index: int = None, limit: int = None) -> [{}]:  # 08
        """
        Returns information about auction history.

        :param identifier: (optional) Single account ID (CScript or address) or vaultId or reserved words:
            "mine" - to list history for all owned accounts or "all" to list whole DB (default = "mine").
        :type identifier: str
        :param maxBlockHeight: (optional) Optional height to iterate from (downto genesis block)
        :type maxBlockHeight: int
        :param vaultId: (optional) Vault id
        :type vaultId: str
        :param index: (optional)  Batch index
        :type index: int
        :param limit: (optional) Maximum number of orders to return
        :type limit: int
        :return: [{},{}...] (json array) -- Objects with auction history information

        :example:

            >>> node.vault.listauctionhistory("all")
        """
        pagination = BuildJson()
        pagination.append("maxBlockHeight", maxBlockHeight)
        pagination.append("vaultId", vaultId)
        pagination.append("index", index)
        pagination.append("limit", limit)
        return self._node._rpc.call("listauctionhistory", identifier, pagination.build())

    def listauctions(self, vaultId: str = None, height: int = None, including_start: bool = None, limit: int = 100) -> [{}]:  # 09
        """
        List all available auctions.

        :param vaultId: (optional) Vault id
        :type vaultId: str
        :param height: (optional) Height to iterate from
        :type height: int
        :param including_start: (optional) If true, then iterate including starting position
        :type including_start: bool
        :param limit: (optional)  Maximum number of orders to return
        :type limit: int
        :return: [{...}] (json array) Json object with auction information

        :example:

            >>> node.vault.listauctions()
        """
        start = BuildJson()
        start.append("vaultId", vaultId)
        start.append("height", height)
        start = None if start.build() is {} else start.build()
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listauctions", pagination.build())

    def listvaulthistory(self, vaultId: str, maxBlockHeight: int = None, depth: int = None, token: str = None,
                         txtype: str = None, limit: int = 100) -> [{}]:  # 10
        """
        Returns the history of the specified vault

        :param vaultId: (required) Vault to get history for
        :type vaultId: str
        :param maxBlockHeight: (optional) Optional height to iterate from (down to genesis block)
        :type maxBlockHeight: int
        :param depth: (optional) Maximum depth, from the genesis block is the default
        :type depth: int
        :param token: (optional) Filter by token
        :type token: str
        :param txtype: (optional) Filter by transaction type, supported letter from {CustomTxType}
        :type txtype: str
        :param limit: (optional) Maximum number of records to return, 100 by default
        :type limit: int
        :return: [{...}] -- (json array) Objects with vault history information

        :example:

            >>> node.vault.listvaulthistory("84b22eee1964768304e624c416f29a91d78a01dc5e8e12db26bdac0670c67bb2")
        """
        options = BuildJson()
        options.append("maxBlockHeight", maxBlockHeight)
        options.append("depth", depth)
        options.append("token", token)
        options.append("txtype", txtype)
        options.append("limit", limit)
        return self._node._rpc.call("listvaulthistory", vaultId, options.build())

    def listvaults(self, ownerAddress: str = None, loanSchemeId: str = None, state: str = 'unknown',
                   verbose: bool = False, start: str = None, including_start: bool = None, limit: int = 100) -> [{}]:  # 11
        """
        List all available vaults.

        :param ownerAddress: (optional) Address of the vault owner
        :type ownerAddress: str
        :param loanSchemeId: (optional) Vault's loan scheme id
        :type loanSchemeId: str
        :param state: (optional) Wether the vault is under a given state.
        :type state: str
        :param verbose: (optional) Flag for verbose list (default = false), otherwise only ids, ownerAddress,
            loanSchemeIds and state are listed
        :type verbose: bool
        :param start: (optional) Optional first key to iterate from, in lexicographical order. Typically it's set to
            last ID from previous request.
        :type start: str
        :param including_start: (optional) If true, then iterate including starting position.
        :type including_start: bool
        :param limit: (optional) Maximum number of orders to return
        :type limit: int
        :return: [{...}] (json array) -- Json object with vault information

        :example:

            >>> node.vault.listvaults()
        """
        options = BuildJson()
        options.append("ownerAddress", ownerAddress)
        options.append("loanSchemeId", loanSchemeId)
        options.append("state", state)
        options.append("verbose", verbose)

        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listvaults", options.build(), pagination.build())

    def paybackwithcollateral(self, vaultId: str) -> str:  # 12
        """
        Payback vault's loans with vault's collaterals.

        :param vaultId: (required) vault hex id
        :type vaultId: str
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.vault.paybackwithcollateral("5474b2e9bfa96446e5ef3c9594634e1aa22d3a0722cb79084d61253acbdf87bf")
        """
        return self._node._rpc.call("paybackwithcollateral", vaultId)

    def placeauctionbid(self, vaultId: str, index: int, _from: str, amount: str, inputs: [{}] = None) -> str:  # 13
        """
        Bid to vault in auction.

        :param vaultId: (required) Vault id
        :type vaultId: str
        :param index: (required) Auction index
        :type index: int
        :param _from: (required) Address to get tokens. If "from" value is: "*" (star), it's means auto-selection
            accounts from wallet
        :type _from: str
        :param amount: (required) Amount of amount@symbol format
        :type amount: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.vault.placeauctionbid("84b22eee1964768304e624c416f29a91d78a01dc5e8e12db26bdac0670c67bb2", 0, "mwSDMvn1Hoc8DsoB7AkLv7nxdrf5Ja4jsF", "100@TSLA")
        """
        return self._node._rpc.call("placeauctionbid", vaultId, index, _from, amount, inputs)

    def updatevault(self, vaultId: str, ownerAddress: str = None, loanSchemeId: str = None, inputs: [{}] = None) -> str:  # 14
        """
        Creates (and submits to local node and network) an `update vault transaction`,
        and saves vault updates to database.

        The last optional argument (may be empty array) is an array of specific UTXOs to spend.

        :param vaultId: (required) Vault id
        :type vaultId: str
        :param ownerAddress: (optional) Vault's owner address
        :type ownerAddress: str
        :param loanSchemeId: (optional) Vault's loan scheme id
        :type loanSchemeId: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.vault.updatevault("84b22eee1964768304e624c416f29a91d78a01dc5e8e12db26bdac0670c67bb2", {"ownerAddress": "mwSDMvn1Hoc8DsoB7AkLv7nxdrf5Ja4jsF"})
        """
        parameters = BuildJson()
        parameters.append("ownerAddress", ownerAddress)
        parameters.append("loanSchemeId", loanSchemeId)
        return self._node._rpc.call("updatevault", vaultId, parameters.build(), inputs)

    def withdrawfromvault(self, vaultId: str, to: str, amount: str, inputs: [{}] = None) -> str:  # 15
        """
        Withdraw collateral token amount from vault.

        :param vaultId: (required) Vault id
        :type vaultId: str
        :param to: (required) Destination address for withdraw of collateral
        :type to: str
        :param amount: (required) Amount of collateral in amount@symbol format
        :type amount: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.vault.withdrawfromvault("84b22eee1964768304e624c416f29a91d78a01dc5e8e12db26bdac0670c67bb2i", "mwSDMvn1Hoc8DsoB7AkLv7nxdrf5Ja4jsF", "1@DFI")
        """
        return self._node._rpc.call("withdrawfromvault", vaultId, to, amount, inputs)
