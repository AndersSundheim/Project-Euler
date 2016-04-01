'''
Created on Mar 31, 2016

@author: Anders
'''
import math
a = list(range(2,105000))
i = 0;
c = 1;
p = 0;
while i<10002:
    if all(x==c or c%x for x in a):
        i+=1
        p=c;
    c+=1
    print(c)
print(p)