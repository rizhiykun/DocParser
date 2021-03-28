import pylightxl as xl
import xlrd
from docx import Document

from func import pathScan, cut


def xlsx(path):
    path = pathScan('xlsx', path)
    exporting_data = []
    xcel_workbook = xl.readxl(fn=path[0])
    for row in xcel_workbook.ws(ws='Sheet1').rows:
        exporting_data.append(row)
    result = []
    for i in range(len(exporting_data)):
        result.append(list(filter(None, exporting_data[i])))

    result = cut(result)
    return result


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
                    exporting_data.append(excel_worksheet.cell_value(row, col))

    exporting_data = cut(exporting_data)

    return exporting_data

def docx(path):
    path = pathScan('docx', path)
    document = Document(*path)
    allText = []

    for i in range(len(document.paragraphs)):
        single_para = document.paragraphs[i]
        for run in single_para.runs:
            allText.append(run.text)

    ex = cut(allText)
    return ex

#print(docx('D:\\docs\\template\\ID\\*'))


#print(xlsx('D:\\docs\\template\\ID\\*'))

#print(xls('D:\\docs\\template\\ID\\*'))
