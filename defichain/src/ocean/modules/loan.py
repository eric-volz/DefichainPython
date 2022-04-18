# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Loan.ts

class Loan:
    def __init__(self, ocean):
        self.ocean = ocean

    def listScheme(self, size=30, next=None):
        return self.ocean.conn.call(f"loans/schemes", size=size, next=next)
