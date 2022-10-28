from ..util import BuildJson


class Loan:
    def __init__(self, node):
        self._node = node

    def createloanscheme(self, mincolratio: int, interestrate: float, id: str, inputs: [{}] = None) -> str:  # 01
        """
        Creates a loan scheme transaction.

        :param mincolratio: (required) Minimum collateralization ratio (integer)
        :type mincolratio: int
        :param interestrate: (required) Interest rate (integer or float)
        :type interestrate: float
        :param id: (required) Unique identifier of the loan scheme (8 chars max)
        :type id: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.loan.createloanscheme(150, 5, "MyScheme")
        """
        return self._node._rpc.call("createloanscheme", mincolratio, interestrate, id, inputs)

    def destroyloanscheme(self, id: str, ACTIVATE_AFTER_BLOCK: int = None, inputs: [{}] = None) -> str:  # 02
        """
        Destroys a loan scheme.

        :param id: (required) Unique identifier of the loan scheme (8 chars max)
        :type id: str
        :param ACTIVATE_AFTER_BLOCK: (optional) Block height at which new changes take effect
        :type ACTIVATE_AFTER_BLOCK: int
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.loan.destroyloanscheme("MyScheme")
        """
        ACTIVATE_AFTER_BLOCK = self._node.blockchain.getblockcount() + 1 if ACTIVATE_AFTER_BLOCK is None else ACTIVATE_AFTER_BLOCK
        return self._node._rpc.call("destroyloanscheme", id, ACTIVATE_AFTER_BLOCK, inputs)

    def getcollateraltoken(self, token: str) -> {}:  # 03
        """
        Return collateral token information.

        :param token: (required) Symbol or id of collateral token
        :type token: str
        :return: {...} (json) -- Json object with collateral token information

        :example:

            >>> node.loan.getcollateraltoken("DFI")
        """
        return self._node._rpc.call("getcollateraltoken", token)

    def getinterest(self, id: str, token: str = "") -> {}:  # 04
        """
        Returns the global and per block interest by loan scheme.

        :param id: (required) Unique identifier of the loan scheme (8 chars max)
        :type id: str
        :param token: (optional) The token's symbol, id or creation tx
        :type token: str
        :return: {...} (json) -- Json object with interest information

            .. code-block:: text

               interestPerBlock: Interest per block is always ceiled
               to the min. unit of fi (8 decimals), however interest
               less than this will continue to accrue until actual utilization
               (eg. - payback of the loan), or until sub-fi maturity.

               realizedInterestPerBlock: The actual realized interest
               per block. This is continues to accumulate until
               the min. unit of the blockchain (fi) can be realized.

        :example:

            >>> node.loan.getinterest("MyScheme", "DUSD")
        """
        return self._node._rpc.call("getinterest", id, token)

    def getloaninfo(self) -> {}:  # 05
        """
        Returns the loan stats.

        :return: {...} (json) -- Json object with loan information

        :example:

            >>> node.loan.getloaninfo()
        """
        return self._node._rpc.call("getloaninfo")

    def getloanscheme(self, id: str) -> {}:  # 06
        """
        Returns information about loan scheme.

        :param id: (required) Unique identifier of the loan scheme (8 chars max)
        :type id: str
        :return: {...} (json) -- returns loanscheme from id

            .. code-block:: text

                {
                    "id" : n                   (string)
                    "mincolratio" : n          (numeric)
                    "interestrate" : n         (numeric)
                }

        :example:

            >>> node.loan.getloanscheme("MyScheme")
        """
        return self._node._rpc.call("getloanscheme", id)

    def getloantoken(self, token: str) -> {}:  # 07
        """
        Return loan token information.

        :param token: (required) Symbol or id of loan token
        :type token: str
        :return: {...} (json) -- Json object with loan token information

        :example:

            >>> node.loan.getloantoken("DUSD")
        """
        return self._node._rpc.call("getloantoken", token)

    def listcollateraltokens(self) -> {}:  # 08
        """
        Return list of all created collateral tokens. If no parameters passed
        it will return all current valid setcollateraltoken transactions

        :return: {...} (json) -- Json object with collateral token information

        :example:

            >>> node.loan.listcollateraltokens()
        """
        return self._node._rpc.call("listcollateraltokens")

    def listloanschemes(self) -> [{}]:  # 09
        """
        List all available loan schemes.

        :return: [{...}] (json array) -- returns list of loan schemes

            .. code-block:: text

                [                              (json array of objects)
                    {
                    "id" : n                   (string)
                    "mincolratio" : n          (numeric)
                    "interestrate" : n         (numeric)
                    },
                    ...
                ]

        :example:

            >>> node.loan.listloanschemes()
        """
        return self._node._rpc.call("listloanschemes")

    def listloantokens(self) -> {}:  # 10
        """
        Return list of all created loan tokens.

        :return: {...} (json) -- Json object with loan token information

        :example:

            >>> node.loan.listloantokens()
        """
        return self._node._rpc.call("listloantokens")

    def paybackloan(self, vaultId: str, _from: str, amounts: str = None, loans: [{}] = None, inputs: [{}] = None) -> str:  # 11
        """
        Creates (and submits to local node and network) a tx to return the loan in desired amount.

        :param vaultId: (required) Id of vault used for loan
        :type vaultId: str
        :param _from: (required) Address containing repayment tokens. If "from" value is: "*" (star), it's means auto-selection accounts from wallet.
        :type _from: str
        :param amounts: (optional) :ref:`Node Address Amount`
        :type amounts: str
        :param loans: (optional) A json array of json objects

            .. code-block:: text

                [
                    {                      (json object)
                    "dToken": "str",     (string, required) The dTokens's symbol, id or creation tx
                    "amounts": "str",    (string, required) Amount in amount@token format.
                    },
                    ...
                ]

        :type loans: json array
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.loan.paybackloan("84b22eee1964768304e624c416f29a91d78a01dc5e8e12db26bdac0670c67bb2", "mxxA2sQMETJFbXcNbNbUzEsBCTn1JSHXST", "10@TSLA")
        """
        metadata = BuildJson()
        metadata.append("vaultId", vaultId)
        metadata.append("from", _from)
        metadata.append("amounts", amounts)
        metadata.append("loans", loans)
        return self._node._rpc.call("paybackloan", metadata.build(), inputs)

    def setcollateraltoken(self, token: str, factor: float, fixedIntervalPriceId: str, activateAfterBlock: int = None, inputs: [{}] = None) -> str:  # 12
        """
        Creates (and submits to local node and network) a set colleteral token transaction.

        :param token: (required) Symbol or id of collateral token
        :type token: str
        :param factor: (required) Collateralization factor
        :type factor: float
        :param fixedIntervalPriceId: (required) token/currency pair to use for price of token
        :type fixedIntervalPriceId: str
        :param activateAfterBlock: (optional) changes will be active after the block height
        :type activateAfterBlock: int
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.loan.setcollateraltoken("TSLA", 150, "TSLA/USD")
        """
        metadata = BuildJson()
        metadata.append("token", token)
        metadata.append("factor", factor)
        metadata.append("fixedIntervalPriceId", fixedIntervalPriceId)
        metadata.append("activateAfterBlock", activateAfterBlock)
        return self._node._rpc.call("setcollateraltoken", metadata.build(), inputs)

    def setdefaultloanscheme(self, id: str, inputs: [{}] = None) -> str:  # 13
        """
        Sets the default loan scheme.

        :param id: (required) Unique identifier of the loan scheme (8 chars max).
        :type id: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.loan.setdefaultloanscheme("MyScheme")
        """
        return self._node._rpc.call("setdefaultloanscheme", id, inputs)

    def setloantoken(self, symbol: str, fixedIntervalPriceId: str, name: str = None, mintable: bool = True, interest: float = 0, inputs: [{}] = None) -> str:  # 14
        """
        Creates (and submits to local node and network) a token for a price feed set in collateral token.

        :param symbol: (required) Token's symbol (unique), not longer than 8
        :type symbol: str
        :param fixedIntervalPriceId: (required) token/currency pair to use for price of token
        :type fixedIntervalPriceId: str
        :param name: (optional) Token's name, not longer than 128
        :type name: str
        :param mintable: (optional) Token's 'Mintable' property, default is 'True'
        :type mintable: bool
        :param interest: (optional) Interest rate (default: 0)
        :type interest: float
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.loan.setloantoken("TSLA", "TSLA/USD", "TSLA Stock", True, 5)
        """
        metadata = BuildJson()
        metadata.append("symbol", symbol)
        metadata.append("name", name)
        metadata.append("fixedIntervalPriceId", fixedIntervalPriceId)
        metadata.append("mintable", mintable)
        metadata.append("interest", interest)
        return self._node._rpc.call("setloantoken", metadata.build(), inputs)

    def takeloan(self, vaultId: str, amounts: str, to: str = None, inputs: [{}] = None) -> str:  # 15
        """
        Creates (and submits to local node and network) a tx to mint loan token in desired amount based on defined loan.

        :param vaultId: (required) Id of vault used for loan
        :type vaultId: str
        :param amounts: (required) :ref:`Node Address Amount`
        :type amounts: str
        :param to: (optional) Address to transfer tokens
        :type to: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.loan.takeloan("84b22eee1964768304e624c416f29a91d78a01dc5e8e12db26bdac0670c67bb2", "10@SPY")
        """
        metadata = BuildJson()
        metadata.append("vaultId", vaultId)
        metadata.append("to", to)
        metadata.append("amounts", amounts)
        return self._node._rpc.call("takeloan", metadata.build(), inputs)

    def updateloanscheme(self, mincolratio: int, interestrate: float, id: str, ACTIVATE_AFTER_BLOCK: int = None, inputs: [{}] = None) -> str:  # 16
        """
        Updates an existing loan scheme.

        :param mincolratio: (required) Minimum collateralization ratio
        :type mincolratio: int
        :param interestrate: (required) Interest rate
        :type interestrate: float
        :param id: (required) Unique identifier of the loan scheme
        :type id: str
        :param ACTIVATE_AFTER_BLOCK: (optional) Block height at which new changes take effect
        :type ACTIVATE_AFTER_BLOCK: int
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.loan.updateloanscheme(150, 5, "MyScheme")
        """
        ACTIVATE_AFTER_BLOCK = self._node.blockchain.getblockcount() + 1 if ACTIVATE_AFTER_BLOCK is None else ACTIVATE_AFTER_BLOCK
        return self._node._rpc.call("updateloanscheme", mincolratio, interestrate, id, ACTIVATE_AFTER_BLOCK, inputs)

    def updateloantoken(self, token: str, symbol: str = None, name: str = None, fixedIntervalPriceId: str = None, mintable: bool = True, interest: float = None, inputs: [{}] = None) -> str:  # 17
        """
        Creates (and submits to local node and network) a transaction to update loan token metadata.

        :param token: (required) The tokens's symbol, id or creation tx
        :type token: str
        :param symbol: (optional) New token's symbol (unique), not longer than 8
        :type symbol: str
        :param name: (optional) New token's name, not longer than 128
        :type name: str
        :param fixedIntervalPriceId: (optional) token/currency pair to use for price of token
        :type fixedIntervalPriceId: str
        :param mintable: (optional) Token's 'Mintable' property, default is 'True'
        :type mintable: bool
        :param interest: (optional) Interest rate
        :type interest: float
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.loan.updateloantoken("TSLA", "TSLAA", "TSLA Stock", "TSLA/USD", True, 5)
        """
        metadata = BuildJson()
        metadata.append("symbol", symbol)
        metadata.append("name", name)
        metadata.append("fixedIntervalPriceId", fixedIntervalPriceId)
        metadata.append("mintable", mintable)
        metadata.append("interest", interest)
        return self._node._rpc.call("updateloantoken", token, metadata.build(), inputs)
