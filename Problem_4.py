'''
Created on Mar 31, 2016


A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

@author: Anders
'''
max = 0;
for i in range(100,999):
    for j in range(100,999):
        a = str(i*j);
        print(a)
        if i*j>max and a==a[::-1]:
            max = i*j;
print(max); 