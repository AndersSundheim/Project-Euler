'''
Created on Mar 31, 2016

@author: Anders
'''
sum = 0;
ll = 0;
l = 1;
n=0;
while n<=4000000:
    #print (n);
    n=ll+l;
    ll=l;
    l=n;    
    if(n%2==0):
        sum+=n;
print(sum);