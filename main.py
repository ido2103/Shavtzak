from audioop import avg
import xlrd
from classes import *
from funcs import *

wbr = xlrd.open_workbook("D:\VisualStudioCodeProjects\Shavtzak\shavtzak.xls")
sheets = wbr.sheets()[0]
list_of_soldiers = []
index = 1
"""
TODO:
need to update all of the fucntions to recieve the new dict instead of the old list.
"""
for i in range(sheets.nrows):
    soldier_value = wbr.sheet_by_index(0).row_values(i)
    list_of_soldiers.append(soldier_value)

dict = listToDict(list_of_soldiers)
print(dict)


"""
The code works in 6 cycles, updating the rest hours & current mission of each soldier on duty. This will be done by calling in a specific function several times.
The aim is to make sure the soldiers don't do more than 4/8 or 8/8. Doing 4/8 reduces 3 resting points (1 for the 4 hours of guarding and 2 for the 8 hours of rest),
while 'siur' and 'hamal' give 4 (same logic). The program will attempt to have everyone's average the same number so everything is equal. The focus is not to make a complete
'shavtzak', but to aid to the sergeants in making a shavtzak which they can alter, saving them time.
"""