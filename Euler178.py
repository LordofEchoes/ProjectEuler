'''
Created on Jul 17, 2019

@author: akuei
'''


count = 0
i = 3
squares = 0
while i < 1000000:
    squares = i*i-1
    if squares > 1000000:
        if i%2 == 0:
            for j in range(2,i,2):
                squares = i*i - j*j
                if squares < 1000000:
                    count += 1
        else:
            for k in range(1,i,2):
                squares = i*i - k*k
                if squares < 1000000:
                    count += 1
    else:
        if i % 2 == 0:
            count += i/2-1
        else:
            count += (i-1)/2
print(count)