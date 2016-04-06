'''
Created on Apr 6, 2016

@author: Anders
'''
def factor(num):
    sum = 0
    for i in range(1,int(num/2)+1):
        if num%i==0:
            sum+=i
    return sum
abundant = []
for i in range(12,28124):
    print(i)
    if factor(i)>i:
        abundant.append(i)
print(abundant)
total = 0
sums = []
for index in range(0,len(abundant)):
    for pos in range(index+1,len(abundant)):
        sums.append(abundant[index]+abundant[pos])
    print("Index",index)
    sums.append(abundant[index]*2)
sums = sorted(sums)
newSums = []
newSums.append(sums[0])
newSums
for x in range(1,len(sums)):
    if sums[x-1]!=sums[x]:
        newSums.append(sums[x])
print(len(sums))
print(len(newSums))
for end in range(1,28124):
    #print("Find",end)
    if end not in newSums:
        print("Added",end)
        total+=end
print(total)