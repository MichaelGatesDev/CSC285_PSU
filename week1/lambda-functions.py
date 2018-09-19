#!/usr/bin/env python3

# Michael Gates
# 31 August 2018

myList = [-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

"""
Create a lambda function in conjunction with the built-in map function that will take a list of data and multiply each number by 3.
"""
multipliedByThree = map(lambda x : x * 3, myList)
print('Multiplied by 3: ', *multipliedByThree)

"""
Create a lambda function in conjunction with the built-in filter function that will return all items of a list that are multiples of 3.
"""
multiplesOfThree = filter(lambda x : x % 3 == 0 and x != 0, myList)
print('Multiples of 3: ', *multiplesOfThree)

"""
Create a lambda function on conjunction with the built-in filter function that will return all items of a list that are negative.
"""
negatives = filter(lambda x : x < 0, myList)
print('Negatives: ', *negatives)
