#!/usr/bin/env python3
# Michael Gates
# 11 September 2018

import sqlite3



def create_db(file):

    con = sqlite3.connect(file)
    cursor = con.cursor()

    command = """CREATE TABLE IF NOT EXISTS people (
    phone_number INTEGER PRIMARY KEY,
    name TEXT
    );
    """

    cursor.execute(command)
    con.commit()
    con.close()
    print("Created database " + file)

def insert(file, name, phone):
    con = sqlite3.connect(file)
    cursor = con.cursor()

    command = "INSERT INTO people VALUES (\"" + phone + "\", \"" + name + "\");"

    cursor.execute(command)
    con.commit()
    con.close()
    print("Inserted data into database.")
