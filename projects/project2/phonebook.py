#!/usr/bin/env python3
# Michael Gates
# 11 September 2018



"""
Create a Python application that acts as a Phonebook program. This program has the following requirements:

The program prints a menu and gives you the option to add an entry, lookup and entry, print all entries, or quit

Each menu action should be contained in a function, for instance "addEntry", "lookupEntry", and "listEntries" or something similar

The SQLite database can consists of one table, named whatever you like, with two columns, one is a number and the primary key to store the phone number and the other is text and used to store the individuals name
"""

import os
import dbutils

dbFile = 'people.db'

"""
When you add an entry it adds the entry to a SQLite database
"""
def addEntry():
    name = input("Enter the name to add: ").strip()
    number = input("Enter the phone number to add: ").replace('-','')
    print("")
    dbutils.insert(dbFile, name, number)
    doMenu()

"""
When you lookup and entry it gets the entry details from a SQLite database
"""
def lookupEntry():
    lookup = input("Enter the phone number to lookup: ")
    print("")
    try:
        lookup = lookup.replace('-','')
        int(lookup)
    except Exception as e:
        print(e)
        print("You didn't enter a valid number!")
    dbutils.find(dbFile, lookup)
    doMenu()


"""
When you view all entries it gets them from a SQLite database
"""
def printAllEntries():
    dbutils.printAll(dbFile)
    doMenu()

def quit():
    print("Exiting program.")

def doMenu():
    print("")
    print("What would you like to do?")
    print("1) Add an entry")
    print("2) Lookup an entry")
    print("3) Print all entries")
    print("4) Quit")
    choice = input("Enter choice: ")
    print("")

    if(choice == "1"):
        addEntry()
    elif(choice == "2"):
        lookupEntry()
    elif(choice == "3"):
        printAllEntries()
    elif(choice == "4"):
        quit()
    else:
        print("You did not enter a valid choice!")
        doMenu()


def main():
    # Create Database if it doesn't exist
    if not os.path.exists(dbFile):
        dbutils.create_db(dbFile)
    # Show the main GUI
    doMenu()

if __name__ == '__main__':
    main()
