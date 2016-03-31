'''
Created on Mar 31, 2016

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