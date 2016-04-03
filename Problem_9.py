'''
Created on Mar 31, 2016


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

@author: Anders
'''
import math

for i in range(1000):
    for j in range(1000):
        if math.sqrt(i**2+j**2)+i+j==1000:
            print(math.sqrt(i**2+j**2)*i*j)