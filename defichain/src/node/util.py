import json


class BuildJson:
    def __init__(self):
        self.json = {}

    def append(self, key, value):
        new = {key: value}
        if value is not None:
            self.json.update(new)

    def get(self):
        if self.json == {}:
            return None
        else:
            return self.json
