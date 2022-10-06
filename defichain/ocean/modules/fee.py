# https://github.com/DeFiCh/jellyfish/blob/main/packages/whale-api-client/src/api/Fee.ts

class Fee:
    def __init__(self, ocean):
        self._ocean = ocean

    def estimate(self, confirmationTarget: int = 10) -> {}:  # 01
        """
        Estimates the fee for transaction to get confirmed

        :param confirmationTarget: (optional) confirmationTarget in blocks till fee get confirmed
        :type confirmationTarget: str
        :return: (json string) {data: float}

        :example:

        >>> ocean.fee.estimate(10)
        """
        return self._ocean._conn.get(f"fee/estimate?confirmationTarget={confirmationTarget}")
