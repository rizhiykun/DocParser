from file_extraxtor import xls, xlsx, docx
x = xls('D:\\docs\\template\\ID\\*')
xx = xlsx('D:\\docs\\template\\ID\\*')
xxx = docx('D:\\docs\\template\\ID\\*')
for key in x:
    kk = key,
    vv= x[key]
    print(kk, vv)