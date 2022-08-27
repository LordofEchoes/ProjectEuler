'''
Created on Jun 29, 2019

@author: akuei
'''
import math
import time
start_time = time.time()

#Pythagorean Triplet, a^2 +b^2=c^2 and a + b + c = 1000
#brute force O(N^2)
def func():
    for a in range(1,333):
        for b in range(a,500):
                c = math.sqrt(a**2 + b**2)
                if (a+b+c == 1000):
                    print("a: " + str(a))
                    print("b: " + str(b))
                    print("c: " + str(c))
                    print("Product: " + str(a*b*c))
                    return
func()
print("%s seconds" %(time.time()-start_time))