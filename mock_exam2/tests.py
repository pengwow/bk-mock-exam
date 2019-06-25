# coding=utf-8
import xlrd
fff = open('e:\\Temp\\checklist.xls','rb')

data = xlrd.open_workbook(file_contents=fff.read())
fff.close()
table = data.sheets()[0]
nrows = table.nrows
for i in range(1, nrows):
    print(table.row_values(i))
