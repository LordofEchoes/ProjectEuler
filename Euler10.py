'''
Created on Jun 29, 2019

@author: akuei
'''

import time
start_time = time.time()

primes = [2,3]
count = 4
while sum(primes) < 2000000:
    if count not in [count for i in primes if count%i == 0]:
        primes.append(count)
    count += 1
    
print(sum(primes))
print("%s seconds" %(time.time()-start_time))