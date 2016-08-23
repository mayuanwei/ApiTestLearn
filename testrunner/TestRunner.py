import os
import re
from excelcaseparser import CaseParser
from requestlib import HTTPRequestlib
from Exception import TestCaseFailException
from jsonparser import JsonParser

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
                    result = httprequest.get(testcase['URL'], testcase['IP'])

                    if result.status_code != 200:
                        raise TestCaseFailException

                    result_data = JsonParser().parser(result.text)
                    if result_data['code'] == 1:
                        raise TestCaseFailException

                    case_pass += 1
                    '''print('第%d条用例' % order, '状态码:', result.status_code, 'pass',
                          '服务器响应:', result_data)'''
                except:
                    case_fail += 1
                    if result.status_code != 200:
                        print('第%d条用例' % order,'状态码:',result.status_code,'fail',
                          '服务器无响应')
                    else:
                        print('第%d条用例' % order,'状态码:',result.status_code,'fail',
                          '服务器响应:',result_data)

            print('通过用例%d条'%case_pass,
                  '失败用例%d条'%case_fail)



a = TestRuuner().runner('D:\\Users\\cpr223\\envs\\ApiTestLearn\\test\\')