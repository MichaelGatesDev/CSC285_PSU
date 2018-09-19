#!/usr/bin/env python3
# Michael Gates
# 11 September 2018

import sqlite3


"""
--------------------
| Phone     | Name |    Phone Number
| INT PRIM  | TEXT |    Individual's Name
--------------------
"""

def create_db(file):

    print("Creating database: " + file)
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


def find(file, phone):
    con = sqlite3.connect(file)
    cursor = con.cursor()
    command = 'SELECT name FROM people WHERE phone_number = "' + phone + '";'
    cursor.execute(command)
    rows = cursor.fetchall()

    for row in rows:
        print("Found user with phone number " + phone + ": " + str(row[0]))

def printAll(file):
    con = sqlite3.connect(file)
    cursor = con.cursor()
    command = 'SELECT * FROM people;'
    cursor.execute(command)
    rows = cursor.fetchall()
    print("List of all people/numbers:")
    for row in rows:
        print(str(row[0]) + ", " + row[1])
