'''
Created on Apr 8, 2016


Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

@author: Anders
'''
# a not even
# b = prime    
max = 0;
for i in range(500):
    if i**2>1000:
        max = i;
        break;
b = list(range(2,1001))
#Sieve of Eratosthenes
for i in range(2,max):
    b[:]=[x for x in b if x%i!=0 or x<=i]
print(len(b),"Primes for b")

a = list(range(2,100))

large_a = 0;
large_b = 0;
num_primes = 0;
for a_ in range(-999,999):
    for b_ in b:
        n = 0;
        temp_primes = 0;
        while all(x==((n**2)+a_*n+b_) or ((n**2)+a_*n+b_)%x for x in a):           
            temp_primes+=1
            n+=1
        if temp_primes>num_primes:
            num_primes = temp_primes
            large_a = a_
            large_b = b_
            print("a",a_,"b",b_,"primes",num_primes)
print(num_primes)
