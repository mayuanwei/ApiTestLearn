from TestcaseBean import TestcaseList,Testcase
import xlrd,xlsxwriter

class CaseParser(object):
    '''def __init__(self,file):
        self.file = file'''

    def read(self,file):
        worksheet = xlrd.open_workbook(file)
        sheet = worksheet.sheet_by_index(0)

        #testcase = Testcase()
        sheet_cells = []
        for now in range(4, sheet.nrows):
            sheet_cells.append(sheet.row_values(now))

        return sheet_cells

    def write_to_testcaselist(self,file):
        testcase = Testcase()
        testcaselist = TestcaseList()

        sheet_cells = CaseParser.read(self,file)
        for sheet_cell in sheet_cells:
            testcase = {'CaseID':sheet_cell[0],
                        'ip':sheet_cell[1],
                        'actResult':sheet_cell[2],
                        'expResult':sheet_cell[3],
                        'Pass':sheet_cell[4],
                        'Desc':sheet_cell[5]
                        }

            testcaselist.append(testcase)

        return testcaselist

    def write(self,filepath,tclist):
        wb = xlsxwriter.Workbook(filepath)
        sht = wb.add_worksheet('Result1')

        sht.write(0,0,'Interface:')
        sht.write(0,1,'ip.taobao.com/service/getIpInfo.php')
        sht.write(1,0,'Method:')
        sht.write(1,1,'GET')
        name = ['CaseID','IP','actResult','expResult','Pass','Desc']
        for i in range(len(name)):
            bold = wb.add_format({'bold':True})
            sht.write(2,i,name[i],bold)

        for i in range(len(tclist)):
            if tclist[i]['Pass'] == 'N':
                bg_color = wb.add_format({'bg_color':'red'})
                sht.write(i + 3, 0, tclist[i]['CaseID'],bg_color)
                sht.write(i + 3, 1, tclist[i]['ip'],bg_color)
                sht.write(i + 3, 2, str(tclist[i]['actResult']),bg_color)
                sht.write(i + 3, 3, tclist[i]['expResult'],bg_color)
                sht.write(i + 3,4,tclist[i]['Pass'],bg_color)
                sht.write(i + 3, 5, tclist[i]['Desc'],bg_color)
            else:
                sht.write(i + 3, 0, tclist[i]['CaseID'],)
                sht.write(i + 3, 1, tclist[i]['ip'])
                sht.write(i + 3, 2, str(tclist[i]['actResult']))
                sht.write(i + 3, 3, tclist[i]['expResult'])
                sht.write(i + 3, 4, tclist[i]['Pass'])
                sht.write(i + 3, 5, tclist[i]['Desc'])

        wb.close()

if __name__=='__main__':
    '''file = 'D:\\Users\\cpr223\\envs\\ApiTestLearn\\test\\testcase_taobaoip.xlsx'
    cp = CaseParser().write_to_testcaselist(file)
    for testcase in cp:
        print(testcase)
    print('总共有%d条用例'%len(cp))'''
    file = 'C:\\Program Files\\Python35\\test\\demo.xlsx'
    tclist = [{'CaseID': '3',
               'Desc': '',
               'expResult': '',
               'ip': '219.137.148.0111',
               'actResult': 'invaild ip.',
               'Pass': 'N'},
              {'Desc': '',
               'Pass': 'Y',
               'ip': '61.183.144.26',
               'expResult': '',
               'actResult': {'county': '', 'area': '华中', 'city_id': '420100', 'county_id': '-1', 'country': '中国', 'ip': '61.183.144.26', 'region': '湖北省', 'city': '武汉市', 'isp_id': '100017', 'area_id': '400000', 'isp': '电信', 'country_id': 'CN', 'region_id': '420000'},
               'CaseID': '1'}]
    print(tclist)
    cp = CaseParser().write(file,tclist)



