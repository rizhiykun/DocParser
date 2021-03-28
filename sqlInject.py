import collections
import sqlite3
from file_extraxtor import xls, xlsx, docx

a,aa,aaa = xls(),xlsx(),docx()
allData = {**a, **aa, **aaa}

def sqlinject():

    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cdb = """ CREATE TABLE IF NOT EXISTS customers(name TEXT, inn INTEGER) """

        for key in allData:
            tt = key
            vv = allData[key]
            query = """ INSERT INTO customers (name, inn) VALUES(tt, vv) """

        cursor.execute(query)


sqlinject()