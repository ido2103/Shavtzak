from multiprocessing import shared_memory
from tkinter import Y
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import time



def avg(dict, key):
    avg = 0
    for i in dict:
        avg += dict[i][key]
    return avg/len(dict)


def lowest(dict, key):
    low = 0
    for i in dict:
        if dict[i][key] < low and dict[i]["RestingHours"] <= 0:
            low = dict[i][key]
    return low


def highest(dict, key):
    high = 0
    for i in dict:
        if dict[i][key] > high and dict[i]["RestingHours"] <= 0:
            high = dict[i][key]
    return high


def higherAvg(list, index):
    """
    Returns Lists of higher than averge names
    """
    l = []
    averege = avg(list, index)
    for i in range(len(list)):
        if (list[i][index] > averege):
            l.append(list[i])
    return l


def listToDict(soldiers):
    """This function will convert the list that we exctract from excel to a dict that's easier to work for."""
    titles = soldiers[0]
    soldiers.remove(soldiers[0])
    dict = {}
    for i in range(len(soldiers)):
        temp = {}
        for j in range(1, len(soldiers[i])):
            temp.update({titles[j]: soldiers[i][j]})
        dict.update({soldiers[i][0]: temp})
    return dict


def reduceMitbahCD(dict, excel):
    for i in dict:
        if dict[i]["MitbahCooldown"] > 0:
            dict[i]["MitbahCooldown"] -= 1


def rewriteExcel(dict, excel):
    for i in dict:
        excel.write(dict[i]["Row"], 1, dict[i]["S.G"])
        excel.write(int(dict[i]["Row"]), 2, dict[i]["Nishkia"])
        excel.write(int(dict[i]["Row"]), 3, dict[i]["Siur"])
        excel.write(int(dict[i]["Row"]), 4, dict[i]["Mitbach"])
        excel.write(int(dict[i]["Row"]), 5, dict[i]["Hamal"])
        excel.write(int(dict[i]["Row"]), 10, dict[i]["RestingHours"])
        excel.write(int(dict[i]["Row"]), 12, dict[i]["MitbahCooldown"])


def cycle(dict, cycleNum):
    # Setting up the excel sheet. To write in it use excel.write(row, column, "data").
    rb = open_workbook("shavtzak.xls")
    wb = copy(rb)
    excel = wb.get_sheet(0)
    """TODO: create the function that is called upon 6 times in order to build the shavtzak. the function receives the list
    of soldiers and builds each "phase" of the shavtzak according to the cycleNum when called. this is the annoying function
    that will be very annoying to write.
    Check for highest SG, Nishkia, siur and so on... Lastly place SG and Nishkia
    The function finds the person with the highest amount of mitbach and then looks for people who are
    a) can do mitbach
    b) have a lower amount
    * this can be improved because it's really memory inefficient but i'm lazy and i don't wanna do it right now
    """
    """The following section gets the 2 people that has the lowest amount to be in the kitchen. 
    TODO:
    make a 1 day minimum cooldown on mitbach"""
    highest1 = highest(dict, "Mitbach")
    print(highest1)
    highest2 = highest1
    soldier1 = {}
    soldier2 = {}
    soldiers = []
    t0 = time.perf_counter()
    # Mitbah
    # Mitbah
    for i in dict:
        if dict[i]["Mitbach"] <= highest1 and (dict[i]["RestingHours"] <= 0) and (dict[i]["IsPtorMitbach"] == 0) and (dict[i]["MitbahCooldown"] <= 0):
            highest1 = dict[i]["Mitbach"]
            soldier1 = i
        elif dict[i]["Mitbach"] <= highest2 and (dict[i]["RestingHours"] <= 0) and (dict[i]["IsPtorMitbach"] == 0) and (dict[i]["MitbahCooldown"] <= 0):
            highest2 = dict[i]["Mitbach"]
            soldier2 = i
        if highest1 > highest2:
            highest1, highest2 = highest2, highest1
            soldier1, soldier2 = soldier2, soldier1
    soldiers.append(soldier1)
    soldiers.append(soldier2)
    print(soldiers)
    for i in dict:
        if i == soldier1:
            value = rb.sheet_by_index(0).cell(int(dict[i]["Row"]), 4).value
            value += 1
            excel.write(int(dict[i]["Row"]), 4, value) # updating the mitbach count
            dict[i]["MitbahCooldown"] = 3 # updating the mitbachcd
        elif i == soldier2:
            value = rb.sheet_by_index(0).cell(int(dict[i]["Row"]), 4).value
            value += 1
            excel.write(int(dict[i]["Row"]), 4, value)
            dict[i]["MitbahCooldown"] = 3
    for i in soldiers:
        for j in dict:
            if i == j:
                dict[j]["Mitbach"] += 1
    """
    for i in range(len(soldiers)):
        temp = {}
        temp.update({soldiers[i]: "Mitbach"})
        soldiers.append(temp)
    """
    soldiers = [soldier for soldier in soldiers if type(soldier) != str]
    print(soldiers)
    for i in dict:
        if (dict[i]["IsPtorMitbach"] == 0) and (dict[i]["MitbahCooldown"] > 0):
            print(dict[i]["MitbahCooldown"])
            dict[i]["MitbahCooldown"] -= 1
            print(dict[i]["MitbahCooldown"])
    # Siur
    # Hamal
    # Nishkia
    # SG
    rewriteExcel(dict, excel)
    wb.save("shavtzak.xls")
    t1 = time.perf_counter()
    print("Time:", t0-t1)
    return soldiers



