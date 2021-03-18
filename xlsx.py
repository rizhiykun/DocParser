import pylightxl as xl
from func import Convert, pathScan, cut
def xlsx(path):
    path = pathScan('xlsx', path)
    a = []
    exporting_data = []
    xcel_workbook = xl.readxl(fn=path[0])
    #for i in range(len(path)):
    for row in xcel_workbook.ws(ws='Sheet1').rows:
        a.append(row)
    result=[]
    for i in range(len(a)):

        result.append(list(filter(None, cut(a[i]))))
    result = [x for x in result if x != []]
    result = sum(result, [])
    result = Convert(result)
    return result

print(xlsx('D:\\docs\\template\\ID\\*'))


