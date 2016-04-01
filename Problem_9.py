'''
Created on Mar 31, 2016

@author: Anders
'''
import math

for i in range(1000):
    for j in range(1000):
        if math.sqrt(i**2+j**2)+i+j==1000:
            print(math.sqrt(i**2+j**2)*i*j)