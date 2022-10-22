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


def highestindiv(dict, key):
    highest1, highest2, highest3, highest4 = 0,0,0,0
    for i in dict:
        if dict[i][key] > highest1 and dict[i]["Division"] == 1 and dict[i]["RestingHours"] <= 0:
            highest1 = dict[i][key]
        elif dict[i][key] > highest2 and dict[i]["Division"] == 2 and dict[i]["RestingHours"] <= 0:
            highest2 = dict[i][key]
        elif dict[i][key] > highest3 and dict[i]["Division"] == 3 and dict[i]["RestingHours"] <= 0:
            highest3 = dict[i][key]
        elif dict[i][key] > highest4 and dict[i]["Division"] == 4 and dict[i]["RestingHours"] <= 0:
            highest4 = dict[i][key]
    return highest1, highest2, highest3, highest4


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


def doSiur2(dict, siurimNum, siurimNumEdit):
    highest1, highest2, highest3, highest4 = highestindiv(dict, "Siur")
    div1, div2, div3, div4 = [], [], [], []
    for i in dict:
        if dict[i]["Siur"] <= highest1 and dict[i]["RestingHours"] <= 0 and dict[i]["Division"] == 1:
            for k in range(int(dict[i]["Siur"])-1, int(highest1)):
                div1.append(i)
        elif dict[i]["Siur"] <= highest2 and dict[i]["RestingHours"] <= 0 and dict[i]["Division"] == 2:
            for k in range(int(dict[i]["Siur"])-1, int(highest2)):
                div2.append(i)
        elif dict[i]["Siur"] <= highest3 and dict[i]["RestingHours"] <= 0 and dict[i]["Division"] == 3:
            for k in range(int(dict[i]["Siur"])-1, int(highest3)):
                div3.append(i)
        elif dict[i]["Siur"] <= highest4 and dict[i]["RestingHours"] <= 0 and dict[i]["Division"] == 4:
            for k in range(int(dict[i]["Siur"])-1, int(highest4)):
                div4.append(i)
    list_of_soldiers = []
    if siurimNumEdit == 1:
        if div1: div1 = random.choice(div1)
        if div2: div2 = random.choice(div2)
        if div3: div3 = random.choice(div3)
        if div4: div4 = random.choice(div4)
        if div1 != []:
            list_of_soldiers.append([div1])
        if div2 != []:
            list_of_soldiers.append([div2])
        if div3 != []:
            list_of_soldiers.append([div3])
        if div4 != []:
            list_of_soldiers.append([div4])
    elif siurimNumEdit == 2:
        try:
            soldier1 = random.choice(div1)
            div1.remove(soldier1)
            for i in range(len(div1)):
                if soldier1 in div1:
                    div1.remove(soldier1)
            soldier2 = random.choice(div1)
            div1 = [soldier1, soldier2]
        except Exception:
            pass
        try:
            soldier1 = random.choice(div2)
            div2.remove(soldier1)
            for i in range(len(div2)):
                if soldier1 in div2:
                    div2.remove(soldier1)
            soldier2 = random.choice(div2)
            div2 = [soldier1, soldier2]
        except Exception:
            pass
        try:
            soldier1 = random.choice(div3)
            div3.remove(soldier1)
            for i in range(len(div3)):
                if soldier1 in div3:
                    div3.remove(soldier1)
            soldier2 = random.choice(div3)
            div3 = [soldier1, soldier2]
        except Exception:
            pass
        try:
            soldier1 = random.choice(div4)
            div4.remove(soldier1)
            for i in range(len(div4)):
                if soldier1 in div4:
                    div4.remove(soldier1)
            soldier2 = random.choice(div4)
            div4 = [soldier1, soldier2]
        except Exception:
            pass
        list_of_soldiers = [div1,div2,div3,div4]
        for k in range(4):
            for i in list_of_soldiers:
                if i == []:
                    list_of_soldiers.remove(i)
        if siurimNumEdit == 1:
            for i in list_of_soldiers:
                i.remove(i[1])
    r = random.randint(0, len(list_of_soldiers)-1)
    for i in list_of_soldiers[r]:
        for j in dict:
            if i == j:
                dict[j]["Siur"] += 1
                dict[j]["RestingHours"] = siurimNum * 8 + 12
    return list_of_soldiers[r], dict


