'''
Created on Mar 31, 2016

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