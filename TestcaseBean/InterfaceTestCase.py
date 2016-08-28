import unittest
import requests
import json
from ddt import ddt,data,unpack
from DataDriver.ExcelDriver import Excel
from configuration import filepath

excel = Excel(filepath+'TestCase.xlsx')

@ddt
class InterfaceTestCase(unittest.TestCase):
    corcase = []
    errcase = []

    def setUp(self):
        pass
    def tearDown(self):
        pass

    @data(*excel.get_data())
    def test_getipinfo(self,data):
        request_data = json.loads(data['Request Data'])
        result = requests.get(data['URL'],request_data)
        try:
            self.assertEqual(result.status_code,200)
            self.assertIn(data['Check Point'],result.text)
        except:
            self.errcase.append((data,'fail'))
        else:
            self.corcase.append((data,'pass'))

if __name__ == '__main__':
    unittest.main(exit=False)
    print(InterfaceTestCase.corcase,'\n',
          InterfaceTestCase.errcase)
