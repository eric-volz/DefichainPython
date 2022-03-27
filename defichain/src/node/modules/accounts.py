from ..util import BuildJson


class Accounts:
    def __init__(self, node):
        self.node = node

    def accounthistorycount(self, owner, no_rewards=None, token=None, txtype=None):  # 01
        """
        Returns count of account history.

        Parameters
        ----------
        owner : str
            (required, string) Single account ID (CScript or address) or reserved words: "mine" - to list history for all owned accounts
            or "all" to list whole DB (default = "mine")


        no_rewards : bool
            (optional, boolean) Filter out rewards


        token : str
            (optional, string) Filter by token


        txtype : str
            (optional, string) Filter by transaction type, supported letter from {CustomTxType}


        Returns
        -------
        int
            (int) Count of account history
        """
        j = BuildJson()
        j.append("no_rewards", no_rewards)
        j.append("token", token)
        j.append("txtype", txtype)
        return self.node.rpc.call("accounthistorycount", owner, j.build())

    def accounttoaccount(self, _from, to, inputs=None):  # 02
        """
        Creates (and submits to local node and network) a transfer transaction from the specified account to the
        specfied accounts.The first optional argument (may be empty array) is an array of specific UTXOs to spend.

        Parameters
        ----------
        _from :
            (string, required) The defi address of sender


        to :
            (json object, required) The defi address is the key, the value is amount in amount@token format. If multiple
            tokens are to be transferred, specify an array ["amount1@t1", "amount2@t2"]
            --> Can be build with "BuildToJson" Class from Utils


        inputs :
            (optional) A json array of json objects


        Returns
        -------
        str
            The hex-encoded hash of broadcasted transaction
        """
        return self.node.rpc.call("accounttoaccount", _from, to, inputs)

    def accounttoutxos(self, _from, to, inputs=None):  # 03
        """
        Creates (and submits to local node and network) a transfer transaction from the specified account to UTXOs.
        The third optional argument (may be empty array) is an array of specific UTXOs to spend.

        Parameters
        ----------
        _from: str
            (string, required) The defi address of sender


        to:
            (string, required) The defi address is the key, the value is amount in amount@token format. Just to send DFI
            --> Can be build with "BuildToJson" Class from Utils


        inputs:
            (json array, optional) A json array of json objects


        Returns
        -------
            str
                (string) The hex-encoded hash of broadcasted transaction
        """
        return self.node.rpc.call("accounttoutxos", _from, to, inputs)

    def executesmartcontract(self, name, amount, address=None, inputs=None):  # 04
        return self.node.rpc.call("executesmartcontract", name, amount, address, inputs)

    def getaccount(self, owner, start=None, including_start=None, limit=None, indexed_amounts=None):  # 05
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)

        return self.node.rpc.call("getaccount", owner, pagination.build(), indexed_amounts)

    def getaccounthistory(self, owner, blockheight, txn):  # 06
        return self.node.rpc.call("getaccounthistory", owner, blockheight, txn)

    def getburninfo(self):  # 07
        return self.node.rpc.call("getburninfo")

    def gettokenbalances(self, start=None, including_start=None, limit=None, indexed_amounts=None, symbol_lookup=None):  # 08
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)

        indexed_amounts = False if indexed_amounts is None else indexed_amounts

        return self.node.rpc.call("gettokenbalances", pagination.build(), indexed_amounts, symbol_lookup)

    def listaccounthistory(self, owner, maxBlockHeight=None, depth=None, no_rewards=None, token=None, txtype=None, limit=None):  # 09
        options = BuildJson()
        options.append("maxBlockHeight", maxBlockHeight)
        options.append("depth", depth)
        options.append("no_rewards", no_rewards)
        options.append("token", token)
        options.append("txtype", txtype)
        options.append("limit", limit)

        return self.node.rpc.call("listaccounthistory", owner, options.build())

    def listaccounts(self, start=None, including_start=None, limit=None, verbose=None, indexed_amounts=None, is_mine_only=None):  # 10
        pagnation = BuildJson()
        pagnation.append("start", start)
        pagnation.append("including_start", including_start)
        pagnation.append("limit", limit)

        verbose = True if verbose is None else verbose
        indexed_amounts = False if indexed_amounts is None else indexed_amounts

        return self.node.rpc.call("listaccounts", pagnation.build(), verbose, indexed_amounts, is_mine_only)

    def listburnhistory(self, maxBlockHeight=None, depth=None, token=None, txtype=None, limit=None):  # 11
        options = BuildJson()
        options.append("maxBlockHeight", maxBlockHeight)
        options.append("depth", depth)
        options.append("token", token)
        options.append("txtype", txtype)
        options.append("limit", limit)

        return self.node.rpc.call("listburnhistory", options.build())

    def listcommunitybalances(self):  # 12
        return self.node.rpc.call("listcommunitybalances")

    def sendtokenstoaddress(self, _from, to, selectionMode=None):  # 13
        return self.node.rpc.call("sendtokenstoaddress", _from, to, selectionMode)

    def sendutxosfrom(self, _from, to, amount, change=None):  # 14
        return self.node.rpc.call("sendutxosfrom", _from, to, amount, change)

    def utxostoaccount(self, amounts, inputs=None):  # 15
        return self.node.rpc.call("utxostoaccount", amounts, inputs)