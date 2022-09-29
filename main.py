import xlrd
import xlwt
from funcs import *
import time
from time import gmtime, strftime


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
    list = cycle2(dict)
    print("Final shavtzak for today:")
    print("Mitbah: ", ", ".join(list[0]))
    print("Hamal: 6:00-14:00", list[1])
    print("Siur: 6:00-14:00", ", ".join(list[2]))
    print("S.G: 6:00-10:00", list[3])
    print("Tapuz: 6:00-10:00", list[4])
    print("S.G: 10:00-14:00", list[5])
    print("Tapuz: 10:00-14:00", list[6])
    print("Hamal: 14:00-22:00", list[7])
    print("Siur: 14:00-22:00", ", ".join(list[8]))
    print("S.G: 14:00-18:00", list[9])
    print("Tapuz: 14:00-18:00", list[10])
    print("S.G: 18:00-22:00", list[11])
    print("Tapuz: 18:00-22:00", list[12])
    print("Hamal: 22:00-6:00", list[13])
    print("Siur: 22:00-6:00", ", ".join(list[14]))
    print("S.G: 22:00-2:00", list[15])
    print("Tapuz: 22:00-2:00", list[16])
    print("S.G: 2:00-6:00", list[17])
    print("Tapuz: 2:00-6:00", list[18])
    """
    The code works in 6 cycles, updating the rest hours & current mission of each soldier on duty. This will be done by calling in a specific function several times.
    The aim is to make sure the soldiers don't do more than 4/8 or 8/8. Doing 4/8 reduces 3 resting points (1 for the 4 hours of guarding and 2 for the 8 hours of rest),
    while 'siur' and 'hamal' give 4 (same logic). The program will attempt to have everyone's average the same number so everything is equal. The focus is not to make a complete
    'shavtzak', but to aid to the sergeants in making a shavtzak which they can alter, saving them time.
    """
    today = str(strftime("%Y-%m-%d", gmtime()))
    book = xlwt.Workbook()
    sheet = book.add_sheet("Shavtzak")
    wb_name = "Shavtzak {0}".format(today)
    sheet.write(0,0, "Times: ")
    sheet.write(0,1, "S.G")
    sheet.write(0,2,"Tapuz")
    sheet.write(0,3,"Siur")
    sheet.write(0,4,"Hamal")
    sheet.write(0,5,"Mitbah")
    sheet.write(1,0,"6:00-10:00")
    sheet.write(2,0,"10:00-14:00")
    sheet.write(3,0,"14:00-18:00")
    sheet.write(4,0,"18:00-22:00")
    sheet.write(5,0,"22:00-2:00")
    sheet.write(6,0,"2:00-6:00")
    sheet.write(1,3,", ".join(list[0]))
    sheet.write(1,4,list[1])
    sheet.write(1,5,", ".join(list[2]))
    sheet.write(1,1,list[3])
    sheet.write(1,2,list[4])
    sheet.write(2,1,list[5])
    sheet.write(2,2,list[6])
    sheet.write(3,4,list[7])
    sheet.write(3,3,", ".join(list[8]))
    sheet.write(3,1,list[9])
    sheet.write(3,2,list[10])
    sheet.write(4,1,list[11])
    sheet.write(4,2,list[12])
    sheet.write(5,4,list[13])
    sheet.write(5,3,", ".join(list[14]))
    sheet.write(5,1,list[15])
    sheet.write(5,2,list[16])
    sheet.write(6,1,list[17])
    sheet.write(6,2,list[18])
    sheet.col(0).width = 3000
    sheet.col(1).width = 3000
    sheet.col(2).width = 5000
    sheet.col(3).width = 8000
    sheet.col(4).width = 5000
    sheet.col(5).width = 8000
    book.save(wb_name + ".xls")
    print("Time: ", time.process_time() - time1)

if __name__ == "__main__":
    try:
        main()
    except PermissionError:
        print("The excel file is open. Close it and restart the program.")
