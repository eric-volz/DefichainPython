# https://github.com/JellyfishSDK/jellyfish/blob/main/packages/whale-api-client/src/api/consortium.ts


class Consortium:
    def __init__(self, ocean):
        self._ocean = ocean

    def getAssetBreakdown(self):

        return self._ocean._conn.get("consortium/assetbreakdown")

    def getMemberStats(self, memberId: str):

        return self._ocean._conn.get(f"consortium/stats/{memberId}")
