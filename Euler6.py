'''
Created on Jun 19, 2019

@author: akuei
'''
squaresum = 0
sumsquare = 0
for i in range(1,101):
    squaresum += i*i
    sumsquare += i
sumsquare = sumsquare*sumsquare
print(sumsquare - squaresum)