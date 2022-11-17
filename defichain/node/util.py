import copy


class BuildJson:
    def __init__(self, json=None):
        new_json = copy.deepcopy(json)
        self.json = new_json if new_json is not None else {}

    def append(self, key, value):
        new = {key: value}
        if value is not None:
            self.json.update(new)

    def empty(self):
        if self.json == {}:
            return True
        return False

    def build(self):
        return self.json


class BuildToJson:
    """
    OUTDATED
    """
    def __init__(self, json=None):
        new_json = copy.deepcopy(json)
        self.json = BuildJson(new_json) if new_json is not None else BuildJson()

    def add(self, address, coin, amount):
        existing_json = self.json.build()
        if not self.json.empty():
            if address in existing_json:
                value = existing_json[address]
                if isinstance(value, list):
                    value.append(f'{amount}@{coin}')
                    self.json.append(address, value)
                else:
                    lst = [value, f'{amount}@{coin}']
                    self.json.append(address, lst)
            else:
                self.json.append(address, f'{amount}@{coin}')
        else:
            self.json.append(address, f'{amount}@{coin}')
        return self.json.build()

    def build(self):
        return self.json.build()


class BuildAmounts:
    """
    An easy to use class to quickly build amounts.

    :param amounts: import already existing amounts: "amount@token" or [”amount1@t1”, “amount2@t2”]
    :type amounts: str or array str

    :example:

        >>> from defichain.node import BuildAmounts
        >>>
        >>> amounts = BuildAmounts()
        >>> amounts.add("DFI", 1)
        >>> amounts.add("BTC", 2)
        >>> amounts.build()
        ['1@DFI', '2@BTC']
    """
    def __init__(self, amounts=None):

        new_amounts = copy.deepcopy(amounts)
        self.amounts = new_amounts if new_amounts is not None else ""

    def add(self, coin: str, amount: float) -> "BuildAmounts":
        """
        Add an amount to other amounts.

        :param coin: coin to use
        :type coin: str
        :param amount: amount of specified coin
        :type amount: float
        :return: "BuildAmounts"
        """
        if self.amounts == "":
            self.amounts = f"{amount}@{coin}"
        else:
            if not isinstance(self.amounts, list):
                self.amounts = [self.amounts]
            self.amounts.append(f"{amount}@{coin}")
        return self

    def build(self) -> {}:
        """
        Returns the amount

        :return: Returns the amount. If it is a single amount, it will return a string. If there are multiple amounts
            it will return a list of strings.
        """
        return self.amounts


class BuildAddressAmounts:
    """
        An easy to use class to quickly build address amounts.

        :param address_amounts: import an existing json address amount: {"address": "amounts"}
        :type address_amounts: json string

        :example:

            >>> from defichain.node import BuildAddressAmounts
            >>>
            >>> address_amounts = BuildAddressAmounts()
            >>> address_amounts.add("address1", "DFI", 1)
            >>> address_amounts.add("address2", "BTC", 2)
            >>> address_amounts.build()
            {'address1': '1@DFI', 'address2': '2@BTC'}
    """
    def __init__(self, address_amounts: {} = None):

        self.address_amounts = BuildToJson(address_amounts)

    def add(self, address: str, coin: str, amount: float) -> "BuildAddressAmounts":
        """
        Add an amount to already existing address amounts.

        :param address: defichain address
        :type address: str
        :param coin: the coin to use
        :type coin: str
        :param amount: the amount of the specified coin
        :type amount: str
        :return: "BuildAddressAmounts"
        """
        self.address_amounts.add(address, coin, amount)
        return self

    def build(self) -> {}:
        """
        Returns the address amount.

        :return: Returns the address amount
        """
        return self.address_amounts.build()
