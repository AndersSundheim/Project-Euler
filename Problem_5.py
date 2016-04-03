'''
Created on Mar 31, 2016


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

@author: Anders
'''
a = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2]
b = [1,2,3,4,5,6,7,8,9,10]
def check(n,m):
    for x in m:
        if n%x!=0:
            return False;
    return True;
for i in range(1,100000000000000):
    if check(i,a):
        print(i)
        break
    
