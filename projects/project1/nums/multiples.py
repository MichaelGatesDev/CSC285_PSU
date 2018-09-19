#!/usr/bin/env python3

# Michael Gates
# 31 August 2018

from nums import divisible

"""
evenMembers()
    Takes one list x and returns a new list with even members
oddMembers()
    Takes one list x and returns a new list with odd members
multiplesOfY()
    Takes one list x and one integer y and returns a new list with all its members multiplied by y.
"""

def evenMembers(x):
    return filter(divisible.isEven, x)

def oddMembers(x):
    return filter(divisible.isOdd, x)

def multiplesOfY(x, y):
    return filter(lambda x : x % y == 0, x)
