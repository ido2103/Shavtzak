import xlrd
import random
from xlrd import open_workbook
from xlutils.copy import copy


def avg(dict, key):
    avg = 0
    for i in dict:
        avg += dict[i][key]
    return avg/len(dict)


def lowest(dict, key):
    low = 999
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


def doSiur(dict):
    rb = open_workbook("shavtzak.xls")
    div1 = {}
    div2 = {}
    div3 = {}
    div4 = {}
    for i in dict:
        value = rb.sheet_by_index(0).cell(int(dict[i]["Row"]), 3).value
        j = {i: value}
        if dict[i]["Division"] == 1 and dict[i]["RestingHours"] <= 0 and dict[i]["MitbahCooldown"] < 2:
            div1.update(j)
        elif dict[i]["Division"] == 2 and dict[i]["RestingHours"] <= 0 and dict[i]["MitbahCooldown"] < 2:
            div2.update(j)
        elif dict[i]["Division"] == 3 and dict[i]["RestingHours"] <= 0 and dict[i]["MitbahCooldown"] < 2:
            div3.update(j)
        elif dict[i]["Division"] == 4 and dict[i]["RestingHours"] <= 0 and dict[i]["MitbahCooldown"] < 2:
            div4.update(j)
    lowest1div1, lowest2div1 = 999, 999
    soldier1div1, soldier2div1 = str, str
    lowest1div2, lowest2div2 = 999, 999
    soldier1div2, soldier2div2 = str, str
    lowest1div3, lowest2div3 = 999, 999
    soldier1div3, soldier2div3 = str, str
    lowest1div4, lowest2div4 = 999, 999
    soldier1div4, soldier2div4 = str, str
    temp_list = []
    list_of_soldiers = []
    for i in div1:
        if div1[i] < lowest1div1:
            lowest1div1 = div1[i]
            soldier1div1 = i
        elif div1[i] < lowest2div1:
            lowest2div1 = div1[i]
            soldier2div1 = i
        if lowest1div1 < lowest2div1:
            lowest2div1, lowest1div1 = lowest1div1, lowest2div1
            soldier2div1, soldier1div1 = soldier1div1, soldier2div1
    temp_list.append(soldier1div1)
    temp_list.append(soldier2div1)
    list_of_soldiers.append(temp_list)
    temp_list = []
    for i in div2:
        if div2[i] < lowest1div2:
            lowest1div2 = div2[i]
            soldier1div2 = i
        elif div2[i] < lowest2div2:
            lowest2div2 = div2[i]
            soldier2div2 = i
        if lowest1div2 < lowest2div2:
            lowest2div2, lowest1div2 = lowest1div2, lowest2div2
            soldier2div2, soldier1div2 = soldier1div2, soldier2div2
    temp_list.append(soldier1div2)
    temp_list.append(soldier2div2)
    list_of_soldiers.append(temp_list)
    temp_list = []
    for i in div3:
        if div3[i] < lowest1div3:
            lowest1div3 = div3[i]
            soldier1div3 = i
        elif div3[i] < lowest2div3:
            lowest2div3 = div3[i]
            soldier2div3 = i
        if lowest1div3 < lowest2div3:
            lowest2div3, lowest1div3 = lowest1div3, lowest2div3
            soldier2div3, soldier1div3 = soldier1div3, soldier2div3
    temp_list.append(soldier1div3)
    temp_list.append(soldier2div3)
    list_of_soldiers.append(temp_list)
    temp_list = []
    for i in div4:
        if div4[i] < lowest1div4:
            lowest1div4 = div4[i]
            soldier1div4 = i
        elif div4[i] < lowest2div4:
            lowest2div4 = div4[i]
            soldier2div4 = i
        if lowest1div4 < lowest2div4:
            lowest2div4, lowest1div4 = lowest1div4, lowest2div4
            soldier2div4, soldier1div4 = soldier1div4, soldier2div4
    temp_list.append(soldier1div4)
    temp_list.append(soldier2div4)
    list_of_soldiers.append(temp_list)
    for i in list_of_soldiers:
        if i[0] == str or i[1] == "":
            list_of_soldiers.remove(i)
    r = random.randint(0, len(list_of_soldiers)-1)
    for i in list_of_soldiers[r]:
        for j in dict:
            if i == j:
                dict[j]["Siur"] += 1
                dict[j]["RestingHours"] = 16

    return list_of_soldiers[r]


