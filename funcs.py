"""
Returns all avereges
"""
from multiprocessing import shared_memory
from tkinter import Y


def avg(list, index):
    if (index == 4):
        return mitbahAvg(list)
    elif (index == 5):
        return hamalAvg(list)
    return sum(list, index) / len(list)

def mitbahAvg(list):
    sum, canMit = mitbahSum(list)
    return sum / canMit

def hamalAvg(list):
    sum, qualified = hamalSum(list)
    return sum / qualified

"""
Returns all sums
"""
def sum(list, index):
    if (index == 4):
        return mitbahSum(list)
    elif (index == 5):
        return hamalSum(list)
    
    sum = 0
    for i in range(len(list)):
        sum += list[i][index]
    return sum

def mitbahSum(list):
    sum = 0
    canMit = 0
    for i in range(len(list)):
        if (not list[i][6]): # Doesn't have ptor
            sum += list[i][4]
            canMit += 1
    return (sum, canMit)

def hamalSum(list):
    sum = 0
    qualified = 0
    for i in range(len(list)):
        if (list[i][8]): # Hamal qualified
            sum += list[i][5]
            qualified += 1
    return(sum, qualified)

"""
Returns Lists of higher than averge names
"""
def higherAvg(list, index):
    l = []
    averege = avg(list, index)
    for i in range (len(list)):
        if (list[i][index] > averege):
            l.append(list[i])
    return l

def sortBy(list, index):
    for i in range (len(list)):
        for j in range (len(list)):
            if (list[i][index] < list[j][index]):
                list[i], list[j] = list[j], list[i]

def createDict(list, index):
    dict = {}
    for soldier in list:
        dict.update({soldier[0]: soldier[index]})
    return dict

def listToDict(soldiers):
    """This function will convert the list that we exctract from excel to a dict that's easier to work for."""
    titles = soldiers[0]
    soldiers.remove(soldiers[0])
    dict = {}
    for i in range(len(soldiers)):
        temp = {}
        for j in range(1, len(soldiers[i])):
            temp.update({titles[j] : soldiers[i][j]})
        dict.update({soldiers[i][0] : temp})
    return dict
        
    
def cycle(list, cycleNum):
    """TODO: create the function that is called upon 6 times in order to build the shavtzak. the function receives the list
    of soldiers and builds each "phase" of the shavtzak according to the cycleNum when called. this is the annoying function
    that will be very annoying to write.
    Check for highest SG, Nishkia, siur and so on... Lastly place SG and Nishkia
    """
    highest = 0
    soldier = []
    final_list = []
    #Mitbah
    
    #Siur
    #Hamal
    #Nishkia
    #SG
    
    for i in list:
        if i[1] > highest and i[10] <= 0:
            soldier, highest = i, i[1]
    return soldier, highest