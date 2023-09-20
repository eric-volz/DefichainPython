class EVM:
    def __init__(self, node):
        self._node = node

    def evmtx(self, _from: str, nonce: int, gasPrice: int, gasLimit: int, to: str, value: float, data: str = "") -> str:
        """
        Creates (and submits to local node and network) a tx to send DFI token to EVM address.

        **Inputs must be in hex format**

        :param _from: (required) From ERC55 address
        :type _from: str
        :param nonce: (required) Transaction nonce
        :type nonce: hex
        :param gasPrice: (required) Gas Price in Gwei
        :type gasPrice: hex
        :param gasLimit: (required) Gas limit
        :type gasLimit: hex
        :param to: (required) To address. Can be empty
        :type to: str
        :param value: (required) Amount to send in DFI
        :type value: hex
        :param data: (optional) Hex encoded data. Can be blank.
        :type data: hex
        :return: "hash" - (string) The hex-encoded hash of broadcasted transaction

        :example:

            >>> node.evm.evmtx("0xB553De274BFc1293DC703B013464202fC65E3FDF", 0x0, 0x09184e72a000, 0x2710, "0xB553De274BFc1293DC703B013464202fC65E3FDF", 0x1e4876e800, 0x0)
        """

        return self._node._rpc.call("evmtx", _from, nonce, gasPrice, gasLimit, to, value, data)

    def logvmmaps(self, type: int) -> {}:
        """
        Logs all block or tx indexes for debugging.

        0 - DVMToEVM Blocks

        1 - EVMToDVM Blocks

        2 - DVMToEVM TXs

        3 - EVMToDVM TXs

        :param type: (required) Type of logs
        :type type: int
        :return: json - (array) Json object with account balances if rpcresult is enabled.This is for debugging purposes only.

        :example:

            >>> node.evm.logvmmaps(0)
        """

        return self._node._rpc.call("logvmmaps", type)

    def vmmap(self, input: str, type: int):
        """
        Give the equivalent of an address, blockhash or transaction from EVM to DVM

        Map Types:

        0 - Auto

        1 - Block Number: DFI -> EVM

        2 - Block Number: EVM -> DFI

        3 - Block Hash: DFI -> EVM

        4 - Block Hash: EVM -> DFI

        5 - Tx Hash: DFI -> EVM

        6 - Tx Hash: EVM -> DFI

        :param input: (required) DVM address, EVM blockhash, EVM transactio
        :type input: str
        :param type: (required) Map types
        :type type: int
        :return: str - The hex-encoded string for address, block or transaction or (number) block number

        :example:

            >>> node.evm.vmmap("1600000", 0)
        """

        return self._node._rpc.call("vmmap", input, type)
