from ..util import BuildJson


class Oracles:
    def __init__(self, node):
        self.node = node

    def appointoracle(self, address, pricefeeds, weightage, inputs=None):  # 01
        return self.node.rpc.call("appointoracle", address, pricefeeds, weightage, inputs)

    def getfixedintervalprice(self, fixedIntervalPriceId):  # 02
        return self.node.rpc.call("getfixedintervalprice", fixedIntervalPriceId)

    def getoracledata(self, oracleid):  # 03
        return self.node.rpc.call("getoracledata", oracleid)

    def getprice(self, currency, token):  # 04
        request = BuildJson()
        request.append("currency", currency)
        request.append("token", token)
        return self.node.rpc.call("getprice", request.build())

    def listfixedintervalprices(self, start=None, limit=None):  # 05
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("limit", limit)
        return self.node.rpc.call("listfixedintervalprices", pagination.build())

    def listlatestrawprices(self, currency, token, start=None, including_start=None, limit=None):  # 06
        request = BuildJson()
        request.append("currency", currency)
        request.append("token", token)

        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self.node.rpc.call("listlatestrawprices", request.build(), pagination.build())

    def listoracles(self, start=None, including_start=None, limit=None):  # 07
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self.node.rpc.call("listoracles", pagination.build())

    def listprices(self, start=None, including_start=None, limit=None):  # 08
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self.node.rpc.call("listprices", pagination.build())

    def removeoracle(self, oracleid, inputs=None):  # 09
        return self.node.rpc.call("removeoracle", oracleid, inputs)

    def setoracledata(self, oracleid, timestamp, prices, inputs=None):  # 10
        return self.node.rpc.call("setoracledata", oracleid, timestamp, prices, inputs)

    def updateoracle(self, oracleid, timestamp, prices, weightage, inputs=None):  # 11
        return self.node.rpc.call("updateoracle", oracleid, timestamp, prices, weightage, inputs)

