from ..util import BuildJson


class Stats:
    def __init__(self, node):
        self._node = node

    def getrpcstats(self, command: str) -> {}:
        """
        Get RPC stats for selected command

        :param command: (required) The command to get stats for
        :type command: str
        :return: {...} (json) -- returns rpc stats

            .. code-block:: text

                {
                    "name":               (string) The RPC command name.
                    "latency":            (json object) Min, max and average latency.
                    "payload":            (json object) Min, max and average payload size in bytes.
                    "count":              (numeric) The number of times this command as been used.
                    "lastUsedTime":       (numeric) Last used time as timestamp.
                    "history":            (json array) History of last 5 RPC calls.
                    [
                        {
                        "timestamp": (numeric)
                        "latency":   (numeric)
                        "payload":   (numeric)
                        }
                    ]
                }

        :example:

            >>> node.stats.getrpcstats("getblockcount")
        """
        return self._node._rpc.call("getrpcstats", command)

    def listrpcstats(self) -> []:
        """
        List used RPC commands

        :return: {...} (json) -- returns a list of rpc stats

            .. code-block:: text

                [
                    {
                        "name":               (string) The RPC command name.
                        "latency":            (json object) Min, max and average latency.
                        "payload":            (json object) Min, max and average payload size in bytes.
                        "count":              (numeric) The number of times this command as been used.
                        "lastUsedTime":       (numeric) Last used time as timestamp.
                        "history":            (json array) History of last 5 RPC calls.
                        [
                            {
                                "timestamp": (numeric)
                                "latency":   (numeric)
                                "payload":   (numeric)
                            }
                        ]
                    }
                ]

        :example:

            >>> node.stats.listrpcstats()
        """
        return self._node._rpc.call("listrpcstats")
