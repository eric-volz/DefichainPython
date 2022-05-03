class Control:
    def __init__(self, node):
        self._node = node

    def getmemoryinfo(self, mode="stats"):  # 01
        return self._node._rpc.call("getmemoryinfo", mode)

    def getrpcinfo(self):  # 02
        return self._node._rpc.call("getrpcinfo")

    def help(self, command=None):  # 03
        return self._node._rpc.call("help", command)

    def logging(self, include=[], exclude=[]):  # 04
        return self._node._rpc.call("logging", include, exclude)

    def stop(self):  # 05
        return self._node._rpc.call("stop")

    def uptime(self):  # 06
        return self._node._rpc.call("uptime")
