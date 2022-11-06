class Control:
    def __init__(self, node):
        self._node = node

    def getmemoryinfo(self, mode: str = "stats") -> {}:  # 01
        """
        Returns an object containing information about memory usage.

        :param mode: (optional) determines what kind of information is returned.

                     1. "stats" returns general statistics about memory usage in the daemon.

                     2. "mallocinfo" returns an XML string describing low-level heap state (only available if compiled with glibc 2.10+).
        :type mode: str
        :return: {...} (json) if mode == "stats" | malloc if mode == "mallocinfo"

            **Result (mode "stats"):**

            .. code-block:: text

                {
                    "locked": {               (json object) Information about locked memory manager
                    "used": xxxxx,          (numeric) Number of bytes used
                    "free": xxxxx,          (numeric) Number of bytes available in current arenas
                    "total": xxxxxxx,       (numeric) Total number of bytes managed
                    "locked": xxxxxx,       (numeric) Amount of bytes that succeeded locking. If this number is smaller than total, locking pages failed at some point and key data could be swapped to disk.
                    "chunks_used": xxxxx,   (numeric) Number allocated chunks
                    "chunks_free": xxxxx,   (numeric) Number unused chunks
                    }
                }

            **Result (mode "mallocinfo"):**

            "<malloc version="1">..."

        :example:

            >>> node.control.getmemoryinfo()
        """
        return self._node._rpc.call("getmemoryinfo", mode)

    def getrpcinfo(self) -> {}:  # 02
        """
        Returns details of the RPC server.

        :return: {...} (json) -- returns rpc info

            .. code-block:: text

                {
                    "active_commands" (array) All active commands
                    [
                        {               (object) Information about an active command
                        "method"       (string)  The name of the RPC command
                        "duration"     (numeric)  The running time in microseconds
                        },...
                    ],
                    "logpath": "xxx" (string) The complete file path to the debug log
                }

        :example:

            >>> node.control.getrpcinfo()
        """
        return self._node._rpc.call("getrpcinfo")

    def help(self, command: str = None) -> str:  # 03
        """
        List all commands, or get help for a specified command.

        :param command: (optinal) The command to get help on
        :type command: str
        :return: "text" (string) The help text

        :example:

            >>> node.control.help()
            >>> node.control.help("getblockcount")
        """
        return self._node._rpc.call("help", command)

    def logging(self, include: [] = [], exclude: [] = []) -> {}:  # 04
        """
        Gets and sets the logging configuration.
        When called without an argument, returns the list of categories with status that are currently being debug logged or not.
        When called with arguments, adds or removes categories from debug logging and return the lists above.
        The arguments are evaluated in order "include", "exclude".
        If an item is both included and excluded, it will thus end up being excluded.
        The valid logging categories are: accountchange, addrman, anchoring, bench, cmpctblock, coindb, db, estimatefee, futureswap, http, leveldb, libevent, loan, mempool, mempoolrej, net, oracle, proxy, prune, rand, reindex, rpc, rpccache, selectcoins, spv, staking, tokensplit, tor, zmq
        In addition, the following are available as category names with special meanings:

        - "all",  "1" : represent all logging categories.
        - "none", "0" : even if other logging categories are specified, ignore all of them.

        :param include: (optinal) A json array of categories to add debug logging

            .. code-block:: text

                [
                    "include_category",    (string) the valid logging category
                    ...
                ]

        :type include: []
        :param exclude: (optinal) A json array of categories to remove debug logging

            .. code-block:: text

                [
                    "exclude_category",    (string) the valid logging category
                    ...
                ]

        :type exclude: []
        :return: {...} (json) -- object where keys are the logging categories, and values indicates its status

            .. code-block:: text

                {
                    "category": true|false,  (bool) if being debug logged or not. false:inactive, true:active
                    ...
                }

        :example:

            >>> node.control.logging(["all"], ["http"])
        """
        return self._node._rpc.call("logging", include, exclude)

    def stop(self) -> None:  # 05
        """
        Stop Defi server.

        :return: None

        :example:

            >>> node.control.stop()
        """
        return self._node._rpc.call("stop")

    def uptime(self) -> int:  # 06
        """
        Returns the total uptime of the server.

        :return: ttt (numeric) -- The number of seconds that the server has been running


        :example:

            >>> node.control.uptime()
        """
        return self._node._rpc.call("uptime")
