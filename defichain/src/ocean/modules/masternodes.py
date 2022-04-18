# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/MasterNodes.ts

class Masternodes:
    def __init__(self, ocean):
        self.ocean = ocean

    def list(self, size=30, next=None):  # 01
        return self.ocean._conn.call("masternodes", size=size, next=next)

    def get(self, id):  # 02
        return self.ocean._conn.call(f"masternodes/{id}")