def doMitbah(dict):
    rb = open_workbook("shavtzak.xls")
    highest1 = highest(dict, "Mitbach")
    highest2 = highest1
    soldier1 = {}
    soldier2 = {}
    soldiers = []
    for i in dict:
        if dict[i]["Mitbach"] <= highest1 and (dict[i]["RestingHours"] <= 0) and (dict[i]["IsPtorMitbach"] == 0) and (
                dict[i]["MitbahCooldown"] <= 0):
            highest1 = dict[i]["Mitbach"]
            soldier1 = i
        elif dict[i]["Mitbach"] <= highest2 and (dict[i]["RestingHours"] <= 0) and (dict[i]["IsPtorMitbach"] == 0) and (
                dict[i]["MitbahCooldown"] <= 0):
            highest2 = dict[i]["Mitbach"]
            soldier2 = i
        if highest1 > highest2:
            highest1, highest2 = highest2, highest1
            soldier1, soldier2 = soldier2, soldier1
    soldiers.append(soldier1)
    soldiers.append(soldier2)
    for i in dict:
        if i == soldier1:
            value = rb.sheet_by_index(0).cell(int(dict[i]["Row"]), 4).value
            value += 1
            dict[i]["Mitbah"] = value  # updating the mitbach count
            dict[i]["MitbahCooldown"] = 3  # updating the mitbachcd
            dict[i]["RestingHours"] = 24
        elif i == soldier2:
            value = rb.sheet_by_index(0).cell(int(dict[i]["Row"]), 4).value
            value += 1
            dict[i]["Mitbah"] = value
            dict[i]["MitbahCooldown"] = 3
            dict[i]["RestingHours"] = 24
    for i in soldiers:
        for j in dict:
            if i == j:
                dict[j]["Mitbach"] += 1

    for i in dict:
        if (dict[i]["IsPtorMitbach"] == 0) and (dict[i]["MitbahCooldown"] > 0):
            dict[i]["MitbahCooldown"] -= 1
    return soldiers, dict


def doHamal(dict):
    num = highest(dict, "Hamal")
    soldier = ''
    for i in dict:
        if (dict[i]["RestingHours"] <= 0) and (dict[i]["IsHamal"] == 1) and (dict[i]["Hamal"] <= num):
            num = dict[i]["Hamal"]
            soldier = i
    for i in dict:
        if i == soldier:
            dict[i]["RestingHours"] = 16
            dict[i]["Hamal"] += 1
    return soldier, dict


def doSG(dict):
    num = highest(dict, "S.G")
    soldier = ''
    for i in dict:
        if (dict[i]["RestingHours"] <= 0) and (dict[i]["IsPtorShmirah"] == 0) and (dict[i]["S.G"] < num):
            soldier = i
            num = dict[i]["S.G"]
    for i in dict:
        if i == soldier:
            dict[i]["RestingHours"] = 8
            dict[i]["S.G"] += 1
    return soldier, dict

def rewriteExcel(dict):
    for i in dict:
        rb = open_workbook("shavtzak.xls")
        wb = copy(rb)
        excel = wb.get_sheet(0)
        excel.write(dict[i]["Row"], 1, dict[i]["S.G"])
        excel.write(int(dict[i]["Row"]), 2, dict[i]["Nishkia"])
        excel.write(int(dict[i]["Row"]), 3, dict[i]["Siur"])
        excel.write(int(dict[i]["Row"]), 4, dict[i]["Mitbach"])
        excel.write(int(dict[i]["Row"]), 5, dict[i]["Hamal"])
        excel.write(int(dict[i]["Row"]), 10, dict[i]["RestingHours"])
        excel.write(int(dict[i]["Row"]), 12, dict[i]["MitbahCooldown"])
        wb.save("shavtzak.xls")


def cycle(dict):
    # Setting up the excel sheet. To write in it use excel.write(row, column, "data").
    rb = open_workbook("shavtzak.xls")
    wb = copy(rb)
    # Mitbah
    mitbah, dict = doMitbah(dict)
    print("Mitbah: ", ', '.join(mitbah))
    # Hamal
    hamal, dict = doHamal(dict)
    print("Hamal: ", hamal)
    # Siur
    siur = doSiur(dict)
    print("Siur: ", ', '.join(siur))
    # Nishkia
    # SG
    sg, dict = doSG(dict)
    print("S.G: ", sg)
    for i in dict:
            dict[i]["RestingHours"] = 0
    rewriteExcel(dict)
    return dict
