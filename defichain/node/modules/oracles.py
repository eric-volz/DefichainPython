from ..util import BuildJson


class Oracles:
    def __init__(self, node):
        self._node = node

    def appointoracle(self, address: str, pricefeeds: [{}], weightage: float, inputs: [{}] = None) -> str:  # 01
        """
        Creates (and submits to local node and network) a `appoint oracle transaction`,
        and saves oracle to database.

        The last optional argument (may be empty array) is an array of specific UTXOs to spend.
        Requires wallet passphrase to be set with walletpassphrase call.


        :param address: (required) oracle address
        :type address: str
        :param pricefeeds: (required) list of allowed token-currency pairs
        :type pricefeeds: json array
        :param weightage: (required) oracle weightage
        :type weightage: float
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.oracles.appointoracle("mwSDMvn1Hoc8DsoB7AkLv7nxdrf5Ja4jsF", [{"currency": "USD", "token": "BTC"}, {"currency": "EUR", "token":"ETH"}], 20)
        """
        return self._node._rpc.call("appointoracle", address, pricefeeds, weightage, inputs)

    def getdusdswapblock(self) -> int:
        """
        Get the next block that DFI to DUSD swap will execute on.

        :return: n (int) -- DFI to DUSD swap execution block. Zero if not set.

        :example:

            >>> node.oracles.getdusdswapblock()
        """
        return self._node._rpc.call("getdusdswapblock")  # 02

    def getfixedintervalprice(self, fixedIntervalPriceId: str) -> {}:  # 03
        """
        Get fixed interval price for a given pair.

        :param fixedIntervalPriceId: (required) token/currency pair to use for price of token
        :type fixedIntervalPriceId: str
        :return: {...} (json) -- returns fixed interval price of token

            .. code-block:: text

                {
                    'fixedIntervalPriceId': 'token/currency',
                    'activePrice': n.nnnnnnnn,
                    'nextPrice': n.nnnnnnnn,
                    'activePriceBlock': n,
                    'nextPriceBlock': n,
                    'timestamp': n,
                    'isLive': True|False
                }

        :example:

            >>> node.oracles.getfixedintervalprice("TSLA/USD")
        """
        return self._node._rpc.call("getfixedintervalprice", fixedIntervalPriceId)

    def getfutureswapblock(self) -> int:  # 04
        """
        Get the next block that futures will execute and update on

        :return: n (numeric) -- Futures execution block. Zero if not set

        :example:

            >>> node.oracles.getfutureswapblock()
        """
        return self._node._rpc.call("getfutureswapblock")

    def getoracledata(self, oracleid: str) -> {}:  # 05
        """
        Returns oracle data in json form

        :param oracleid: (required) oracle hex id
        :type oracleid: str
        :return: {...} (string) -- oracle data in json form

        :example:

            >>> node.noracles.getoracledata()
        """
        return self._node._rpc.call("getoracledata", oracleid)

    def getprice(self, token: str, currency: str) -> float:  # 06
        """
        The only argument is a json-form request containing token and currency names

        :param token: (required) token name
        :type token: str
        :param currency: (required) currency name
        :type currency: str
        :return: float -- returns price of token in given currency

        :example:

            >>> node.oracles.getprice("TSLA", "USD")
        """
        request = BuildJson()
        request.append("currency", currency)
        request.append("token", token)
        return self._node._rpc.call("getprice", request.build())

    def listfixedintervalprices(self, start: int = None, limit: int = 100) -> {}:  # 07
        """
        Get all fixed interval prices

        :param start: (optional) Optional first key to iterate from, in lexicographical order.Typically it's set to last ID from previous request
        :type start: int
        :param limit: (optional) Maximum number of fixed interval prices to return
        :type limit: int
        :return: {...} (json) -- returns fixed interval prices

            .. code-block:: text

                {
                    'priceFeedId': 'token/currency',
                    'activePrice': n.nnnnnnnn,
                    'nextPrice': n.nnnnnnnn,
                    'timestamp': n,
                    'isLive': True|False
                }

        :example:

            >>> node.oracles.listfixedintervalprices()
        """
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listfixedintervalprices", pagination.build())

    def listlatestrawprices(self, token: str, currency: str, start: str = None, including_start: bool = None, limit: int = 100) -> {}:  # 08
        """
        Returns latest raw price updates through all the oracles for specified token and currency

        :param token: (required) currency name
        :type token: str
        :param currency: (required) token name
        :type currency: str
        :param start: (optional) Optional first key to iterate from, in lexicographical order. Typically it's set to last ID from previous request
        :type start: str
        :param including_start: (optional) If true, then iterate including starting position
        :type including_start: bool
        :param limit: (optional) Maximum number of orders to return
        :type limit: int
        :return: {...} (json) -- Array of json objects containing full information about token prices

        :example:

            >>> node.oracles.listlatestrawprices("TSLA", "USD")
        """
        request = BuildJson()
        request.append("currency", currency)
        request.append("token", token)

        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listlatestrawprices", request.build(), pagination.build())

    def listoracles(self, start: str = None, including_start: bool = None, limit: int = 100) -> []:  # 09
        """
        Returns list of oracle ids

        :param start: (optional) Optional first key to iterate from, in lexicographical order. Typically it's set to last ID from previous request
        :type start: str
        :param including_start: (optional) If true, then iterate including starting position
        :type including_start: bool
        :param limit: (optional) Maximum number of orders to return
        :type limit: int
        :return: [...] (array) -- list of known oracle ids

        :example:

            >>> node.oracles.listoracles()
        """

        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listoracles", pagination.build())

    def listprices(self, start: int = None, including_start: bool = None, limit: int = 100) -> {}:  # 10
        """
        Calculates aggregated prices for all supported pairs (token, currency)

        :param start: (optional) Optional first key to iterate from, in lexicographical order.Typically it's set to last ID from previous request
        :type start: int
        :param including_start: (optional) If true, then iterate including starting position
        :type including_start: bool
        :param limit: (optional) Maximum number of orders to return
        :type limit: int
        :return: [{...}] (json array) -- array containing json-objects with information

        .. code-block:: text

            {
                'token': string,
                'currency': string,
                'price': n.nnnnnnn,
                'ok': True|False
            }

        :example:

            >>> node.oracles.listprices()
        """
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listprices", pagination.build())

    def removeoracle(self, oracleid: str, inputs: [{}] = None) -> str:  # 11
        """
        Removes oracle,
        The only argument is oracleid hex value.

        :param oracleid: (required) oracle id
        :type oracleid: str
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.oracles.removeoracle("0xabcd1234ac1243578697085986498694")
        """
        return self._node._rpc.call("removeoracle", oracleid, inputs)

    def setoracledata(self, oracleid: str, timestamp: int, prices: [{}], inputs: [{}] = None) -> str:  # 12
        """
        Creates (and submits to local node and network) a `set oracle data transaction`.

        The last optional argument (may be empty array) is an array of specific UTXOs to spend.
        Requires wallet passphrase to be set with walletpassphrase call.

        :param oracleid: (required) oracle hex id
        :type oracleid: str
        :param timestamp: (required) balances timestamp
        :type timestamp: int
        :param prices: (required) tokens raw prices:the array of price and token strings in price@token format

            .. code-block:: text

                [
                    {                            (json object)
                        "currency": "str",       (string, required) Currency name
                        "tokenAmount": "str",    (string, required) Amount@token
                    },
                    ...
                ]

        :type prices: json array
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.oracles.setoracledata("5474b2e9bfa96446e5ef3c9594634e1aa22d3a0722cb79084d61253acbdf87bf", 1612237937, [{"currency":"USD", "tokenAmount":"38293.12@BTC"}, {"currency":"EUR", "tokenAmount":"1328.32@ETH"}])
        """
        return self._node._rpc.call("setoracledata", oracleid, timestamp, prices, inputs)

    def updateoracle(self, oracleid: str, address: str, pricefeeds: [{}], weightage: int, inputs: [{}] = None) -> str:  # 13
        """
        Creates (and submits to local node and network) a `update oracle transaction`,
        and saves oracle updates to database.

        The last optional argument (may be empty array) is an array of specific UTXOs to spend.
        Requires wallet passphrase to be set with walletpassphrase call.

        :param oracleid: (required) oracle id
        :type oracleid: str
        :param address: (required) oracle address
        :type address: str
        :param pricefeeds: (required) list of allowed token-currency pairs

            .. code-block:: text

                [
                    {                       (json object)
                        "currency": "str",  (string, required) Currency name
                        "token": "str",     (string, required) Token name
                    },
                    ...
                ]

        :type pricefeeds: json array
        :param weightage: (required) oracle weightage
        :type weightage: int
        :param inputs: (optional) :ref:`Node Inputs`
        :type inputs: json array
        :return: "hash" (string) -- The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.oracles.setoracledata("5474b2e9bfa96446e5ef3c9594634e1aa22d3a0722cb79084d61253acbdf87bf", "mwSDMvn1Hoc8DsoB7AkLv7nxdrf5Ja4jsF", [{"currency":"USD", "tokenAmount":"38293.12@BTC"}, {"currency":"EUR", "tokenAmount":"1328.32@ETH"}], 20)
        """
        return self._node._rpc.call("updateoracle", oracleid, address, pricefeeds, weightage, inputs)

