'''
Created on Apr 2, 2016

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

@author: Anders
'''
#Simple permutation problem, requires a combination of 20 rights and 20 downs in some permutation for a total of 40 moves
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(40)/(factorial(20)*factorial(20)))