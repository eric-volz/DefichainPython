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
            Single account ID (CScript or address) or reserved words: "mine" - to list history for all owned accounts
            or "all" to list whole DB (default = "mine")


            no_rewards : bool
                (optional) Filter out rewards


            token : str
                (optional) Filter by token


            txtype : str
                (optional) Filter by transaction type, supported letter from {CustomTxType}

        Returns
        -------
        int
            Count of account history
        """
        j = BuildJson()
        j.append("no_rewards", no_rewards)
        j.append("token", token)
        j.append("txtype", txtype)
        return self.node.rpc.call("accounthistorycount", owner, j.get())

    def accounttoaccount(self, _from, inputs=None, **to):
        """
        Creates (and submits to local node and network) a transfer transaction from the specified account to the
        specfied accounts.The first optional argument (may be empty array) is an array of specific UTXOs to spend.

        Parameters
        ----------
        _from : str
            (required) The defi address of sender


        inputs :
            (optional) A json array of json objects


        to :
            (required) The defi address is the key, the value is amount in amount@token format. If multiple tokens are
            to be transferred, specify an array ["amount1@t1", "amount2@t2"]

        Returns
        -------
        str
            The hex-encoded hash of broadcasted transaction
        """
        return self.node.rpc.call("accounttoaccount", _from, to, inputs)
