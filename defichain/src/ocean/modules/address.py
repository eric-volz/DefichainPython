#  https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Address.ts

class Address:
    def __init__(self, ocean):
        self.ocean = ocean

    def listAccountHistory(self, address, size=30, next=None):
        return self.ocean.conn.call(f"address/{address}/history", size=size, next=next)

