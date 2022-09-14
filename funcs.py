from multiprocessing import shared_memory
from tkinter import Y


def avg(dict, key):
    avg = 0
    for i in dict:
        avg += dict[i][key]
    return avg/len(dict)


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


def cycle(list, cycleNum):
    """TODO: create the function that is called upon 6 times in order to build the shavtzak. the function receives the list
    of soldiers and builds each "phase" of the shavtzak according to the cycleNum when called. this is the annoying function
    that will be very annoying to write.
    Check for highest SG, Nishkia, siur and so on... Lastly place SG and Nishkia
    """
    highest = 0
    soldier = []
    final_list = []
    # Mitbah

    # Siur
    # Hamal
    # Nishkia
    # SG

    for i in list:
        if i[1] > highest and i[10] <= 0:
            soldier, highest = i, i[1]
    return soldier, highest
