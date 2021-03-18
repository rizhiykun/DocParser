import xlrd
from func import Convert, pathScan, cut

def xls(path):
    path = pathScan('xls', path)

    exporting_data = []
    for i in range(len(path)):
        excel_workbook = xlrd.open_workbook(path[i], on_demand=True)
        number_of_sheets = int(len(excel_workbook.sheet_names()))

        for i in range(number_of_sheets):
            excel_worksheet = excel_workbook.sheet_by_index(i)
            for row in range(excel_worksheet.nrows):
                for col in range(excel_worksheet.ncols):
                  exporting_data.append(excel_worksheet.cell_value(row,col))

    result = cut(exporting_data)

    a = Convert(result)
    return a

print(xls('D:\\docs\\template\\ID\\*'))