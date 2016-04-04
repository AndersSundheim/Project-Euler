'''
Created on Apr 2, 2016


The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

@author: Anders
'''
max = 0
out = 0
for x in range(1,1000000):
    y = x;
    chain = 0;
    while y!=1:
        if y%2==0:
            y/=2;
        else:
            y = (3*y)+1
        chain+=1;
    if chain>max:
        max = chain
        out = x
    print("|Chain ",chain,"|Number ",x,"|")
print(out)