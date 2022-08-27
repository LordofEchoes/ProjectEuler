'''
Created on Jun 18, 2019

@author: akuei
'''

maxNum = 0
for i in range(999):
    for j in range(999):
        num = i*j
        if str(num)[0:3] == str(num)[5:2:-1]:
            if i*j > maxNum:
                maxNum = i*j
print(maxNum)