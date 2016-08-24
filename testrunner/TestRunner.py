import os
import re
from excelcaseparser import CaseParser
from requestlib import HTTPRequestlib
from Exception import TestCaseFailException
from verifylib import VerifyLib

class TestRuuner(object):
    """"""

    def __init__(self):
        """Constructor for """
        object.__init__(self)

    #找到路径表xlsx文件
    def search_xlsx(self,dirpath):
        files = os.listdir(dirpath)

        regex = '[^$~][a-zA-Z0-9_-]*\.xlsx'
        file_xlsx = []

        for file in files:
            if re.match(regex,file) != None:
                file_xlsx.append(file)

        return file_xlsx

    #获取xlsx文件路径
    def get_xlsx_path(self,dirpath):
        dirpath = 'D:\\Users\\cpr223\\envs\\ApiTestLearn\\test\\'

        file_xlsxs = TestRuuner.search_xlsx(self,dirpath)
        filepaths = []
        for file_xlsx in file_xlsxs:
            filepaths.append(dirpath+file_xlsx)

        return filepaths

    def runner(self,dirpath):
        filepaths = TestRuuner.get_xlsx_path(self,dirpath)

        for filepath in filepaths:
            caseparser = CaseParser()
            testcaselist = caseparser.write_to_testcaselist(filepath)

            case_pass = 0
            case_fail = 0
            for testcase in testcaselist:
                # 记录第几条用例
                order = testcaselist.index(testcase) + 1
                # 发送get请求
                httprequest = HTTPRequestlib()
                try:
                    result = httprequest.get('http://ip.taobao.com/service/getIpInfo.php', testcase)

                    if result.status_code != 200:
                        raise TestCaseFailException

                    #result_data = VerifyLib().json_parser(result.text)
                    result_data = result.json()
                    if result_data['code'] == 1:
                        raise TestCaseFailException

                    case_pass += 1
                    testcase['Pass'] = 'Y'
                    '''print('第%d条用例' % order, '状态码:', result.status_code, 'pass',
                          '服务器响应:', result_data)'''
                except:
                    case_fail += 1
                    testcase['Pass'] = 'N'
                    '''if result.status_code != 200:
                        print('第%d条用例' % order,'状态码:',result.status_code,'fail',
                          '服务器无响应')
                    else:
                        print('第%d条用例' % order,'状态码:',result.status_code,'fail',
                          '服务器响应:',result_data)'''

                finally:
                    testcase['actResult'] = result_data['data']
                    print(testcase)




a = TestRuuner().runner('D:\\Users\\cpr223\\envs\\ApiTestLearn\\test\\')