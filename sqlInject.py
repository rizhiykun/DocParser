import collections
import sqlite3
from file_extraxtor import xls, xlsx, docx

def sync():
    x = xls('D:\\docs\\template\\ID\\*')
    xx = xlsx('D:\\docs\\template\\ID\\*')
    xxx = docx('D:\\docs\\template\\ID\\*')
    return x, xx, xxx


def sqlinject():
    super_dict = collections.defaultdict(set)

    for d in sync:
        for k, v in d.iteritems():
            super_dict[k].add(v)
    print(super_dict)

    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cdb = """ CREATE TABLE IF NOT EXISTS customers(name TEXT, inn INTEGER) """

        for key in x:
            tt = key
            vv = x[key]
            query = """ INSERT INTO customers (name, inn) VALUES(tt, vv) """

        cursor.execute(query)


sqlinject()