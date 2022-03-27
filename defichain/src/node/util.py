import json


class BuildJson:
    def __init__(self):
        self.json = {}

    def append(self, key, value):
        new = {key: value}
        if value is not None:
            self.json.update(new)

    def build(self):
        if self.json == {}:
            return None
        else:
            return self.json


class BuildToJson:
    def __init__(self):
        self.json = BuildJson()

    def add(self, address, coin, amount):
        existing_json = self.json.build()
        if existing_json is not None:
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

    def build(self):
        return self.json.build()
