import xlrd
import xlwt
import random
from xlrd import open_workbook
from xlutils.copy import copy
from time import gmtime, strftime
import os
import time
import copy as cp


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

"""
def makeExcel(list):
    today = str(strftime("%Y-%m-%d", gmtime()))
    book = xlwt.Workbook()
    sheet = book.add_sheet("Shavtzak")
    wb_name = "Shavtzak {0}".format(today)
    list_of_doubled = []
    all_people = []
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = True
    style.font = font
    style2 = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = False
    style2.font = font
    for i in list:
        if type(i) == str:
            all_people.append(i)
        else:
            all_people.append(i[0])
            all_people.append(i[1])
    for i in range(len(all_people)):
        for j in range(1 + i, len(all_people)):
            if all_people[i] == all_people[j]:
                list_of_doubled.append(all_people[i])
    sheet.write(0, 0, "Times: ")
    sheet.write(0, 1, "S.G")
    sheet.write(0, 2, "Tapuz")
    sheet.write(0, 3, "Siur")
    sheet.write(0, 4, "Hamal")
    sheet.write(0, 5, "Mitbah")
    sheet.write(1, 0, "6:00-10:00")
    sheet.write(2, 0, "10:00-14:00")
    sheet.write(3, 0, "14:00-18:00")
    sheet.write(4, 0, "18:00-22:00")
    sheet.write(5, 0, "22:00-2:00")
    sheet.write(6, 0, "2:00-6:00")
    sheet.write(1, 5, ", ".join(list[0]),
                style=style if list[0][0] in list_of_doubled or list[0][1] in list_of_doubled else style2)
    sheet.write(1, 4, list[1], style=style if list[1] in list_of_doubled else style2)
    sheet.write(1, 3, ", ".join(list[2]),
                style=style if list[2][0] in list_of_doubled or list[2][1] in list_of_doubled else style2)
    sheet.write(1, 1, list[3], style=style if list[3] in list_of_doubled else style2)
    sheet.write(1, 2, list[4], style=style if list[4] in list_of_doubled else style2)
    sheet.write(2, 1, list[5], style=style if list[5] in list_of_doubled else style2)
    sheet.write(2, 2, list[6], style=style if list[6] in list_of_doubled else style2)
    sheet.write(3, 4, list[7], style=style if list[7] in list_of_doubled else style2)
    sheet.write(3, 3, ", ".join(list[8]),
                style=style if list[8][0] in list_of_doubled or list[8][1] in list_of_doubled else style2)
    sheet.write(3, 1, list[9], style=style if list[9] in list_of_doubled else style2)
    sheet.write(3, 2, list[10], style=style if list[10] in list_of_doubled else style2)
    sheet.write(4, 1, list[11], style=style if list[11] in list_of_doubled else style2)
    sheet.write(4, 2, list[12], style=style if list[12] in list_of_doubled else style2)
    sheet.write(5, 4, list[13], style=style if list[13] in list_of_doubled else style2)
    sheet.write(5, 3, ", ".join(list[14]), style=style if list[14][0] in list_of_doubled or list[14][1] else style2)
    sheet.write(5, 1, list[15], style=style if list[15] in list_of_doubled else style2)
    sheet.write(5, 2, list[16], style=style if list[16] in list_of_doubled else style2)
    sheet.write(6, 1, list[17], style=style if list[17] in list_of_doubled else style2)
    sheet.write(6, 2, list[18], style=style if list[18] in list_of_doubled else style2)
    sheet.col(0).width = 3000
    sheet.col(1).width = 3000
    sheet.col(2).width = 5000
    sheet.col(3).width = 8000
    sheet.col(4).width = 5000
    sheet.col(5).width = 8000
    book.save(wb_name + ".xls")
    return wb_name
"""


