# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Tokens.ts

class Tokens:
    def __init__(self, ocean):
        self.ocean = ocean

    def list(self, size=30, next=None):
        return self.ocean._conn.get("tokens", size=size, next=next)

    def get(self, id):
        return self.ocean._conn.get(f"tokens/{id}")
