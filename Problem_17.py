'''
Created on Apr 4, 2016


If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

@author: Anders
'''
sum = 11;
s = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
d = [0,0,6,6,5,5,5,7,6,6]
h = 7
for x in range(1,1000):
    if x<=19:
        sum+=s[x]
    elif x<=99:
        y = x
        while y%10!=0:
            y-=1;
        sum+=d[int(y/10)]
        sum+=s[x%10]
    else:
        y = x
        while y%100!=0:
            y-=1
        z = x%100;
        o = x%100;
        if z<=19:
            sum+=s[z]
            print(s[z])
        else:
            while z%10!=0:
                z-=1
            sum+=d[int(z/10)]
            sum+=s[o%10]
        sum+=s[int(y/100)]
        sum+=7
        print(7)
        if x%100!=0:
            sum+=3    
            print(3)   
print(sum)