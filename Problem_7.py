'''
Created on Mar 31, 2016


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

@author: Anders
'''

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