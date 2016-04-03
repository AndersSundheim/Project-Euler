'''
Created on Mar 31, 2016

@author: Anders
'''

def factors(a):
    f = 0;
    for x in range(1,int(a/2)+1):
        if a%x==0:
            f+=1;
    return f+1;

sum=0;
for i in range(1,1000000):
    sum+=i;
    if sum%2==0 and sum%3==0 and sum%7==0 and sum%5==0 and sum%13==0 and sum%17==0:
        r = factors(sum)
        print(sum," ",r," ",i)
    else:
        r = 2;   
    if r>=500:
        print(i)
        break