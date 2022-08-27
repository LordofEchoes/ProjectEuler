'''
Created on Jun 18, 2019

@author: akuei
'''

prime = 600851475143
factors = []
while prime != 1:
    for i in range(2,prime+1):
        if prime%i == 0:
            prime = int(prime/i)
            factors.append(i)
            break
print(factors[len(factors)-1])