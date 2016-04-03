'''
Created on Mar 31, 2016


The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

@author: Anders
'''
sum1=0;
for i in range(0,101):
    sum1+=i;
sum1 = sum1**2
sum2=0;
for i in range(0,101):
    sum2+=i**2
print(sum1-sum2)
