# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Blocks.ts

class Blocks:
    def __init__(self, ocean):
        self.ocean = ocean

    def list(self, size=30, next=None):
        return self.ocean.conn.call("blocks", size=size, next=next)

    def get(self, id):
        return self.ocean.conn.call(f"blocks/{id}")

    def getTransactions(self, hash, size=30, next=None):
        return self.ocean.conn.call(f"blocks/{hash}/transactions", size=size, next=next)
