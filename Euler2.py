'''
Created on Jun 18, 2019

@author: akuei
'''

fiblist = [1, 2]
i = 1
while fiblist[i] < 4000000:
    fiblist.append(fiblist[i] + fiblist[i-1])
    i += 1
print(sum(i for i in fiblist if i%2 == 0))