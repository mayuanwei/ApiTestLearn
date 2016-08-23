from TestcaseBean import TestcaseList,Testcase
import xlrd

class CaseParser(object):
    '''def __init__(self,file):
        self.file = file'''

    def testcase_read_by_ecxel(self,file):
        worksheet = xlrd.open_workbook(file)
        sheet = worksheet.sheet_by_index(0)

        #testcase = Testcase()
        sheet_cells = []
        for now in range(1, sheet.nrows):
            sheet_cells.append(sheet.row_values(now))

        return sheet_cells

    def write_to_testcaselist(self,file):
        testcase = Testcase()
        testcaselist = TestcaseList()

        sheet_cells = CaseParser.testcase_read_by_ecxel(self,file)
        for sheet_cell in sheet_cells:
            testcase = {'URL':sheet_cell[0],
                        'method':sheet_cell[1],
                        'IP':sheet_cell[2],
                        'response':sheet_cell[3]
                        }

            testcaselist.append(testcase)

        return testcaselist

'''if __name__=='__main__':
    file = 'C:\\Program Files\\Python35\\test\\testcase_taobaoip.xlsx'
    cp = CaseParser().write_to_testcaselist(file)
    for testcase in cp:
        print(testcase)
    print('总共有%d条用例'%len(cp))'''


