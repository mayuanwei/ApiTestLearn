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
        self.l = []
    def tearDown(self):
        #print(self.errcount)
        pass

    '''def test_p(self):
        print('test_p')'''

    @data((2,3),(1,4))
    @unpack
    def test_mul(self,x,y):
        res = mul(x,y)
        try:
            #self.assertEqual(res,3)
            self.assertIn('a1','abc')
        except:
            #p(self.errcount)
            self.errcount.append('a')
            print(self.errcount,'test fail')

def runner():
    suite = unittest.TestLoader().loadTestsFromTestCase(Funcase)
    '''suite = unittest.TestSuite()
    suite.addTest(Funcase('test_mul'))'''
    #unittest.TextTestRunner.run(suite)
    return suite

def count():
    print(123)

if __name__=='__main__':
    unittest.main(defaultTest='runner')
    #print(Funcase.errcount)
    #unittest.main()