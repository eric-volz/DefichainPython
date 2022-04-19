# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Fee.ts

class Fee:
    def __init__(self, ocean):
        self.ocean = ocean

    def estimate(self, confirmationTarget=10):  # 01
        return self.ocean._conn.get(f"fee/estimate?confirmationTarget={confirmationTarget}")
