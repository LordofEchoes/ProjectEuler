'''
Created on Jun 19, 2019

@author: akuei
'''

import time
start_time = time.time()

primes = [2,3]
count = 4
i = 0
while i != 10001:
    if count not in [count for i in primes if count%i == 0]:
        i += 1
        primes.append(count)
    count += 1
    
print(primes[i-1])
print("%s seconds" %(time.time()-start_time))