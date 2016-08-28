import xlrd

wb = xlrd.open_workbook(path)
sht = wb.sheet_by_index(0)
sht.cell_