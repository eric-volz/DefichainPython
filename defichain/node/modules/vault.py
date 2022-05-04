from ..util import BuildJson


class Vault:
    def __init__(self, node):
        self._node = node

    def closevault(self, vaultId, to, inputs=None):  # 01
        return self._node._rpc.call("closevault", vaultId, to, inputs)

    def createvault(self, ownerAddress, loanSchemeId="", inputs=None):  # 02
        return self._node._rpc.call("createvault", ownerAddress, loanSchemeId, inputs)

    def deposittovault(self, vaultId, _from, amount, inputs=None):  # 03
        return self._node._rpc.call("deposittovault", vaultId, _from, amount, inputs)

    def estimatecollateral(self, loanAmounts, targetRatio, tokens={"DFI": 1}):  # 04
        return self._node._rpc.call("estimatecollateral", loanAmounts, targetRatio, tokens)

    def estimateloan(self, vaultId, tokens, targetRatio=None):  # 05
        return self._node._rpc.call("estimateloan", vaultId, tokens, targetRatio)

    def estimatevault(self, collateralAmounts, loanAmounts):  # 06
        return self._node._rpc.call("estimatevault", collateralAmounts, loanAmounts)

    def getvault(self, vaultId):  # 07
        return self._node._rpc.call("getvault", vaultId)

    def listauctionhistory(self, identifier="mine", maxBlockHeight=None, vaultId=None, index=None, limit=None):  # 08
        pagination = BuildJson()
        pagination.append("maxBlockHeight", maxBlockHeight)
        pagination.append("vaultId", vaultId)
        pagination.append("index", index)
        pagination.append("limit", limit)
        return self._node._rpc.call("listauctionhistory", identifier, pagination.build())

    def listauctions(self, vaultId=None, height=None, including_start=False, limit=100):  # 09
        start = BuildJson()
        start.append("vaultId", vaultId)
        start.append("height", height)
        start = None if start.build() is {} else start.build()
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self._node._rpc.call("listauctions", pagination.build())

    def listvaulthistory(self, vaultId, maxBlockHeight=None, depth=None, token=None, txtype=None, limit=100):  # 10
        options = BuildJson()
        options.append("maxBlockHeight", maxBlockHeight)
        options.append("depth", depth)
        options.append("token", token)
        options.append("txtype", txtype)
        options.append("limit", limit)
        return self._node._rpc.call("listvaulthistory", vaultId, options.build())

    def listvaults(self, ownerAddress=None, loanSchemeId=None, state='unknown', verbose=False, start=None,
                   including_start=False, limit=100):  # 11
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

    def placeauctionbid(self, vaultId, index, _from, amount, inputs=None):  # 12
        return self._node._rpc.call("placeauctionbid", vaultId, index, _from, amount, inputs)

    def updatevault(self, vaultId, ownerAddress, loanSchemeId, inputs=None):  # 13
        parameters = BuildJson()
        parameters.append("ownerAddress", ownerAddress)
        parameters.append("loanSchemeId", loanSchemeId)
        return self._node._rpc.call("updatevault", vaultId, parameters.build(), inputs)

    def withdrawfromvault(self, vaultId, to, amount, inputs=None):  # 14
        return self._node._rpc.call("withdrawfromvault", vaultId, to, amount, inputs)
