class Zmq:
    def __init__(self, node):
        self._node = node

    def getzmqnotifications(self) -> {}:
        """
        Returns information about the active ZeroMQ notifications

        :return: [{...}] (json array) -- returns information about the active ZeroMQ notifications

            .. code-block:: text

                [
                    {                        (json object)
                        "type": "pubhashtx", (string) Type of notification
                        "address": "...",    (string) Address of the publisher
                        "hwm": n             (numeric) Outbound message high water mark
                    },
                    ...
                ]

        :example:

            >>> node.control.getzmqnotifications()
        """
        return self._node._rpc.call("getzmqnotifications")
