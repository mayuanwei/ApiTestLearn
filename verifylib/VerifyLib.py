import json

class VerifyLib(object):
    """"""

    def __init__(self):
        """Constructor for JsonParser"""
        object.__init__(self)

    def json_parser(self,json_data):
        dict_data = json.loads(json_data)
        return dict_data


