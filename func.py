import glob
import re

"""
Function
"""


def cut(exporting_data):
    # if list have sublists
    if all(isinstance(a, list) for a in exporting_data):
        exporting_data = [item for sublist in exporting_data for item in sublist]

    # cut trash from list
    keys, values, finishedData = [], [], []
    regex = re.compile(r'(\s\S\w+"|\w+ \w+)')

    for i in range(len(exporting_data)):
        finishedData.append(regex.findall(exporting_data[i]))
    cutted = [x for x in finishedData if x]
    flat_list = [item for sublist in cutted for item in sublist]


    # transform to dict
    for i in range(len(flat_list)):

        a = flat_list[i].strip()
        a = a.replace('"','')
        if a.isalnum():
            values.append(a)
        else:
            keys.append(a)
    db = dict(zip(keys, values))
    return db


def pathScan(formt, path):
    # path scaner for files
    gpath = []
    files = glob.glob(path)
    for i in range(len(files)):
        if files[i].endswith(formt):
            gpath.append(files[i])
    return gpath
