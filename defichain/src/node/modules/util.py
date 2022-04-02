class Util:
    def __init__(self, node):
        self.node = node

    def createmultisig(self, nrequired, keys, address_type=None):  # 01
        return self.node.rpc.call("createmultisig", nrequired, keys, address_type)

    def deriveaddresses(self, descriptor, range=None):  # 02
        return self.node.rpc.call("deriveaddresses", descriptor, range)

    def estimatesmartfee(self, conf_target, estimate_mode=None):  # 03
        return self.node.rpc.call("estimatesmartfee", conf_target, estimate_mode)

    def getdescriptorinfo(self):  # 04
        pass

    def signmessagewithprivkey(self):  # 05
        pass

    def validateaddress(self):  # 06
        pass

    def verifymessage(self):  # 07
        pass
