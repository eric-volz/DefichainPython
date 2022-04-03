from ..util import BuildJson


class Vault:
    def __init__(self, node):
        self.node = node

    def closevault(self, vaultId, to, inputs=None):  # 01
        return self.node.rpc.call("closevault", vaultId, to, inputs)

    def createvault(self, ownerAddress, loanSchemeId=None, inputs=None):  # 02
        loanSchemeId = "" if loanSchemeId is None else loanSchemeId
        return self.node.rpc.call("createvault", ownerAddress, loanSchemeId, inputs)

    def deposittovault(self, vaultId, _from, token, amount, inputs=None):  # 03
        return self.node.rpc.call("deposittovault", vaultId, _from, f"{amount}@{token}", inputs)

    def estimatecollateral(self, loanAmounts, targetRatio, tokens=None):  # 04
        return self.node.rpc.call("estimatecollateral", loanAmounts, targetRatio, tokens)

    def estimateloan(self, vaultId, tokens, targetRatio=None):  # 05
        return self.node.rpc.call("estimateloan", vaultId,tokens, targetRatio)

    def estimatevault(self, collateralAmounts, loanAmounts):  # 06
        return self.node.rpc.call("estimatevault", collateralAmounts, loanAmounts)

    def getvault(self, vaultId):  # 07
        return self.node.rpc.call("getvault", vaultId)

    def listauctionhistory(self, identifier, maxBlockHeight=None, vaultId=None, index=None, limit=None):  # 08
        pagination = BuildJson()
        pagination.append("maxBlockHeight", maxBlockHeight)
        pagination.append("vaultId", vaultId)
        pagination.append("index", index)
        pagination.append("limit", limit)
        return self.node.rpc.call("listauctionhistory", identifier, pagination.build())

    def listauctions(self, vaultId=None, height=None, including_start=None, limit=None):  # 09
        start = BuildJson()
        start.append("vaultId", vaultId)
        start.append("height", height)
        start = None if start.build() is {} else start.build()
        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self.node.rpc.call("listauctions", pagination.build())

    def listvaulthistory(self, vaultId, maxBlockHeight=None, depth=None, token=None, txtype=None, limit=None):  # 10
        options = BuildJson()
        options.append("maxBlockHeight", maxBlockHeight)
        options.append("depth", depth)
        options.append("token", token)
        options.append("txtype", txtype)
        options.append("limit", limit)
        return self.node.rpc.call("listvaulthistory", vaultId, options.build())

    def listvaults(self, ownerAddress=None, loanSchemeId=None, state=None, verbose=None, start=None,
                   including_start=None, limit=None):  # 11
        options = BuildJson()
        options.append("ownerAddress", ownerAddress)
        options.append("loanSchemeId", loanSchemeId)
        options.append("state", state)
        options.append("verbose", verbose)

        pagination = BuildJson()
        pagination.append("start", start)
        pagination.append("including_start", including_start)
        pagination.append("limit", limit)
        return self.node.rpc.call("listvaults", options.build(), pagination.build())

    def placeauctionbid(self, vaultId, index, _from, token, amount, inputs=None):  # 12
        return self.node.rpc.call("placeauctionbid", vaultId, index, _from, f"{amount}@{token}", inputs)

    def updatevault(self, vaultId, ownerAddress, loanSchemeId, inputs=None):  # 13
        parameters = BuildJson()
        parameters.append("ownerAddress", ownerAddress)
        parameters.append("loanSchemeId", loanSchemeId)
        return self.node.rpc.call("updatevault", vaultId, parameters.build(), inputs)

    def withdrawfromvault(self, vaultId, to, token, amount, inputs=None):  # 14
        return self.node.rpc.call("withdrawfromvault", vaultId, to, f"{amount}@{token}", inputs)
