import xlrd
import os
import sys
from configuration import filepath

class Excel():
    def __init__(self,filepath):
        if os.path.exists(filepath) == False:
            print('文件不存在！')
            sys.exit()
        self.wb = xlrd.open_workbook(filepath)
        self.sht = self.wb.sheet_by_index(1)
        self.url = self.sht.row_values(0)
        self.row = self.sht.row_values(2)

    def get_data(self):
        datalist = []
        data = {}
        for row in range(3,self.sht.nrows):
            data = {self.url[0]:self.url[1],
                    self.row[0]:self.sht.cell_value(row,0),
                    self.row[1]:self.sht.cell_value(row,1),
                    self.row[2]:self.sht.cell_value(row,2)}
            '''data[self.url[0]] = self.url[1]
            data[self.row[1]] = self.sht.cell_value(row,1)
            data[self.row[2]] = self.sht.cell_value(row,2)'''
            datalist.append(data)
        return datalist

'''e = Excel(filepath+'TestCase.xlsx')
e.get_data()'''

