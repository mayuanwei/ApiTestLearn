#继承与dict类

class Testcase(dict):
    """"""
    def __init__(self,cfg={}):
        """Constructor for testcase"""
        dict.__init__(self,cfg)
        #self.cfg = cfg

    '''def __setitem__(self, key, value):
        self.cfg[key] = value'''

    def __getitem__(self, item):
        return dict.__getitem__(self,item)
        #return self.cfg[item]