from TestcaseBean import TestcaseList
import xlrd

class CaseParser(object):
    '''def __init__(self,file):
        self.file = file'''

    def testcase_read_by_ecxel(self,file):
        worksheet = xlrd.open_workbook(file)
        sheet = worksheet.sheet_by_index(0)

        sheet_cell = []
        for row in range(1, sheet.nrows):
            sheet_cell.append(sheet.row_values(row))

        return sheet_cell

    def write_to_testcaselist(self,file):
        testcaselist = TestcaseList()
        testcaselist = CaseParser.testcase_read_by_ecxel(self,file)
        return testcaselist

if __name__=='__main__':
    file = 'C:\\Program Files\\Python35\\test\\testcase_taobaoip.xlsx'
    cp = CaseParser()
    testcaselist = cp.write_to_testcaselist(file)
    for testcase in testcaselist:
        print(testcase)
    print('总共有%d条用例'%len(testcaselist))


