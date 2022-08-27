'''
Created on Jun 19, 2019

@author: akuei
'''
numlist = []
multiple = 1
for i in range(2,20):
    num = i
    for j in numlist:
        if num%j == 0:
            num = num/j
    numlist.append(num)
for k in numlist:
    multiple = multiple*k
print(int(multiple))