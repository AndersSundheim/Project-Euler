'''
Created on Apr 5, 2016


n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

@author: Anders
'''
#Combination of 2 previous problems
import math
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
x=factorial(100)
sum=0
for n in range(0,int(math.log10(x))+1):
    sum+=( (x%(10**(n+1)))-(x%(10**(n))) )/(10**n)
print(sum)