#!/usr/bin/env python3
# Michael Gates
# 18 September 2018

import os
from tkinter import *
import sqlite3


dbFile = 'people.db'

tk = Tk()
tk.title("Phonebook Application")


"""
--------------------
| Phone     | Name |    Phone Number
| INT PRIM  | TEXT |    Individual's Name
--------------------
"""
def dbutils_create_db(file):

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

def dbutils_insert(file, name, phone):
    con = sqlite3.connect(file)
    cursor = con.cursor()
    command = "INSERT INTO people VALUES (\"" + phone + "\", \"" + name + "\");"
    cursor.execute(command)
    con.commit()
    con.close()


def dbutils_find(file, phone):
    con = sqlite3.connect(file)
    cursor = con.cursor()
    command = 'SELECT name FROM people WHERE phone_number = "' + phone + '";'
    cursor.execute(command)
    rows = cursor.fetchall()
    return rows if rows is not None else []

def dbutils_getAll(file):
    con = sqlite3.connect(file)
    cursor = con.cursor()
    command = 'SELECT * FROM people;'
    cursor.execute(command)
    rows = cursor.fetchall()
    return rows if rows is not None else []


"""
MAIN PROGRAM FUNCTION
"""
def main():

    # Create database if it doesn't exist
    if(not os.path.exists(dbFile)):
        dbutils_create_db(dbFile)


    """ DRAW MAIN FRAME BELOW """
    label = Label(tk, text="Select an option from the menu above.")
    label.pack()

    f = Frame(tk, width=200, height=200)
    f.pack()

    close_button = Button(tk, text="Close", command=tk.quit)
    close_button.pack()

    menubar = Menu(tk)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Add New Entry", command=lambda: showAddEntryFrame(f))
    filemenu.add_command(label="Lookup Entry", command=lambda: showLookupEntryFrame(f))
    filemenu.add_command(label="List All Entries", command=lambda: processListAllEntries(f))
    filemenu.add_command(label="Quit", command=tk.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    tk.config(menu=menubar)

    tk.mainloop()


""" Draws the 'add entry' frame """
def showAddEntryFrame(frame):
    clearFrame(frame)

    nameLabel = Label(frame, text="Enter name:")
    nameLabel.pack()
    nameEntry = Entry(frame)
    nameEntry.pack()
    phoneNumberLabel = Label(frame, text="Enter phone number:")
    phoneNumberLabel.pack()
    phoneNumberEntry = Entry(frame)
    phoneNumberEntry.pack()

    b = Button(frame, text="Add Entry", command=lambda: processAddEntry(frame, nameEntry.get(), phoneNumberEntry.get()))
    b.pack()


""" Draws the 'lookup entry' frame """
def showLookupEntryFrame(frame):
    clearFrame(frame)

    phoneLabel = Label(frame, text="Enter phone number to lookup:")
    phoneLabel.pack()
    phoneEntry = Entry(frame)
    phoneEntry.pack()

    b = Button(frame, text="Search", command=lambda: processLookupEntry(frame, phoneEntry.get()))
    b.pack()

def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def processAddEntry(frame, name, phone):
    if(len(name)<1 or len(phone)<10):
        print("Invalid entry.")
        return
    try:
        dbutils_insert(dbFile, name, phone)
        clearFrame(frame)
        print("Added entry for " + name + " => " + phone)
    except Exception as e:
        print("Entry already exists for " + name + " => " + phone)

def processLookupEntry(frame, phone):
    if(len(phone)<10):
        print("Invalid lookup.")
        return

    clearFrame(frame)
    found = dbutils_find(dbFile, phone)

    resultsLabel = Label(frame, text="Search Results for " + phone + ":")
    resultsLabel.pack()
    if(len(found) < 1):
        noResultsLabel = Label(frame, text="No results found.")
        noResultsLabel.pack()
        return
    for f in found:
        if(len(f) < 1):
            continue
        print(f[0])
        l = Label(frame, text=f[0])
        l.pack()


def processListAllEntries(frame):
    clearFrame(frame)
    found = dbutils_getAll(dbFile)

    resultsLabel = Label(frame, text="List of all results:")
    resultsLabel.pack()
    if(len(found) < 1):
        noResultsLabel = Label(frame, text="No results found.")
        noResultsLabel.pack()
        return
    for f in found:
        if(len(f) < 1):
            continue
        print(str(f[0]) + " => " + f[1])
        l = Label(frame, text=str(f[0]) + " => " + f[1])
        l.pack()

if __name__ == "__main__":
    main()