def exampleSiur(dict, siurimNum, siurimNumEdit, list):
    highest1, highest2, highest3, highest4 = highestindiv(dict, "Siur")
    div1, div2, div3, div4 = [], [], [], []
    for i in dict:
        if dict[i]["Siur"] <= highest1 and dict[i]["RestingHours"] <= 0 and dict[i]["Division"] == 1 and i not in list:
            for k in range(int(dict[i]["Siur"])-1, int(highest1)):
                div1.append(i)
        elif dict[i]["Siur"] <= highest2 and dict[i]["RestingHours"] <= 0 and dict[i]["Division"] == 2 and i not in list:
            for k in range(int(dict[i]["Siur"])-1, int(highest2)):
                div2.append(i)
        elif dict[i]["Siur"] <= highest3 and dict[i]["RestingHours"] <= 0 and dict[i]["Division"] == 3 and i not in list:
            for k in range(int(dict[i]["Siur"])-1, int(highest3)):
                div3.append(i)
        elif dict[i]["Siur"] <= highest4 and dict[i]["RestingHours"] <= 0 and dict[i]["Division"] == 4 and i not in list:
            for k in range(int(dict[i]["Siur"])-1, int(highest4)):
                div4.append(i)
    list_of_soldiers = []
    if siurimNumEdit == 1:
        if div1: div1 = random.choice(div1)
        if div2: div2 = random.choice(div2)
        if div4: div3 = random.choice(div3)
        if div4: div4 = random.choice(div4)
        if div1 != []:
            list_of_soldiers.append([div1])
        if div2 != []:
            list_of_soldiers.append([div2])
        if div3 != []:
            list_of_soldiers.append([div3])
        if div4 != []:
            list_of_soldiers.append([div4])
    elif siurimNumEdit == 2:
        try:
            soldier1 = random.choice(div1)
            div1.remove(soldier1)
            for i in range(len(div1)):
                if soldier1 in div1:
                    div1.remove(soldier1)
            soldier2 = random.choice(div1)
            div1 = [soldier1, soldier2]
        except Exception:
            pass
        try:
            soldier1 = random.choice(div2)
            div2.remove(soldier1)
            for i in range(len(div2)):
                if soldier1 in div2:
                    div2.remove(soldier1)
            soldier2 = random.choice(div2)
            div2 = [soldier1, soldier2]
        except Exception:
            pass
        try:
            soldier1 = random.choice(div3)
            div3.remove(soldier1)
            for i in range(len(div3)):
                if soldier1 in div3:
                    div3.remove(soldier1)
            soldier2 = random.choice(div3)
            div3 = [soldier1, soldier2]
        except Exception:
            pass
        try:
            soldier1 = random.choice(div4)
            div4.remove(soldier1)
            for i in range(len(div4)):
                if soldier1 in div4:
                    div4.remove(soldier1)
            soldier2 = random.choice(div4)
            div4 = [soldier1, soldier2]
        except Exception:
            pass
        list_of_soldiers = [div1,div2,div3,div4]
        for k in range(4):
            for i in list_of_soldiers:
                if i == []:
                    list_of_soldiers.remove(i)
        if siurimNumEdit == 1:
            for i in list_of_soldiers:
                i.remove(i[1])
    new_list = []
    for i in list_of_soldiers:
        for j in i:
            new_list.append(j)
    return new_list


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


