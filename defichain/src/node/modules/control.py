class Control:
    def __init__(self, node):
        self.node = node

    def getmemoryinfo(self, mode=None):
        return self.node.rpc.call("getmemoryinfo", mode)

    def getrpcinfo(self):
        return self.node.rpc.call("getrpcinfo")

    def help(self, command=None):
        return self.node.rpc.call("help", command)

    def logging(self, include=None, exclude=None):
        include = [] if include is None else include
        return self.node.rpc.call("logging", include, exclude)

    def stop(self):
        return self.node.rpc.call("stop")

    def uptime(self):
        return self.node.rpc.call("uptime")
