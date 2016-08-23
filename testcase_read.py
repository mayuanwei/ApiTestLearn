import xlrd

def testcase_read_by_ecxel(testcasefile):
    worksheet = xlrd.open_workbook(testcasefile)
    sheet = worksheet.sheet_by_index(0)

    sheet_row = sheet.row_values(1)
    sheet_col = sheet.col_values(1)
    #print(sheet_row)
    #print(sheet_col)

    sheet_cell = []
    for row in range(1, sheet.nrows):
        sheet_cell.append(sheet.row_values(row))

    return sheet_cell


def write_to_testcase(testcasefile):
    testcase = {'URL':None,
                'method':None,
                'request':None,
                'response':None}
    testcaselist = []

    testcase_data = testcase_read_by_ecxel(testcasefile)
    for data in testcase_data:
        testcase={'URL':data[0],
                 'method':data[1],
                 'request':data[2],
                 'response':None}
        testcaselist.append(testcase)

    return testcaselist

if __name__ == '__main__':
    file = 'C:\\Program Files\\Python35\\test\\testcase_taobaoip.xlsx'
    for data in testcase_read_by_ecxel(file):
        print(data)

    for testcase in write_to_testcase(file):
        print(testcase)
