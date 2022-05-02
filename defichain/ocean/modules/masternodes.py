# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/MasterNodes.ts

class Masternodes:
    def __init__(self, ocean):
        self._ocean = ocean

    def list(self, size=30, next=None):  # 01
        return self._ocean._conn.get("masternodes", size=size, next=next)

    def get(self, id):  # 02
        return self._ocean._conn.get(f"masternodes/{id}")
