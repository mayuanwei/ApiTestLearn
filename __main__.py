from excelcaseparser import CaseParser
from requestlib import HTTPRequestlib
from Exception import TestCaseFailException
from jsonparser import JsonParser

if __name__=='__main__':
    file = 'C:\\Program Files\\Python35\\test\\testcase_taobaoip.xlsx'

    #解析excel用例
    caseparser = CaseParser()
    testcaselist = caseparser.write_to_testcaselist(file)


    #循环读取测试用例
    for testcase in testcaselist:
        #记录第几条用例
        order = testcaselist.index(testcase)+1
        #发送get请求
        httprequest = HTTPRequestlib()
        try:
            result = httprequest.get(testcase['URL'],testcase['IP'])

            if result.status_code != 200:
                raise TestCaseFailException

            result_data = JsonParser().parser(result.text)
            if result_data['code'] == 1:
                raise TestCaseFailException

            print('第%d条用例' % order, '状态码:', result.status_code,'pass')
        except:
            print('第%d条用例'%order,'状态码:',result.status_code,'fail')