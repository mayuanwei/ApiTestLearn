import unittest
from ddt import ddt,data,unpack

def mul(x,y):
    return x*y

def p(v):
    print(v)

@ddt
class Funcase(unittest.TestCase):
    errcount = []
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_p(self):
        print('test_p')

    @data((2,3),(1,4))
    @unpack
    def test_mul(self,x,y):
        res = mul(x,y)
        try:
            self.assertEqual(res,3)
        except:
            #p(self.errcount)
            print('test fail')

def runner():
    suite = unittest.TestLoader().loadTestsFromTestCase(Funcase)
    '''suite = unittest.TestSuite()
    suite.addTest(Funcase('test_mul'))'''
    #unittest.TextTestRunner.run(suite)
    return suite

if __name__=='__main__':
    unittest.main(defaultTest='runner')
    #unittest.main()