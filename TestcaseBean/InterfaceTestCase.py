import unittest
import requests
import json
from ddt import ddt,data,unpack
from DataDriver.ExcelDriver import Excel
from configuration import filepath
from TestResultCount.ResultCount import ResultCount
from Email.Email import Email
from TestResultCount.HTMLReport import HTMLReport

excel = Excel(filepath+'TestCase.xlsx')

@ddt
class InterfaceTestCase(unittest.TestCase):
    corcases = []
    errcases = []

    def setUp(self):
        pass
    def tearDown(self):
        pass

    @data(*excel.get_data())
    def test_getipinfo(self,data):
        request_data = json.loads(data['Request Data'])
        result = requests.get(data['URL'],request_data)
        self.assertEqual(result.status_code, 200)
        self.assertIn(data['Check Point'], result.text)
        '''try:
            self.assertEqual(result.status_code,200)
            self.assertIn(data['Check Point'],result.text)
        except:
            self.errcases.append((data,result.text,'fail'))
        else:
            self.corcases.append((data,result.json(),'pass'))'''

if __name__ == '__main__':
    suite = unittest.makeSuite(InterfaceTestCase)#.main(exit=False)
    report = HTMLReport('C:\\Users\\cpr223\\PycharmProjects\\ApiTestLearn\\TestResult\\Result.html',suite)
    text = report.report_parser()

    '''rescount = ResultCount(InterfaceTestCase.errcases,InterfaceTestCase.corcases)
    failcount,text = rescount.failcount()'''

    email = Email(text,'mayw@corp.hxqc.com')
    email.sendmail()