def doMitbah2(dict, siurimNum):
    num = highest(dict, "Mitbach")
    list_to_pick = []
    soldier1, soldier2 = {}, {}
    for i in dict:
        if (dict[i]["Mitbach"] <= num) and (dict[i]["RestingHours"] <= 0) and (dict[i]["IsPtorMitbach"] == 0) and (dict[i]["MitbahCooldown"] <= 0):
            for k in range(int(dict[i]["Mitbach"])-1, int(num)):
                list_to_pick.append(i)
    soldier1 = random.choice(list_to_pick)
    for j in range(0, len(list_to_pick)-1):
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
        if dict[i]["MitbahCooldown"] > 0:
            dict[i]["MitbahCooldown"] -= 1
    return soldiers, dict


def doHamal2(dict, hamalNum, siurimNum):
    num = highest(dict, "Hamal")
    hamals = []
    for i in dict:
        if (dict[i]["RestingHours"] <= 0) and (dict[i]["IsHamal"] == 1) and (dict[i]["Hamal"] <= num) and (
                dict[i]["MitbahCooldown"] < 2):
            for k in range(int(dict[i]["Hamal"])-1, int(num)):
                hamals.append(i)
    soldier = random.choice(hamals)
    dict[soldier]["RestingHours"] = siurimNum * 8 + siurimNum * 8 + 12
    dict[soldier]["Hamal"] += 1
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
    dict[soldier]["RestingHours"] = 12
    dict[soldier]["S.G"] += 1
    return soldier, dict


def doTapuz2(dict):
    num = highest(dict, "Tapuz")
    list_to_pick = []
    for i in dict:
        if (dict[i]["RestingHours"] <= 0) and (dict[i]["IsPtorShmirah"] == 0) and (dict[i]["Tapuz"] <= num):
            for k in range(int(dict[i]["Tapuz"])-1, int(num)):
                list_to_pick.append(i)
    soldier = random.choice(list_to_pick)
    dict[soldier]["RestingHours"] = 12
    dict[soldier]["Tapuz"] += 1
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


def returnScore(list_of_soldiers, list_of_doubled):
    score = 0
    list_sg = []
    list_tapuz = []
    for i in range(4, len(list_of_soldiers)):
        if i % 2 == 0: list_sg.append(list_of_soldiers[i])
        else: list_tapuz.append(list_of_soldiers[i])
    list_sg = list_sg + list_tapuz
    for i in range(len(list_sg)):
        if list_sg.count(list_sg[i]) > 1:
            if i + 3 < len(list_sg) and (list_sg[i] == list_sg[i+3]):
                score -= 10
            elif i + 4 < len(list_sg) and (list_sg[i] == list_sg[i+4]):
                score -= 7
            elif i + 5 < len(list_sg) and list_sg[i] == list_sg[i+5]:
                score -= 5
            elif i + 6 < len(list_sg) and list_sg[i] == list_sg[i+6]:
                score -= 1
            elif i + 9 < len(list_sg) and list_sg[i] == list_sg[i+9]:
                score -= 10
            elif i + 10 < len(list_sg) and list_sg[i] == list_sg[i+10]:
                score -= 7
            elif i + 11 < len(list_sg) and list_sg[i] == list_sg[i+11]:
                score -= 5
            elif i + 12 < len(list_sg) and list_sg[i] == list_sg[i+12]:
                score -= 1
            else:
                score += 1
    for i in list_of_soldiers[3]:
        if i in list_sg:
            score -= 3
    return score


def checkPerfect(dictToIter, siurimNum, SiurimNumEdit):
    list_to_check = []
    makePerfect = False
    for i in dictToIter:
        num = len(list_to_check)
        if num < 6 and dictToIter[i]["RestingHours"] <= 0 and dictToIter[i]["IsPtorShmirah"] == False:
            list_to_check.append(i)
        elif 12 > num >= 6 and dictToIter[i]["RestingHours"] <= 0 and dictToIter[i]["IsPtorShmirah"] == False:
            list_to_check.append(i)
        elif 12 <= num < 13 and dictToIter[i]["RestingHours"] <= 0 and exampleSiur(dictToIter, siurimNum, SiurimNumEdit,
                                                                                   list_to_check) != []:
            list_to_check.append(exampleSiur(dictToIter, siurimNum, SiurimNumEdit, list_to_check))
        elif 13 <= num < 15 and dictToIter[i]["RestingHours"] <= 0 and dictToIter[i]["IsPtorMitbach"] == False and \
                dictToIter[i]["MitbahCooldown"] <= 0 and i not in list_to_check[12]:
            list_to_check.append(i)
        elif 15 <= num <= 16 and dictToIter[i]["RestingHours"] <= 0 and dictToIter[i]["IsHamal"] == True and i not in \
                list_to_check[12]:
            list_to_check.append(i)
        elif num >= 16 and dictToIter[i]["RestingHours"] <= 0:
            list_to_check.append(i)
    if len(list_to_check) >= 16:
        makePerfect = True
    return makePerfect