def doSiur(dict, siurimNum, siurimNumEdit):
    rb = open_workbook("shavtzak.xls")
    div1 = {}
    div2 = {}
    div3 = {}
    div4 = {}
    for i in dict:
        value = rb.sheet_by_index(0).cell(int(dict[i]["Row"]), 3).value
        j = {i: value}
        if dict[i]["Division"] == 1 and (dict[i]["RestingHours"] <= 0 and (dict[i]["MitbahCooldown"] < 2)):
            div1.update(j)
        elif dict[i]["Division"] == 2 and (dict[i]["RestingHours"] <= 0 and (dict[i]["MitbahCooldown"] < 2)):
            div2.update(j)
        elif dict[i]["Division"] == 3 and (dict[i]["RestingHours"] <= 0 and (dict[i]["MitbahCooldown"] < 2)):
            div3.update(j)
        elif dict[i]["Division"] == 4 and (dict[i]["RestingHours"] <= 0 and (dict[i]["MitbahCooldown"] < 2)):
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
    if siurimNumEdit == 1:
        for i in list_of_soldiers:
            i.remove(i[1])
    for k in range(4):
        for i in list_of_soldiers:
            for j in i:
                if j == str:
                    list_of_soldiers.remove(i)
                    break
    r = random.randint(0, len(list_of_soldiers)-1)
    for i in list_of_soldiers[r]:
        for j in dict:
            if i == j:
                dict[j]["Siur"] += 1
                dict[j]["RestingHours"] = siurimNum * 8 + 12
    return list_of_soldiers[r], dict


def doMitbah(dict, siurimNum):
    highest1 = highest(dict, "Mitbach")
    highest2 = highest1
    soldier1 = {}
    soldier2 = {}
    soldiers = []
    list_to_pick = []
    soldier = random.choice(list_to_pick)
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
    print(soldiers)
    print(highest1)
    for i in dict:
        if i == soldier1:
            dict[i]["Mitbah"] += 1  # updating the mitbach count
            dict[i]["MitbahCooldown"] = 3  # updating the mitbachcd
            dict[i]["RestingHours"] = (siurimNum * 8) + 24
        elif i == soldier2:
            dict[i]["Mitbah"] += 1
            dict[i]["MitbahCooldown"] = 3
            dict[i]["RestingHours"] = (siurimNum * 8) + 24
    for i in soldiers:
        for j in dict:
            if i == j:
                dict[j]["Mitbach"] += 1

    for i in dict:
        if dict[i]["MitbahCooldown"] > 0:
            dict[i]["MitbahCooldown"] -= 1
    return soldiers, dict


def doMitbah2(dict, siurimNum):
    num = highest(dict, "Mitbach")
    list_to_pick = []
    soldier1, soldier2 = {}, {}
    for i in dict:
        if (dict[i]["Mitbach"] <= num) and (dict[i]["RestingHours"] <= 0) and (dict[i]["IsPtorMitbach"] == 0) and (dict[i]["MitbahCooldown"] <= 0):
            for k in range(int(dict[i]["Mitbach"])-1, int(num)):
                list_to_pick.append(i)
    soldier1 = random.choice(list_to_pick)
    for i in list_to_pick:
        if i == soldier1: list_to_pick.remove(i)
    soldier2 = random.choice(list_to_pick)
    soldiers = [soldier1, soldier2]
    for i in dict:
        if i == soldier1:
            dict[i]["Mitbach"] += 1  # updating the mitbach count
            dict[i]["MitbahCooldown"] = 3  # updating the mitbachcd
            dict[i]["RestingHours"] = (siurimNum * 8) + 28
        elif i == soldier2:
            dict[i]["Mitbach"] += 1
            dict[i]["MitbahCooldown"] = 3
            dict[i]["RestingHours"] = (siurimNum * 8) + 28
    for i in soldiers:
        for j in dict:
            if i == j:
                dict[j]["Mitbach"] += 1

    for i in dict:
        if dict[i]["MitbahCooldown"] > 0:
            dict[i]["MitbahCooldown"] -= 1
    return soldiers, dict


def doHamal(dict, hamalNum, siurimNum):
    num = highest(dict, "Hamal")
    soldier = ''
    for i in dict:
        if (dict[i]["RestingHours"] <= 0) and (dict[i]["IsHamal"] == 1) and (dict[i]["Hamal"] <= num) and (dict[i]["MitbahCooldown"] < 2):
            num = dict[i]["Hamal"]
            soldier = i
    for i in dict:
        if i == soldier:
            dict[i]["RestingHours"] = siurimNum * 8 + siurimNum * 8 + 12
            dict[i]["Hamal"] += 1
    return soldier, dict


def doSG(dict): # not in use
    num = highest(dict, "S.G")
    soldier = ''
    for i in dict:
        if (dict[i]["RestingHours"] <= 0) and (dict[i]["IsPtorShmirah"] == 0) and (dict[i]["S.G"] <= num) and (dict[i]["MitbahCooldown"] < 2):
            soldier = i
            num = dict[i]["S.G"]
    for i in dict:
        if i == soldier:
            dict[i]["RestingHours"] = 12
            dict[i]["S.G"] += 1
    return soldier, dict


