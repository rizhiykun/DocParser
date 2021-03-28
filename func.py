import glob
import re

"""
Functions
"""


def cut(exporting_data):
    keys, values, finishedData = [], [], []

    # if list have sublists
    if all(isinstance(a, list) for a in exporting_data):
        exporting_data = [item for sublist in exporting_data for item in sublist]  #delete all sublists

    # cut trash from list
    regex = re.compile(r'(\s\S\w+"|\w+ \w+)')                      #search template

    for i in range(len(exporting_data)):
        finishedData.append(regex.findall(exporting_data[i]))      #found all data
    cutted = [x for x in finishedData if x]                        #clean clear sublist
    flat_list = [item for sublist in cutted for item in sublist]   #delete all sublists


    # transform to dict
    for i in range(len(flat_list)):

        a = flat_list[i].strip()
        a = a.replace('"','')        #clear all "
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
