'''
Created on Mar 31, 2016


The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

@author: Anders
'''
max = 0;
for i in range(1000000):
    if i**2>2000000:
        max = i;
        break;
all = list(range(2,2000001))
#Sieve of Eratosthenes in a couple lines
b = list(range(2,31))
for i in range(2,max):
    all[:]=[x for x in all if x%i!=0 or x<=i]
out = 0;
for i in all:
    out+=i;
print(out)