def doSG2(dict):
    num = highest(dict, "S.G")
    list_to_pick = []
    for i in dict:
        if (dict[i]["RestingHours"] <= 0) and (dict[i]["IsPtorShmirah"] == 0) and (dict[i]["S.G"] <= num) and (
                dict[i]["MitbahCooldown"] < 2):
            for k in range(int(dict[i]["S.G"])-1, int(num)):
                list_to_pick.append(i)
    soldier = random.choice(list_to_pick)
    for i in dict:
        if i == soldier:
            dict[i]["RestingHours"] = 12
            dict[i]["S.G"] += 1
    return soldier, dict


def doTapuz(dict): # not in use
    num = highest(dict, "Tapuz")
    soldier = ''
    for i in dict:
        if (dict[i]["RestingHours"] <= 0) and (dict[i]["IsPtorShmirah"] == 0) and (dict[i]["Tapuz"] <= num) and (dict[i]["MitbahCooldown"] < 2):
            soldier = i
            num = dict[i]["Tapuz"]
    for i in dict:
        if i == soldier:
            dict[i]["RestingHours"] = 12
            dict[i]["Tapuz"] += 1
    return soldier, dict


def doTapuz2(dict):
    num = highest(dict, "Tapuz")
    list_to_pick = []
    for i in dict:
        if (dict[i]["RestingHours"] <= 0) and (dict[i]["IsPtorShmirah"] == 0) and (dict[i]["Tapuz"] <= num):
            for k in range(int(dict[i]["Tapuz"])-1, int(num)):
                list_to_pick.append(i)
    soldier = random.choice(list_to_pick)
    for i in dict:
        if i == soldier:
            dict[i]["RestingHours"] = 12
            dict[i]["Tapuz"] += 1
    return soldier, dict


def rewriteExcel(dict):
    for i in dict:
        rb = open_workbook("shavtzak.xls")
        wb = copy(rb)
        excel = wb.get_sheet(0)
        excel.write(dict[i]["Row"], 1, dict[i]["S.G"])
        excel.write(int(dict[i]["Row"]), 2, dict[i]["Tapuz"])
        excel.write(int(dict[i]["Row"]), 3, dict[i]["Siur"])
        excel.write(int(dict[i]["Row"]), 4, dict[i]["Mitbach"])
        excel.write(int(dict[i]["Row"]), 5, dict[i]["Hamal"])
        excel.write(int(dict[i]["Row"]), 10, dict[i]["RestingHours"])
        excel.write(int(dict[i]["Row"]), 12, dict[i]["MitbahCooldown"])
        wb.save("shavtzak.xls")


