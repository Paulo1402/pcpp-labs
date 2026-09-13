import json


class JsonParserMixin:
    def encode(self):
        return json.dumps(self._data)

    @classmethod
    def decode(cls, json_string):
        dct = json.loads(json_string)
        return cls(**dct)
