'''
Created on Apr 5, 2016


Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

@author: Anders
'''
import re

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
file = open("names.txt")
names = file.read().split(",")
pattern = re.compile("[A-Z]+")
names[:]=[x[pattern.search(x).start():pattern.search(x).end()] for x in names]
names = sorted(names)
def sumName(name):
    sum=0
    for i in range(0,len(name)):
        sum+=letters.index(name[i])+1
    return sum
total = 0
for x in range(0,len(names)):
    total+=(sumName(names[x])*(x+1))
print(total)
print(sumName("COLIN")*938)