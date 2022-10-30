class Util:
    def __init__(self, node):
        self._node = node

    def createmultisig(self, nrequired: int, keys: [str], address_type: str = "legacy") -> {}:  # 01
        """
        Creates a multi-signature address with n signature of m keys required.
        It returns a json object with the address and redeemScript.


        :param nrequired: (required) The number of required signatures out of the n keys
        :type nrequired: int
        :param keys: (required) A json array of hex-encoded public keys
        :type keys: json array
        :param address_type: (optional) The address type to use. Options are "legacy", "p2sh-segwit", and "bech32"
        :type address_type: str
        :return: {...} (json) -- returns a json object with the address and redeemScript

            .. code-block:: text

                {
                    "address":"multisigaddress",  (string) The value of the new multisig address.
                    "redeemScript":"script"       (string) The string value of the hex-encoded redemption script.
                }

        :example:

            >>> node.util.createmultisig(2, ["03789ed0bb717d88f7d321a368d905e7430207ebbd82bd342cf11ae157a7ace5fd", "03dbc6764b8884a92e871274b87583e6d5c2a58819473e17e107ef3f6aa5a61626"])
        """
        return self._node._rpc.call("createmultisig", nrequired, keys, address_type)

    def deriveaddresses(self, descriptor: str, range: int or [] = None) -> [str]:  # 02
        """
        Derives one or more addresses corresponding to an output descriptor.

        Examples of output descriptors are:

            pkh(<pubkey>)                        P2PKH outputs for the given pubkey

            wpkh(<pubkey>)                       Native segwit P2PKH outputs for the given pubkey

            sh(multi(<n>,<pubkey>,<pubkey>,...)) P2SH-multisig outputs for the given threshold and pubkeys

            raw(<hex script>)                    Outputs whose scriptPubKey equals the specified hex scripts

        In the above, <pubkey> either refers to a fixed public key in hexadecimal notation, or to an xpub/xprv
        optionally followed by one or more path elements separated by "/", where "h" represents a hardened child key.

        For more information on output descriptors, see the documentation in the doc/descriptors.md file.

        :param descriptor: (required) The descriptor
        :type descriptor: str
        :param range: (optional) If a ranged descriptor is used, this specifies the end or the range (in [begin,end] notation) to derive
        :type range: int or array
        :return: [...] (array) -- the derived addresses

        :example:

            >>> node.util.deriveaddresses("wpkh([d34db33f/84h/0h/0h]xpub6DJ2dNUysrn5Vt36jH2KLBT2i1auw1tTSSomg8PhqNiUtx8QX2SvC9nrHu81fT41fvDUnhMjEzQgXnQjKEu3oaqMSzhSrHMxyyoEAmUHQbY/0/*)#cjjspncu", [0,2])
        """
        return self._node._rpc.call("deriveaddresses", descriptor, range)

    def estimatesmartfee(self, conf_target: int, estimate_mode: str = "CONSERVATIVE") -> {}:  # 03
        """
        Estimates the approximate fee per kilobyte needed for a transaction to begin
        confirmation within conf_target blocks if possible and return the number of blocks
        for which the estimate is valid. Uses virtual transaction size as defined
        in BIP 141 (witness data is discounted).


        :param conf_target: (required) Confirmation target in blocks (1 - 1008)
        :type conf_target: int
        :param estimate_mode: (optional) The fee estimate mode.
             Whether to return a more conservative estimate which also satisfies
             a longer history. A conservative estimate potentially returns a
             higher feerate and is more likely to be sufficient for the desired
             target, but is not as responsive to short term drops in the
             prevailing fee market.

             Must be one of:

             "UNSET"

             "ECONOMICAL"

             "CONSERVATIVE"

        :type estimate_mode: str
        :return: {...} (json) -- resturns a estimation of a fee

            .. code-block:: text

                {
                  "feerate" : x.x,     (numeric, optional) estimate fee rate in DFI/kB
                  "errors": [ str... ] (json array of strings, optional) Errors encountered during processing
                  "blocks" : n         (numeric) block number where estimate was found
                }

            The request target will be clamped between 2 and the highest target
            fee estimation is able to return based on how long it has been running.

            An error is returned if not enough transactions and blocks
            have been observed to make an estimate for any number of blocks.

        :example:

            >>> node.util.estimatesmartfee(6)
        """
        return self._node._rpc.call("estimatesmartfee", conf_target, estimate_mode)

    def getdescriptorinfo(self, descriptor: str) -> {}:  # 04
        """
        Analyses a descriptor

        :param descriptor: (required) The descriptor
        :type descriptor: str
        :return: {...} (json) -- returns information about decriptor

            .. code-block:: text

                {
                    "descriptor" : "desc",         (string) The descriptor in canonical form, without private keys
                    "checksum" : "chksum",         (string) The checksum for the input descriptor
                    "isrange" : true|false,        (boolean) Whether the descriptor is ranged
                    "issolvable" : true|false,     (boolean) Whether the descriptor is solvable
                    "hasprivatekeys" : true|false, (boolean) Whether the input descriptor contained at least one private key
                }

        :example:

            >>> node.util.getdescriptorinfo("wpkh([d34db33f/84h/0h/0h]0279be667ef9dcbbac55a06295Ce870b07029Bfcdb2dce28d959f2815b16f81798)")
        """
        return self._node._rpc.call("getdescriptorinfo", descriptor)

    def signmessagewithprivkey(self, privkey: str, message: str) -> str:  # 05
        """
        Sign a message with the private key of an address

        :param privkey: (required) The private key to sign the message with
        :type privkey: str
        :param message: (required) The message to create a signature of
        :type message: str
        :return: "signature" (string) -- The signature of the message encoded in base 64

        :example:

            >>> node.util.signmessagewithprivkey("privkey", "my message")
        """
        return self._node._rpc.call("signmessagewithprivkey", privkey, message)

    def validateaddress(self, address: str) -> {}:  # 06
        """
        Return information about the given defi address

        :param address: (required) The defi address to validate
        :type address: str
        :return: {...} (json) -- Return information about the given defi address

            .. code-block:: text

                {
                  "isvalid" : true|false,       (boolean) If the address is valid or not. If not, this is the only property returned.
                  "address" : "address",        (string) The defi address validated
                  "scriptPubKey" : "hex",       (string) The hex-encoded scriptPubKey generated by the address
                  "isscript" : true|false,      (boolean) If the key is a script
                  "iswitness" : true|false,     (boolean) If the address is a witness address
                  "witness_version" : version   (numeric, optional) The version number of the witness program
                  "witness_program" : "hex"     (string, optional) The hex value of the witness program
                }


        :example:

            >>> node.util.validateaddress("df1qduwqfyhz0n0duvmudlhmyx2uzk4u2xqmn627zr")
        """
        return self._node._rpc.call("validateaddress", address)

    def verifymessage(self, address: str, signature: str, message: str) -> bool:  # 07
        """
        Verify a signed message

        :param address: (required) The defi address to use for the signature
        :type address: str
        :param signature: (required) The signature provided by the signer in base 64 encoding (see signmessage)
        :type signature: str
        :param message: (required) The message that was signed
        :type message: str
        :return: bool -- If the signature is verified or not

        :example:

            >>> node.util.verifymessage("df1qduwqfyhz0n0duvmudlhmyx2uzk4u2xqmn627zr", "signature", "my message")
        """
        return self._node._rpc.call("verifymessage", address, signature, message)
