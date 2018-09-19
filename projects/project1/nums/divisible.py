#!/usr/bin/env python3

# Michael Gates
# 31 August 2018

"""
isEven()
    Takes one parameter x and returns true if even, false if not
isOdd()
    Takes one parameter x and returns true if odd, false if not
divisibleBy3()
    Takes one parameter x and returns true if x is divisible by 3, false if not
"""

def isEven(x):
    return x % 2 == 0

def isOdd(x):
    return x % 2 != 0

def divisibleBy3(x):
    return x % 3 == 0
