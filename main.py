import xlrd
from funcs import *
from classes import *
import time
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def window(dict):
    app = QApplication(sys.argv)
    win = MyWindow(dict)
    win.show()
    sys.exit(app.exec_())


def main():
    time1 = time.process_time()
    wbr = xlrd.open_workbook("D:\ShavTzak\shavtzak.xls")
    sheets = wbr.sheets()[0]
    list_of_soldiers = []
    index = 1
    for i in range(sheets.nrows):
        soldier_value = wbr.sheet_by_index(0).row_values(i)
        list_of_soldiers.append(soldier_value)

    dict = listToDict(list_of_soldiers)
    # list = cycle(dict, 3, 3)
    """
    The code works in 6 cycles, updating the rest hours & current mission of each soldier on duty. This will be done by calling in a specific function several times.
    The aim is to make sure the soldiers don't do more than 4/8 or 8/8. Doing 4/8 reduces 3 resting points (1 for the 4 hours of guarding and 2 for the 8 hours of rest),
    while 'siur' and 'hamal' give 4 (same logic). The program will attempt to have everyone's average the same number so everything is equal. The focus is not to make a complete
    'shavtzak', but to aid to the sergeants in making a shavtzak which they can alter, saving them time.
    """
    window(dict)
    print("Time: ", time.process_time() - time1)

if __name__ == "__main__":
    try:
        main()
    except PermissionError:
        sys.exit("The excel file is open. Close it and restart the program.")
