# https://github.com/JellyfishSDK/jellyfish/blob/main/packages/whale-api-client/src/api/consortium.ts


class Consortium:
    def __init__(self, ocean):
        self._ocean = ocean

    def getAssetBreakdown(self):
        """
        Gets the asset breakdown information of consortium members

        :return: Json String

            .. code-block::

                {
                    tokenId: string
                    id: string
                    name: string
                    backingAddresses: string[]
                    minted: string
                    burned: string
                }

        :example:

        >>> ocean.consortium.getAssetBreakdown()
        """

        return self._ocean._conn.get("consortium/assetbreakdown")

    def getMemberStats(self, memberId: str):
        """
        Gets the stats information of a specific consortium member

        :param memberId: (required) member id of the consortium member
        :type memberId: str
        :return: Json String

            .. code-block::

                {
                    memberId: string
                    memberName: string
                    mintTokens:
                    [
                        {
                        tokenSymbol: string
                        tokenDisplaySymbol: string
                        tokenId: string
                        member:
                            {
                                minted: string
                                mintedDaily: string
                                mintLimit: string
                                mintDailyLimit: string
                            }
                        token:
                            {
                                minted: string
                                mintedDaily: string
                                mintLimit: string
                                mintDailyLimit: string
                            }
                        }
                    ]
                }

        :example:

        >>> ocean.consortium.getMemberStats("memberId")
        """

        return self._ocean._conn.get(f"consortium/stats/{memberId}")
