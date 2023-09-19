

class Converter:

    """
    **Methods to convert different datatypes**
    """

    # Integer - Bytes
    @staticmethod
    def int_to_bytes(i: int, length: int) -> bytes:
        """
        Converts int to bytes

        :param i: (required) number
        :type i: int
        :param length: (required) length of the bytes
        :type length: int
        :return: bytes
        """
        return i.to_bytes(length, byteorder="little")

    @staticmethod
    def bytes_to_int(b: bytes) -> int:
        """
        Converts bytes to int

        :param b: (required) binary data
        :type b: bytes
        :return: int
        """
        return int.from_bytes(b, byteorder="little")

    # Hex - Bytes
    @staticmethod
    def hex_to_bytes(h: str) -> bytes:
        """
        Converts hex to bytes

        :param h: (required) hex string
        :type h: str
        :return: bytes
        """
        return bytes.fromhex(h)

    @staticmethod
    def bytes_to_hex(b: bytes) -> str:
        """
        Converts bytes to hex

        :param b: (required) binary data
        :type b: bytes
        :return: str - hex data
        """
        return b.hex()

    # Hex - Integer
    @staticmethod
    def hex_to_int(h: str) -> int:
        """
        Converts hex to int

        :param h: (required) hex string data
        :type h: str
        :return: int
        """
        return Converter.bytes_to_int(Converter.hex_to_bytes(h))

    @staticmethod
    def int_to_hex(i: int or str, length: int) -> str:
        """
        Converts int to hex

        :param i: (required) number
        :type i: int | str
        :param length: (required) length of the hex data
        :type length: int
        :return: str - hex string data
        """
        return i.to_bytes(length=length, byteorder="little").hex()

    # String - Hex
    @staticmethod
    def str_to_hex(s: str) -> str:
        """
        Converts str to hex

        :param s: (required) string data
        :type s: str
        :return: str - hex string data
        """
        return s.encode("utf-8").hex()

    @staticmethod
    def hex_to_str(h: str) -> str:
        """
        Converts hex to str

        :param h: (required) hex string data
        :type h: str
        :return: str - string data
        """
        return bytes.fromhex(h).decode("ascii")

    # Float - Integer
    @staticmethod
    def int_to_float(i: int) -> float:
        """
        Converts a given integer number into a float with eight decimal places

        1111 -> 0.00001111
        122222222 -> 1.22222222

        :param i: (required) integer number
        :type i: float
        :return: int - returns the float number shifted by eight decimal places
        """
        return round(float(i) / 100000000.0, 8)

    @staticmethod
    def float_to_int(f: float) -> int:
        """
        Converts a given float number with eight decimal places into an integer

        0.00001111 -> 1111
        1.22222222 -> 122222222

        :param f: (required) float number
        :type f: float
        :return: int - returns the integer number shifted by eight decimal places
        """
        return int(round(f * 100000000))

    @staticmethod
    def amount_float_to_int(amount: str) -> str:
        """
        Converts an amount value from float to int

        :param amount: (required) Amount
        :type amount: :ref:`Transactions Amounts`
        :return: :ref:`Transactions Amounts` - with int value
        """
        return f'{Converter.float_to_int(float(amount.split("@")[0]))}@{amount.split("@")[1]}'

    @staticmethod
    def addressAmount_float_to_int(addressAmount: {}) -> {}:
        """
        Converts all values in an address amount from float to int

        :param addressAmount: (required) AddressAmount
        :type addressAmount: :ref:`Transactions AddressAmount`
        :return: :ref:`Transactions AddressAmount` - with int values
        """
        from . import BuildAddressAmounts
        newAddressAmount = BuildAddressAmounts()
        for address in addressAmount:
            if isinstance(addressAmount[address], list):
                for amount in addressAmount[address]:
                    value, token = amount.split('@')
                    value = Converter.float_to_int(float(value))
                    newAddressAmount.add(address, token, value)
            else:
                value, token = addressAmount[address].split('@')
                value = Converter.float_to_int(float(value))
                newAddressAmount.add(address, token, value)
        return newAddressAmount.build()
