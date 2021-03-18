import xlrd
import re
path = "D:\\docs\\template\\ID\\Book1.xls"

exporting_data = []
excel_workbook = xlrd.open_workbook(path, on_demand=True)
excel_worksheet = excel_workbook.sheet_by_index(0)
number_of_sheets = int(len(excel_workbook.sheet_names()))

for i in range(number_of_sheets):
    excel_worksheet = excel_workbook.sheet_by_index(i)
    for row in range(excel_worksheet.nrows):
        for col in range(excel_worksheet.ncols):
            exporting_data.append(excel_worksheet.cell_value(row,col))
result = [x for x in exporting_data if x]
result = [re.sub('{{Founder_Name: "','',i) for i in result]
result = [re.sub('"}}','',i) for i in result]
result = [re.sub('{{INN: "','',i) for i in result]


def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct


print(Convert(result))
