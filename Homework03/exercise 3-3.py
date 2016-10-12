#Exercise 3.3
import xlrd as xl
import numpy as np

workbook = xl.open_workbook('Data/classprobs.xls')
sheet = workbook.sheet_by_index(0)
col1 = sheet.col(0)
nRows = len(col1)
