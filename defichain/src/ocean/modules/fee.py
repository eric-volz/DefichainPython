# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Fee.ts

class Fee:
    def __init__(self, ocean):
        self.ocean = ocean

    def estimate(self, confirmationTarget=10):
        return self.ocean.conn.call(f"fee/estimate?confirmationTarget={confirmationTarget}")
