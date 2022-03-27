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

    def accounttoaccount(self, _from, to, inputs=None):
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

    def accounttoutxos(self, _from, to, inputs=None):
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

    def executesmartcontract(self, name, amount, address=None, inputs=None):
        return self.node.rpc.call("executesmartcontract", name, amount, address, inputs)

    def getaccount(self, owner, start=None, including_start=None, limit=None, indexed_amounts=None):
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        pagination.append("indexed_amounts", indexed_amounts)

        return self.node.rpc.call("getaccount", owner, pagination.build())
