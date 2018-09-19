#!/usr/bin/env python3
# Michael Gates
# 11 September 2018

import dbutils

"""
#1 - Write a Python function that will create a SQLite database with the following columns:
Phone number, of type INTEGER, is the primary key
Name of person, of type TEXT

#2 - Write one example INSERT statement to insert a phone number and the name of a person to the database.
"""

def main():
    dbutils.create_db("database.db")

    name = input("Enter the name to add to the database: ")
    phone = input("Enter the phone number (without dashes) to add to the database: ")

    dbutils.insert("database.db", name, phone)

if __name__ == '__main__':
    main()
