class Network:
    def __init__(self, node):
        self._node = node

    def addnode(self, node: str, command: str) -> None:  # 01
        """
        Attempts to add or remove a node from the addnode list.
        Or try a connection to a node once.
        Nodes added using addnode (or -connect) are protected from DoS disconnection and are not required to be
        full nodes/support SegWit as other outbound peers are (though such peers will not be synced from).

        :param node: (required) The node (see getpeerinfo for nodes)
        :type node: str
        :param command: (required) 'add' to add a node to the list,
            'remove' to remove a node from the list,
            'onetry' to try a connection to the node once
        :type command: str
        :return: None

        :example:

            >>> node.network.addnode("192.168.0.6:8555", "onetry")
        """
        return self._node._rpc.call("addnode", node, command)

    def clearbanned(self) -> None:  # 02
        """
        Clear all banned IPs

        :return: None

        :example:

            >>> node.network.clearbanned()
        """
        return self._node._rpc.call("clearbanned")

    def disconnectnode(self, address: str = "", nodeid: int = None) -> None:  # 03
        """
        Immediately disconnects from the specified peer node.

        Strictly one out of 'address' and 'nodeid' can be provided to identify the node.

        To disconnect by nodeid, either set 'address' to the empty string, or call using the named 'nodeid' argument only.

        :param address: (optional) The IP address/port of the node
        :type address: str
        :param nodeid: (optional) The node ID (see getpeerinfo for node IDs)
        :type nodeid: int
        :return: None

        :example:

            >>> node.network.disconnectnode("192.168.0.6:8555")
        """
        return self._node._rpc.call("disconnectnode", address, nodeid)

    def getaddednodeinfo(self, node: str = None) -> [{}]:  # 04
        """
        Returns information about the given added node, or all added nodes
        (note that onetry addnodes are not listed here)

        :param node: (optional) If provided, return information about this specific node, otherwise all nodes are returned
        :type node: str
        :return: [{...}] (json array) -- returns info about an added node

            .. code-block:: text

                [
                    {
                        "addednode" : "192.168.0.201",     (string) The node IP address or name (as provided to addnode)
                        "connected" : true|false,          (boolean) If connected
                        "addresses" : [                    (list of objects) Only when connected = true
                            {
                            "address" : "192.168.0.201:8555",  (string) The DeFi Blockchain server IP and port we're connected to
                            "connected" : "outbound"           (string) connection, inbound or outbound
                            }
                        ]
                    }
                    ,...
                ]

        :example:

            >>> node.network.getaddednodeinfo()
        """
        return self._node._rpc.call("getaddednodeinfo", node)

    def getconnectioncount(self) -> int:  # 05
        """
        Returns the number of connections to other nodes

        :return: n (int) -- The connection count

        :example:

            >>> node.network.getconnectioncount()
        """
        return self._node._rpc.call("getconnectioncount")

    def getnettotals(self) -> {}:  # 06
        """
        Returns information about network traffic, including bytes in, bytes out,
        and current time.

        :return: {...} (json) -- returns information about network traffic

            .. code-block:: text

                {
                    "totalbytesrecv": n,   (numeric) Total bytes received
                    "totalbytessent": n,   (numeric) Total bytes sent
                    "timemillis": t,       (numeric) Current UNIX time in milliseconds
                    "uploadtarget":
                    {
                        "timeframe": n,                         (numeric) Length of the measuring timeframe in seconds
                        "target": n,                            (numeric) Target in bytes
                        "target_reached": true|false,           (boolean) True if target is reached
                        "serve_historical_blocks": true|false,  (boolean) True if serving historical blocks
                        "bytes_left_in_cycle": t,               (numeric) Bytes left in current time cycle
                        "time_left_in_cycle": t                 (numeric) Seconds left in current time cycle
                    }
                }

        :example:

            >>> node.network.getnettotals()
        """
        return self._node._rpc.call("getnettotals")

    def getnetworkinfo(self) -> {}:  # 07
        """
        Returns an object containing various state info regarding P2P networking

        :return: {...} (json) -- returns network info

            .. code-block:: text

                {
                    "version": xxxxx,                      (numeric) the server version
                    "subversion": "/Satoshi:x.x.x/",       (string) the server subversion string
                    "protocolversion": xxxxx,              (numeric) the protocol version
                    "localservices": "xxxxxxxxxxxxxxxx",   (string) the services we offer to the network
                    "localrelay": true|false,              (bool) true if transaction relay is requested from peers
                    "timeoffset": xxxxx,                   (numeric) the time offset
                    "connections": xxxxx,                  (numeric) the number of connections
                    "networkactive": true|false,           (bool) whether p2p networking is enabled
                    "networks": [                          (array) information per network
                        {
                            "name": "xxx",                 (string) network (ipv4, ipv6 or onion)
                            "limited": true|false,         (boolean) is the network limited using -onlynet?
                            "reachable": true|false,       (boolean) is the network reachable?
                            "proxy": "host:port"           (string) the proxy that is used for this network, or empty if none
                            "proxy_randomize_credentials": true|false,  (string) Whether randomized credentials are used
                        }
                        ,...
                    ],
                    "relayfee": x.xxxxxxxx,                (numeric) minimum relay fee for transactions in DFI/kB
                    "incrementalfee": x.xxxxxxxx,          (numeric) minimum fee increment for mempool limiting or BIP 125 replacement in DFI/kB
                    "localaddresses": [                    (array) list of local addresses
                        {
                            "address": "xxxx",             (string) network address
                            "port": xxx,                   (numeric) network port
                            "score": xxx                   (numeric) relative score
                        }
                        ,...
                    ]
                    "warnings": "..."                      (string) any network and blockchain warnings
                }

        :example:

            >>> node.network.getnetworkinfo()
        """
        return self._node._rpc.call("getnetworkinfo")

    def getnodeaddresses(self, count: int = 1) -> [{}]:  # 08
        """
        Return known addresses which can potentially be used to find new nodes in the network

        :param count: (optional) Timestamp in seconds since epoch (Jan 1 1970 GMT) keeping track of when the node was last seen
        :type count: int
        :return: [{...}] (json array) -- returns known addresses

            .. code-block:: text

                [
                    {
                    "time": ttt,                (numeric) Timestamp in seconds since epoch (Jan 1 1970 GMT) keeping track of when the node was last seen
                    "services": n,              (numeric) The services offered
                    "address": "host",          (string) The address of the node
                    "port": n                   (numeric) The port of the node
                    }
                    ,....
                ]

        :example:

            >>> node.network.getnodeaddresses()
        """
        return self._node._rpc.call("getnodeaddresses", count)

    def getpeerinfo(self) -> [{}]:  # 09
        """
        Returns data about each connected network node as a json array of objects

        :return: {...} (json) -- returns data about peers

            .. code-block:: text

                [
                    {
                        "id": n,                   (numeric) Peer index
                        "addr":"host:port",        (string) The IP address and port of the peer
                        "addrbind":"ip:port",      (string) Bind address of the connection to the peer
                        "addrlocal":"ip:port",     (string) Local address as reported by the peer
                        "services":"xxxxxxxxxxxxxxxx",   (string) The services offered
                        "relaytxes":true|false,    (boolean) Whether peer has asked us to relay transactions to it
                        "lastsend": ttt,           (numeric) The time in seconds since epoch (Jan 1 1970 GMT) of the last send
                        "lastrecv": ttt,           (numeric) The time in seconds since epoch (Jan 1 1970 GMT) of the last receive
                        "bytessent": n,            (numeric) The total bytes sent
                        "bytesrecv": n,            (numeric) The total bytes received
                        "conntime": ttt,           (numeric) The connection time in seconds since epoch (Jan 1 1970 GMT)
                        "timeoffset": ttt,         (numeric) The time offset in seconds
                        "pingtime": n,             (numeric) ping time (if available)
                        "minping": n,              (numeric) minimum observed ping time (if any at all)
                        "pingwait": n,             (numeric) ping wait (if non-zero)
                        "version": v,              (numeric) The peer version, such as 70001
                        "subver": "/Satoshi:0.8.5/",  (string) The string version
                        "inbound": true|false,     (boolean) Inbound (true) or Outbound (false)
                        "addnode": true|false,     (boolean) Whether connection was due to addnode/-connect or if it was an automatic/inbound connection
                        "startingheight": n,       (numeric) The starting height (block) of the peer
                        "banscore": n,             (numeric) The ban score
                        "synced_headers": n,       (numeric) The last header we have in common with this peer
                        "synced_blocks": n,        (numeric) The last block we have in common with this peer
                        "inflight": [
                            n,                      (numeric) The heights of blocks we're currently asking from this peer
                            ...
                        ],
                        "whitelisted": true|false, (boolean) Whether the peer is whitelisted
                        "minfeefilter": n,         (numeric) The minimum fee rate for transactions this peer accepts
                        "bytessent_per_msg": {
                            "msg": n,              (numeric) The total bytes sent aggregated by message type
                               When a message type is not listed in this json object, the bytes sent are 0.
                               Only known message types can appear as keys in the object.
                            ...
                        },
                        "bytesrecv_per_msg": {
                            "msg": n,               (numeric) The total bytes received aggregated by message type
                               When a message type is not listed in this json object, the bytes received are 0.
                               Only known message types can appear as keys in the object and all bytes received of unknown message types are listed under '*other*'.
                            ...
                        }
                    }
                    ,...
                ]

        :example:

            >>> node.network.getpeerinfo()
        """
        return self._node._rpc.call("getpeerinfo")

    def getversioninfo(self) -> {}:  # 10
        """
        Returns an object containing various version info about the node

        :return: {...} (json) -- returns information about the node

            .. code-block:: text

                {
                    "name": DeFiChain                     (string) Node name
                    "version": "xxxxx",                   (string) Node version string
                    "numericVersion": xxxxx,              (number) Node numeric version
                    "fullVersion": "DefiChain:x.x.x",     (string) Full node version string including name and version
                    "userAgent": "/DefiChain:x.x.x/",     (string) P2P user agent string (subversion string conforming to BIP-14)
                    "protoVersion": "xxxxx",              (number) Operating protocol version
                    "protoVersionMin": "xxxxx",           (number) Minimum protocol that's supported by the node
                    "rpcVersion": "xxxxx",                (string) RPC version
                    "rpcVersionMin": "xxxxx",             (string) Minimum RPC version supported
                    "spv": {
                        "btc": {
                            "userAgent": "xxxxx",             (string) BTC SPV agent string
                            "protoVersion": "xxxxx",          (number) BTC SPV protocol version
                            "protoVersionMin": "xxxxx",       (number) Minimum BTC SPV protocol that's supported by the node
                        }
                    }
                }

        :example:

            >>> node.network.getversioninfo()
        """
        return self._node._rpc.call("getversioninfo")

    def listbanned(self) -> [{}]:  # 11
        """
        List all banned IPs/Subnets

        :return: [{...}] (json array) -- List of band nodes

        :example:

            >>> node.network.listbanned()
        """
        return self._node._rpc.call("listbanned")

    def ping(self) -> None:  # 12
        """
        Requests that a ping be sent to all other nodes, to measure ping time.

        Results provided in getpeerinfo, pingtime and pingwait fields are decimal seconds.

        Ping command is handled in queue with all other commands, so it measures processing backlog, not just network ping.

        :return: None

        :example:

            >>> node.network.ping()
        """
        return self._node._rpc.call("ping")

    def setban(self, subnet: str, command: str, bantime: int = 0, absolute: bool = False) -> None:  # 13
        """
        Attempts to add or remove an IP/Subnet from the banned list

        :param subnet: (required) The IP/Subnet (see getpeerinfo for nodes IP) with an optional netmask (default is /32 = single IP)
        :type subnet: str
        :param command: (required) 'add' to add an IP/Subnet to the list, 'remove' to remove an IP/Subnet from the list
        :type command: str
        :param bantime: (optional) time in seconds how long (or until when if [absolute] is set) the IP is banned
            (0 or empty means using the default time of 24h which can also be overwritten by the -bantime startup argument)
        :type bantime: int
        :param absolute: (optional) If set, the bantime must be an absolute timestamp in seconds since epoch
            (Jan 1 1970 GMT)
        :type absolute: bool
        :return: None

        :example:

            >>> node.network.setban("192.168.0.6", "add", 86400)
        """
        return self._node._rpc.call("setban", subnet, command, bantime, absolute)

    def setnetworkactive(self, state: bool) -> None:  # 14
        """
        Disable/enable all p2p network activity

        :param state: (required) true to enable networking, false to disable
        :type state: bool
        :return: None

        :example:

            >>> node.network.setnetworkactive(True)
        """
        return self._node._rpc.call("setnetworkactive", state)
