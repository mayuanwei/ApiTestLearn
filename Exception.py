
class TestCaseFailException(Exception):
    """"""

    def __init__(self):
        """Constructor for TestCaseFailException"""
        Exception.__init__(self)
    '''def __str__(self):
        return repr(self.msg)'''

#print(TestCaseFailException('aaa'))