import json


class JsonSerializableMixin:
    def to_json(self):
        a = json.dumps(self.__dict__, default=lambda x: x.__dict__)
        return a