class Control:
    def __init__(self, node):
        self.node = node

    def getmemoryinfo(self, mode=None):  # 01
        return self.node.rpc.call("getmemoryinfo", mode)

    def getrpcinfo(self):  # 02
        return self.node.rpc.call("getrpcinfo")

    def help(self, command=None):  # 03
        return self.node.rpc.call("help", command)

    def logging(self, include=None, exclude=None):  # 04
        include = [] if include is None else include
        return self.node.rpc.call("logging", include, exclude)

    def stop(self):  # 05
        return self.node.rpc.call("stop")

    def uptime(self):  # 06
        return self.node.rpc.call("uptime")
