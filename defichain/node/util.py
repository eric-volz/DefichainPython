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
