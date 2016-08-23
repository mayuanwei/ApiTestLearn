import json

class JsonParser(object):
    """"""

    def __init__(self):
        """Constructor for JsonParser"""
        object.__init__(self)

    def parser(self,json_data):
        dict_data = json.loads(json_data)
        return dict_data
