#!/usr/bin/env python3

# Michael Gates
# 5 September 2018

from nums import multiples
from nums import divisible

"""
Create a test.py file that imports everything in the nums package and tests each functions from both modules 3 times.
"""

listA = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
listB = [-9,-6,-3,0,3,6,9]
listC = [-20,-15,-10,-5,0,5,10,15,20]

# multiples tests
print(*multiples.evenMembers(listA))
print(*multiples.evenMembers(listB))
print(*multiples.evenMembers(listC))
print(*multiples.oddMembers(listA))
print(*multiples.oddMembers(listB))
print(*multiples.oddMembers(listC))
print(*multiples.multiplesOfY(listA, 2))
print(*multiples.multiplesOfY(listB, 3))
print(*multiples.multiplesOfY(listC, 10))

# divisible tests
print(divisible.isEven(0))
print(divisible.isEven(1))
print(divisible.isEven(2))
print(divisible.isOdd(0))
print(divisible.isOdd(1))
print(divisible.isOdd(2))
print(divisible.divisibleBy3(0))
print(divisible.divisibleBy3(3))
print(divisible.divisibleBy3(15))
