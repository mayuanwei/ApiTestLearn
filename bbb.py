import xlrd,xlwt
from xlutils.copy import copy

def write(row,col,str):
    rb = xlrd.open_workbook(r'C:\Program Files\Python35\test\demo.xls',formatting_info=True)
    sht = rb.sheet_by_index(0)
    wb = copy(sht)
    #ws = wb.sheet_by_index(0)
    wb.write(row,col,str)
    sht.save(r'C:\Program Files\Python35\test\demo.xls')

write(1,1,'myw')