def cycle2(dict, siurimNum, SiurimNumEdit, makePerfect, attempts, sevev, inactive):
    dict1 = cp.deepcopy(dict)
    for i in inactive:
        if i in dict1:
            dict1.pop(i)
    if sevev == 1: # MP
        if "Lidor" in dict1:
            dict1.pop("Lidor")
        for i in list(dict1):
            if not dict1[i]["IsSevevMP"]:
                dict1.pop(i)
    elif sevev == 2: # smp
        if "Lidor" in dict1:
            dict1.pop("Lidor")
        for i in list(dict1):
            if dict1[i]["IsSevevMP"]:
                dict1.pop(i)
    else:
        pass
    # Mitbah first, then hamal, then siurim and then shmirot
    list_to_check = []
    dictToIter = cp.deepcopy(dict1)
    if not makePerfect:
        try:
            makePerfect = checkPerfect(dictToIter, siurimNum, SiurimNumEdit)
        except Exception as exc:
            print(exc)
    print("Len: {0}".format(len(list_to_check)))
    list_of_soldiers, doubled = computeList(cp.deepcopy(dict1), siurimNum, SiurimNumEdit, sevev)
    best_attempt = []
    best_points = -999
    best_dict = {}
    if makePerfect and doubled:
        print("Making perfect shavtzak.")
        while doubled != [] and attempts > 0:
            dict2 = cp.deepcopy(dict1)
            list_of_soldiers, doubled = computeList(dict2, siurimNum, SiurimNumEdit, sevev)
            print(attempts)
            attempts -= 1
    elif not makePerfect:
        while attempts > 0:
            dict2 = cp.deepcopy(dict1)
            list_of_soldiers, doubled = computeList(dict2, siurimNum, SiurimNumEdit, sevev)
            temp_score = returnScore(list_of_soldiers, doubled)
            if temp_score > best_points:
                best_attempt = list_of_soldiers
                best_points = temp_score
                best_dict = cp.deepcopy(dict2)
            attempts -= 1
    print(best_attempt)
    print(best_points)
    print("Made shavtzak.")
    if best_attempt == []:
        best_attempt = list_of_soldiers
    excel_file, x = makeExcel2(best_attempt, siurimNum, SiurimNumEdit) # make the new excel shavtzak file
    os.startfile(excel_file + ".xls")
    rewriteExcel(best_dict)  # upload the information to the original excel file and update the information on it


def computeList(dict, siurimNum, SiurimNumEdit, sevev):
    list_of_soldiers = []
    hamal_list = []
    siurim_list = []
    dict2 = dict.copy()

    mitbah, dict2 = doMitbah2(dict2, siurimNum)
    for i in mitbah:
        list_of_soldiers.append(i)
    for j in range(3):
        hamal, dict2 = doHamal2(dict2, SiurimNumEdit, siurimNum)
        hamal_list.append(hamal)
        for i in dict2:
            if dict2[i]["RestingHours"] > 0:
                dict2[i]["RestingHours"] -= 4  # so they can do other missions other than hamal
    for j in range(siurimNum):
        siur, dict2 = doSiur2(dict2, siurimNum, SiurimNumEdit)
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
        for j in dict2:
            if dict2[j]["RestingHours"] > 0:
                dict2[j]["RestingHours"] -= 4
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
