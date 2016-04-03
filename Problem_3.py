'''
Created on Mar 31, 2016


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

@author: Anders
'''

i = 2
n=600851475143
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i
print(n);