import sqlite3
import os
from file_extraxtor import xls, xlsx, docx


def sqlinject():
    allData = {**xls(), **xlsx(), **docx()}              #collect all dict`s
    prj_dir = os.path.abspath(os.path.curdir)
    base_name= 'database.db'
    connect = sqlite3.connect(prj_dir + '/' + base_name) #Create dbase if not exist

    with sqlite3.connect(base_name) as connect:
        cursor = connect.cursor()
        cdb = """ CREATE TABLE IF NOT EXISTS customers(name TEXT, inn INTEGER) """
        cursor.execute(cdb)

        for (key, values) in allData.items():
            cursor.execute("INSERT INTO customers (name, inn) VALUES (?, ?)", (key, values))

sqlinject()