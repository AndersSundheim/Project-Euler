'''
Created on Apr 4, 2016


2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

@author: Anders
'''
#digital sum function
import math
x = 2**1000
sum=0
for n in range(0,int(math.log10(x))+1):
    sum+=( (x%(10**(n+1)))-(x%(10**(n))) )/(10**n)
print(sum)