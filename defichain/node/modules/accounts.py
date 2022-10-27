from ..util import BuildJson


class Accounts:
    def __init__(self, node):
        self._node = node

    def accounthistorycount(self, owner: str = "mine", no_rewards: bool = None, token: str = None,
                            txtype: str = None) -> int:  # 01
        """
        Returns count of account history.

        :param owner: (optional) Single account ID (CScript or address) or reserved words: "mine" - to list history for all owned accounts or "all" to list whole DB (default = "mine").
        :type owner: str
        :param no_rewards: (optional) Filter out rewards
        :type no_rewards: bool
        :param token: (optional) Filter by token
        :type token: str
        :param txtype: (optional) Filter by transaction type, supported letter from {CustomTxType}
        :type txtype: str
        :return: int -- Count of account history

        :example:

            >>> node.accounts.accounthistorycount("all", True)
        """
        j = BuildJson()
        j.append("no_rewards", no_rewards)
        j.append("token", token)
        j.append("txtype", txtype)
        return self._node._rpc.call("accounthistorycount", owner, j.build())

    def accounttoaccount(self, _from: str, to: {}, inputs: [{}] = None) -> str:  # 02
        """
        Creates (and submits to local node and network) a transfer transaction from the specified account to the specfied accounts.
        The first optional argument (may be empty array) is an array of specific UTXOs to spend.

        :param _from: (required) The defi address of sender
        :type _from: str
        :param to: (required) :ref:`Node Address Amount`
        :type to: json object
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.accounts.accounttoaccount(sender_address, {"address1":"1.0@DFI","address2":["2.0@BTC", "3.0@ETH"]}, [])
        """
        return self._node._rpc.call("accounttoaccount", _from, to, inputs)

    def accounttoutxos(self, _from: str, to: {}, inputs: [{}] = None) -> str:  # 03
        """
        Creates (and submits to local node and network) a transfer transaction from the specified account to UTXOs.
        The third optional argument (may be empty array) is an array of specific UTXOs to spend.

        :param _from: (required) The defi address of sender
        :type _from: str
        :param to: (required) :ref:`Node Address Amount`
        :type to: json object
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.accounts.accounttoutxos(sender_address, {"address1":"100@DFI"}, [])
        """
        return self._node._rpc.call("accounttoutxos", _from, to, inputs)

    def executesmartcontract(self, name: str, amount: str, address: str = "", inputs: [{}] = None) -> str:  # 04
        """
        Creates and sends a transaction to either fund or execute a smart contract. Available contracts: dbtcdfiswap

        :param name: (required) Name of the smart contract to send funds to
        :type name: str
        :param amount: (required) :ref:`Node Amount`
        :type amount: str
        :param address: (optional) Address to be used in contract execution if required
        :type address: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.accounts.executesmartcontract("dbtcdfiswap", "1000@DFI")
        """
        return self._node._rpc.call("executesmartcontract", name, amount, address, inputs)

    def futureswap(self, address: str, amount: str, destination: str = "", inputs: [{}] = None) -> str:  # 05
        """
        Creates and submits to the network a futures contract

        :param address: (required) Address to fund contract and receive resulting token
        :type address:  str
        :param amount: (required) :ref:`Node Amount`
        :type amount: str
        :param destination: (optional) Expected dToken if DUSD supplied
        :type destination: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.accounts.futureswap(address, "1@TSLA")
            >>> node.accounts.futureswap(address, "1000@DUSD", "TSLA")
        """
        return self._node._rpc.call("futureswap", address, amount, destination, inputs)

    def getaccount(self, owner: str, start: str = None, including_start: bool = None, limit: int = None,
                   indexed_amounts: bool = False) -> "[{...}]":  # 06
        """
        Returns information about account.

        :param owner: (required) Owner address in base58/bech32/hex encoding
        :type owner: str
        :param start: (optional) Optional first key to iterate from, in lexicographical order.Typically it's set to last tokenID from previous request.
        :type start: str
        :param including_start: (optional) If true, then iterate including starting position. False by default
        :type including_start: bool
        :param limit: (optional) Maximum number of orders to return, 100 by default
        :type limit: int
        :param indexed_amounts: (optional) Format of amounts output (default = false): (true: obj = {tokenid:amount,...}, false: array = ["amount@tokenid"...])
        :type indexed_amounts: bool
        :return: [{...}] (json array) -- object with order information

        :example:

            >>> node.accounts.getaccount("mxxA2sQMETJFbXcNbNbUzEsBCTn1JSHXST")
        """
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)

        return self._node._rpc.call("getaccount", owner, pagination.build(), indexed_amounts)

    def getaccounthistory(self, owner: str, blockheight: int, txn: int) -> {}:  # 07
        """
        Returns information about account history.

        :param owner: (required) Single account ID (CScript or address).
        :type owner: str
        :param blockheight: (required) Block Height to search in.
        :type blockheight: int
        :param txn: (required) for order in block.
        :type txn: int
        :return: {...} (json) -- An object with account history information

        :example:

            >>> node.accounts.getaccounthistory("mxxA2sQMETJFbXcNbNbUzEsBCTn1JSHXST", 103, 2)
        """
        return self._node._rpc.call("getaccounthistory", owner, blockheight, txn)

    def getburninfo(self) -> {}:  # 08
        """
        Returns burn address and burnt coin and token information.
        Requires full acindex for correct amount, tokens and feeburn values.

        :return: {...} (json) -- information about burned coins

            .. code-block:: text

                {
                    "address" : "address", (string) The defi burn address
                    "amount" : n.nnnnnnnn, (string) The amount of DFI burnt
                    "tokens" :  [
                        {
                            (array of burnt tokens) "name" : "name"
                            "amount" : n.nnnnnnnn
                        }
                    ]
                    "feeburn" : n.nnnnnnnn, (string) The amount of fees burnt
                    "emissionburn" : n.nnnnnnnn, (string) The amount of non-utxo coinbase rewards burnt
                }

        :example:

            >>> node.accounts.getaccount()
        """
        return self._node._rpc.call("getburninfo")

    def getpendingdusdswaps(self, address: str) -> {}:  # 09
        """
        Get specific pending DFI-to-DUSD swap.

        :param address: (required) Address to get all pending future swaps
        :type address: str
        :return: {...} (json) -- returns pending DUSD - DFI Swaps

            .. code-block:: text

                {
                    owner :       "address"
                    amount :      n.nnnnnnnn
                }

        :example:

            >>> node.accounts.getpendingdusdswaps(address)
        """
        return self._node._rpc.call("getpendingdusdswaps", address)

    def getpendingfutureswaps(self, address: str) -> {}:  # 10
        """
        Get specific pending futures.

        :param address: (required) Address to get all pending future swaps
        :type address: str
        :return: {...} (json) -- returns pending future swaps

            .. code-block:: text

                {
                    owner :       "address"
                    values : [{
                        tokenSymbol : "SYMBOL"
                        amount :      n.nnnnnnnn
                        destination : "SYMBOL"
                    }...]
                }

        :example:

            >>> node.accounts.getpendingfutureswaps(address)
        """
        return self._node._rpc.call("getpendingfutureswaps", address)

    def gettokenbalances(self, start: str = None, including_start: bool = None, limit: int = None,
                         indexed_amounts: bool = False, symbol_lookup: bool = False) -> []:  # 11
        """
        Returns the balances of all accounts that belong to the wallet.

        :param start: (optional) Optional first key to iterate from, in lexicographical order.Typically it's set to last tokenID from previous request.
        :type start: str
        :param including_start: (optional) If true, then iterate including starting position. False by default
        :type including_start: bool
        :param limit: (optional) Maximum number of tokens to return, 100 by default
        :type limit: int
        :param indexed_amounts: (optional) Format of amounts output (default = false): (true: obj = {tokenid:amount,...}, false: array = ["amount@tokenid"...])
        :type indexed_amounts: bool
        :param symbol_lookup: (optional) Use token symbols in output (default = false)
        :type symbol_lookup: bool
        :return: [...] (json array) -- object with balances information

        :example:

            >>> node.accounts.gettokenbalances()
        """
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)

        return self._node._rpc.call("gettokenbalances", pagination.build(), indexed_amounts, symbol_lookup)

    def listaccounthistory(self, owner: str, maxBlockHeight: int = None, depth: int = None, no_rewards: bool = None,
                           token: str = None, txtype: str = None, limit: int = None, txn: int = None,
                           format: str = None) -> [{}]:  # 12
        """
        Returns information about account history.

        :param owner: (required) Single account ID (CScript or address) or reserved words: "mine" - to list history for all owned accounts or "all" to list whole DB (default = "mine").
        :type owner: str
        :param maxBlockHeight: (optional) Optional height to iterate from (downto genesis block), (default = chaintip).
        :type maxBlockHeight: int
        :param depth: (optional) Maximum depth, from the genesis block is the default
        :type depth: int
        :param no_rewards: (optional) Filter out rewards
        :type no_rewards: bool
        :param token: (optional) Filter by token
        :type token: str
        :param txtype: (optional) Filter by transaction type, supported letter from {CustomTxType}
        :type txtype: str
        :param limit: (optional) Maximum number of records to return, 100 by default
        :type limit: int
        :param txn: (optional) Order in block, unlimited by default
        :type txn: int
        :param format: (optional) Return amounts with the following: 'id' -> <amount>@id; (default)'symbol' -> <amount>@symbol
        :type format: str
        :return: [{},{}, ...] (json array) -- Objects with account history information

        :example:

            >>> node.accounts.listaccounthistory("all", 160, 10)
        """
        options = BuildJson()
        options.append("maxBlockHeight", maxBlockHeight)
        options.append("depth", depth)
        options.append("no_rewards", no_rewards)
        options.append("token", token)
        options.append("txtype", txtype)
        options.append("limit", limit)
        options.append("txn", txn)
        options.append("format", format)

        return self._node._rpc.call("listaccounthistory", owner, options.build())

    def listaccounts(self, start: str = None, including_start: bool = None, limit: int = None, verbose: bool = True,
                     indexed_amounts: bool = False, is_mine_only: bool = False) -> {}:  # 13
        """
        Returns information about all accounts on chain.

        :param start: (optional) Optional first key to iterate from, in lexicographical order.Typically it's set to last ID from previous request.
        :type start: str
        :param including_start: (optional) If true, then iterate including starting position. False by default
        :type including_start: bool
        :param limit: (optional) Maximum number of orders to return, 100 by default
        :type limit: int
        :param verbose: (optional) Flag for verbose list (default = true), otherwise limited objects are listed
        :type verbose: bool
        :param indexed_amounts: (optional) Format of amounts output (default = false): (true: {tokenid:amount}, false: "amount@tokenid")
        :type indexed_amounts: bool
        :param is_mine_only: (optional) Get balances about all accounts belonging to the wallet
        :type is_mine_only: bool
        :return: {id:{...},...} (json) -- Json object with accounts information

        :example:

            >>> node.accounts.listaccounts()
        """
        pagnation = BuildJson()
        pagnation.append("start", start)
        pagnation.append("including_start", including_start)
        pagnation.append("limit", limit)

        return self._node._rpc.call("listaccounts", pagnation.build(), verbose, indexed_amounts, is_mine_only)

    def listburnhistory(self, maxBlockHeight: int = None, depth: int = None, token: str = None, txtype: str = None,
                        limit: int = None) -> [{}]:  # 14
        """
        Returns information about burn history.

        :param maxBlockHeight: (optional) Optional height to iterate from (down to genesis block), (default = chaintip).
        :type maxBlockHeight: int
        :param depth: (optional) Maximum depth, from the genesis block is the default
        :type depth: int
        :param token: (optional) Filter by token
        :type token: str
        :param txtype: (optional) Filter by transaction type, supported letter from {CustomTxType}
        :type txtype: str
        :param limit: (optional) Maximum number of records to return, 100 by default
        :type limit: int
        :return: [{},{}, ...] (json array) -- objects with burn history information

        :example:

            >>> node.accounts.listburnhistory(160, 10)
        """
        options = BuildJson()
        options.append("maxBlockHeight", maxBlockHeight)
        options.append("depth", depth)
        options.append("token", token)
        options.append("txtype", txtype)
        options.append("limit", limit)

        return self._node._rpc.call("listburnhistory", options.build())

    def listcommunitybalances(self) -> {}:  # 15
        """
        Returns information about all community balances.

        :return: {balance_type:value,...} (json) -- Json object with accounts information

        :example:

            >>> node.accounts.listcommunitybalances()
        """
        return self._node._rpc.call("listcommunitybalances")

    def listpendingdusdswaps(self) -> {}:  # 16
        """
        Get all pending DFI-to_DUSD swaps.

        :return: [{...}] (json array) -- array containing json-objects having following fields

        .. code-block:: text

            {
                owner : "address"
                amount :      n.nnnnnnnn
            }

        :example:

            >>> node.accounts.listpendingdusdswaps()

        """
        return self._node._rpc.call("listpendingdusdswaps")

    def listpendingfutureswaps(self) -> {}:  # 17
        """
        Get all pending futures.

        :return: [{...}] (json array) -- array containing json-objects having following fields:

        .. code-block:: text

            {
                owner : "address"
                values : [{
                    tokenSymbol : "SYMBOL"
                    amount : n.nnnnnnnn
                    destination : "SYMBOL"
                }...]
            }

        :example:

            >>> node.accounts.listpendingfutureswaps()
        """
        return self._node._rpc.call("listpendingfutureswaps")

    def sendtokenstoaddress(self, _from: {}, to: {}, selectionMode: str = "pie") -> str:  # 18
        """
        Creates (and submits to local node and network) a transfer transaction from your accounts balances (may be picked manualy or autoselected) to the specfied accounts.

        :param _from: (required) :ref:`Node Address Amount`
        :type _from: json object
        :param to: (required) :ref:`Node Address Amount`
        :type to: json object
        :param selectionMode: (optional) If param "from" is empty this param indicates accounts autoselection mode.
                            May be once of:
                            "forward" - Selecting accounts without sorting, just as address list sorted.
                            "crumbs" - Selecting accounts by ascending of sum token amounts. It means that we will select first accounts with minimal sum of neccessary token amounts.
                            "pie" - Selecting accounts by descending of sum token amounts. It means that we will select first accounts with maximal sum of neccessary token amounts.
        :type selectionMode: str
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.accounts.sendtokenstoaddress({"srcAddress1":"2.0@DFI", "srcAddress2":["3.0@DFI", "2.0@ETH"]}, {"dstAddress1":["5.0@DFI", "2.0@ETH"]})
        """
        return self._node._rpc.call("sendtokenstoaddress", _from, to, selectionMode)

    def sendutxosfrom(self, _from: str, to: str, amount: int, change: str = None) -> str:  # 19
        """
        Send a transaction using UTXOs from the specfied address.

        :param _from: (required) The address of sender
        :type _from: str
        :param to: (required) The address of receiver
        :type to: str
        :param amount: (required) The amount to send
        :type amount: int
        :param change: (optional) The address to send change to (Default: from address)
        :type change: str
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.accounts.sendutxosfrom(from_address, to_address, 100)
        """
        change = _from if change is None else change
        return self._node._rpc.call("sendutxosfrom", _from, to, amount, change)

    def utxostoaccount(self, amounts: {}, inputs: [{}] = None) -> str:  # 20
        """
        Creates (and submits to local node and network) a transfer transaction from the wallet UTXOs to specfied account.
        The second optional argument (may be empty array) is an array of specific UTXOs to spend.

        :param amounts: (required) :ref:`Node Address Amount`
        :type amounts: json object
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.accounts.utxostoaccount({"address1":"1.0@DFI"})
        """
        return self._node._rpc.call("utxostoaccount", amounts, inputs)

    def withdrawfutureswap(self, address: str, amount: str, destination: str = "", inputs: [{}] = None) -> str:  # 21
        """
        Creates and submits to the network a withdrawal from futures contract transaction.
        Withdrawal will be back to the address specified in the futures contract.

        :param address: (required) Address used to fund contract with
        :type address: str
        :param amount: (required) :ref:`Node Amount`
        :type amount: str
        :param destination: (optional) The dToken if DUSD supplied
        :type destination: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.accounts.withdrawfutureswap(address, "1@TSLA")
            >>> node.accounts.withdrawfutureswap(address, "1000@DUSD", "TSLA")
        """
        return self._node._rpc.call("withdrawfutureswap", address, amount, destination, inputs)
