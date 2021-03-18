import glob
import re
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

def cut(exporting_data):
    result = [x for x in exporting_data if x]
    result = [re.sub('{{Founder_Name: "', '', i) for i in result]
    result = [re.sub('"}}', '', i) for i in result]
    result = [re.sub('{{INN: "', '', i) for i in result]
    result = [i.lstrip() for i in result]
    result = [i.rstrip() for i in result]

    return result


def pathScan(formt,path):
    a=[]
    files = glob.glob (path)
    for i in range(len(files)):
        if files[i].endswith(formt):
            a.append(files[i])
    return a

