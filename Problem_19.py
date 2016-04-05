'''
Created on Apr 5, 2016


You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

@author: Anders
'''
year = 1901;
month = 1;
day = 2;
count = 0;
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
for y in range(1901,2001):
    for m in range(1,13):
        if day == 7:
            count +=1;
        if y%4==0:
            days[2]=29;
        else:
            days[2]=28;
        for d in range(0,days[m]):
            day+=1
            if day==8:
                day = 1
print(count)    