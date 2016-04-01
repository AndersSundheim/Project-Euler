'''
Created on Mar 31, 2016

@author: Anders
'''
max = 0;
for i in range(1000000):
    if i**2>2000000:
        max = i;
        break;
all = list(range(2,2000001))
#for i in range()
b = list(range(2,31))
for i in range(2,max):
    all[:]=[x for x in all if x%i!=0 or x<=i]
out = 0;
for i in all:
    out+=i;
print(out)