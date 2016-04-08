'''
Created on Apr 6, 2016


A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

@author: Anders
'''
p = list(range(0,10))
t = [1,2,3,4]
#print(t[7:3:-1])
for i in range(2,1000001):
    print("Permutation ",i)
    k = 0
    for x in range(0,len(p)-1):
        if p[x]<p[x+1]:
            k = x
    l = 0;
    for y in range(k+1,len(p)):
        if p[y]>p[k]:
            l = y
    p[k],p[l]=p[l],p[k]
    p[k+1:len(p)]=p[len(p)-1:k:-1]
    print(p)