def makeExcel2(soldiers, siurim, hamal):
    today = str(strftime("%Y-%m-%d", gmtime()))
    book = xlwt.Workbook()
    sheet = book.add_sheet("Shavtzak")
    wb_name = "Shavtzak {0}".format(today)
    list_of_doubled = []
    all_people = []
    for i in soldiers:
        if type(i) == str:
            all_people.append(i)
        elif type(i) == list and type(i[0]) != list:
            for j in i:
                all_people.append(j)
        elif type(i) == dict:
            return ("Could not make perfect shavtzak!")
        elif type(i[0]) == list:
            for j in i:
                for k in j:
                    all_people.append(k)
    for i in range(len(all_people)):
        for j in range(1 + i, len(all_people)):
            if all_people[i] == all_people[j]:
                list_of_doubled.append(all_people[i])
    plain = xlwt.easyfont('')
    bold = xlwt.easyfont('bold true')
    for i in range(len(soldiers)):
        if type(soldiers[i]) == str:
            soldiers[i] = (soldiers[i], plain) if soldiers[i] not in list_of_doubled else (soldiers[i], bold)
        elif type(soldiers[i]) == list and type(soldiers[i][0]) != list:
            for j in range(len(soldiers[i])):
                soldiers[i][j] = (soldiers[i][j], plain) if soldiers[i][j] not in list_of_doubled else (soldiers[i][j], bold)
        if type(soldiers[i][0]) == list:
            for j in range(len(soldiers[i])):
                for k in range(len(soldiers[i][j])):
                    soldiers[i][j][k] = (soldiers[i][j][k], plain) if soldiers[i][j][k] not in list_of_doubled else (
                    soldiers[i][j][k], bold)

    #sheet.write_rich_text(0, 0, (seg1, seg2))
    sheet.write(0, 0, "Names")
    sheet.write(0, 1, "S.G")
    sheet.write(0, 2, "Tapuz")
    sheet.write(0, 3, "Siur")
    sheet.write(0, 4, "Hamal")
    sheet.write(0, 5, "Mitbah")
    sheet.write(1, 0, "6:00-10:00")
    sheet.write(2, 0, "10:00-14:00")
    sheet.write(3, 0, "14:00-18:00")
    sheet.write(4, 0, "18:00-22:00")
    sheet.write(5, 0, "22:00-2:00")
    sheet.write(6, 0, "2:00-6:00")
    sheet.write_rich_text(1, 5, (soldiers[0], ", ", soldiers[1]))
    sheet.write_rich_text(1, 4, (soldiers[2][0], " "))
    sheet.write_rich_text(2, 4, (soldiers[2][0], " "))
    sheet.write_rich_text(3, 4, (soldiers[2][1], " "))
    sheet.write_rich_text(4, 4, (soldiers[2][1], " "))
    sheet.write_rich_text(5, 4, (soldiers[2][2], " "))
    sheet.write_rich_text(6, 4, (soldiers[2][2], " "))
    if (len(soldiers[3][0])) == 2:
        if (len(soldiers[3])) == 3:
            sheet.write_rich_text(1, 3, (soldiers[3][0][0], ", ", soldiers[3][0][1]))
            sheet.write_rich_text(2, 3, (soldiers[3][0][0], ", ", soldiers[3][0][1]))
            sheet.write_rich_text(3, 3, (soldiers[3][1][0], ", ", soldiers[3][1][1]))
            sheet.write_rich_text(4, 3, (soldiers[3][1][0], ", ", soldiers[3][1][1]))
            sheet.write_rich_text(5, 3, (soldiers[3][2][0], ", ", soldiers[3][2][1]))
            sheet.write_rich_text(6, 3, (soldiers[3][2][0], ", ", soldiers[3][2][1]))
        elif (len(soldiers[3])) == 2:
            sheet.write_rich_text(1, 3, (soldiers[3][0][0], ", ", soldiers[3][0][1]))
            sheet.write_rich_text(2, 3, (soldiers[3][0][0], ", ", soldiers[3][0][1]))
            sheet.write_rich_text(5, 3, (soldiers[3][1][0], ", ", soldiers[3][1][1]))
            sheet.write_rich_text(6, 3, (soldiers[3][1][0], ", ", soldiers[3][1][1]))
        elif (len(soldiers[3])) == 1:
            sheet.write_rich_text(5, 3, (soldiers[3][0][0], ", ", soldiers[3][0][1]))
            sheet.write_rich_text(6, 3, (soldiers[3][0][0], ", ", soldiers[3][0][1]))
    elif (len(soldiers[3][0])) == 1:
        if (len(soldiers[3])) == 3:
            sheet.write_rich_text(1, 3, (soldiers[3][0][0], " "))
            sheet.write_rich_text(2, 3, (soldiers[3][0][0], " "))
            sheet.write_rich_text(3, 3, (soldiers[3][1][0], " "))
            sheet.write_rich_text(4, 3, (soldiers[3][1][0], " "))
            sheet.write_rich_text(5, 3, (soldiers[3][2][0], " "))
            sheet.write_rich_text(6, 3, (soldiers[3][2][0], " "))
        elif (len(soldiers[3])) == 2:
            sheet.write_rich_text(1, 3, (soldiers[3][0][0], " "))
            sheet.write_rich_text(2, 3, (soldiers[3][0][0], " "))
            sheet.write_rich_text(5, 3, (soldiers[3][1][0], " "))
            sheet.write_rich_text(6, 3, (soldiers[3][1][0], " "))
        elif (len(soldiers[3])) == 1:
            sheet.write_rich_text(5, 3, (soldiers[3][0][0], " "))
            sheet.write_rich_text(6, 3, (soldiers[3][0][0], " "))
    sheet.write_rich_text(1, 1, (soldiers[4], " "))
    sheet.write_rich_text(1, 2, (soldiers[5], " "))
    sheet.write_rich_text(2, 1, (soldiers[6], " "))
    sheet.write_rich_text(2, 2, (soldiers[7], " "))
    sheet.write_rich_text(3, 1, (soldiers[8], " "))
    sheet.write_rich_text(3, 2, (soldiers[9], " "))
    sheet.write_rich_text(4, 1, (soldiers[10], " "))
    sheet.write_rich_text(4, 2, (soldiers[11], " "))
    sheet.write_rich_text(5, 1, (soldiers[12], " "))
    sheet.write_rich_text(5, 2, (soldiers[13], " "))
    sheet.write_rich_text(6, 1, (soldiers[14], " "))
    sheet.write_rich_text(6, 2, (soldiers[15], " "))
    sheet.col(0).width = 3000
    sheet.col(1).width = 5000
    sheet.col(2).width = 5000
    sheet.col(3).width = 8000
    sheet.col(4).width = 5000
    sheet.col(5).width = 8000
    book.save(wb_name + ".xls")
    return wb_name, list_of_doubled


