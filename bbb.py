class testcase(dict):
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



t = testcase()
t['a'] = 1
print(t['a'])
print(t)

a = dict()
a['b'] = 1
print(a['b'])
print(a)