def cycle2(dict1, siurimNum, SiurimNumEdit, makePerfect, attempts, sevev, inactive):
    for i in inactive:
        dict1.pop(i)
        print(i)
    # Mitbah first, then hamal, then siurim and then shmirot
    dict2 = dict1
    list_of_soldiers, doubled = computeList(dict1, siurimNum, SiurimNumEdit, sevev)
    if attempts == 0:
        print("Could not make perfect shavtzak withing the given attempts.")
        return
    if makePerfect and doubled:
        print("Making perfect shavtzak.")
        while doubled != [] and attempts > 0:
            dict2 = cp.deepcopy(dict1)
            list_of_soldiers, doubled = computeList(dict2, siurimNum, SiurimNumEdit, sevev)
            print(attempts)
            attempts -= 1
    print("Made shavtzak.")
    excel_file, x = makeExcel2(list_of_soldiers, siurimNum, SiurimNumEdit) # make the new excel shavtzak file
    os.startfile(excel_file + ".xls")
    rewriteExcel(dict2)  # upload the information to the original excel file and update the information on it


def computeList(dict, siurimNum, SiurimNumEdit, sevev):
    list_of_soldiers = []
    hamal_list = []
    siurim_list = []
    dict2 = dict.copy()
    if sevev == 0: # normal
        pass
    elif sevev == 1: # MP
        for i in list(dict2):
            if not dict2[i]["IsSevevMP"]:
                dict2.pop(i)
    elif sevev == 2: # smp
        dict2.pop("Lidor ")
        for i in list(dict2):
            if dict2[i]["IsSevevMP"]:
                dict2.pop(i)
    mitbah, dict2 = doMitbah2(dict2, siurimNum)
    for i in mitbah:
        list_of_soldiers.append(i)
    for j in range(3):
        hamal, dict2 = doHamal(dict2, SiurimNumEdit, siurimNum)
        hamal_list.append(hamal)
        for i in dict2:
            if dict2[i]["RestingHours"] > 0:
                dict2[i]["RestingHours"] -= 4  # so they can do other missions other than hamal
    for j in range(siurimNum):
        siur, dict2 = doSiur(dict2, siurimNum, SiurimNumEdit)
        siurim_list.append(siur)
        for i in dict2:
            if dict2[i]["RestingHours"] > 0:
                dict2[i]["RestingHours"] -= 4  # same as hamal
    list_of_soldiers.append(hamal_list)
    list_of_soldiers.append(siurim_list)
    for i in range(6):
        sg, dict2 = doSG2(dict2)
        list_of_soldiers.append(sg)
        tapuz, dict2 = doTapuz2(dict2)
        list_of_soldiers.append(tapuz)
        for i in dict2:
            if dict2[i]["RestingHours"] > 0:
                dict2[i]["RestingHours"] -= 4
    list_of_doubled = []
    all_people = []
    for i in list_of_soldiers:
        if i == {}:
            return [], ["Data"]
        elif type(i) == str:
            all_people.append(i)
        elif type(i) == list and type(i[0]) != list:
            for j in i:
                all_people.append(j)
        elif type(i[0]) == list:
            for j in i:
                for k in j:
                    all_people.append(k)
    for i in range(len(all_people)):
        for j in range(1 + i, len(all_people)):
            if all_people[i] == all_people[j]:
                list_of_doubled.append(all_people[i])

    return list_of_soldiers, list_of_doubled


