import sys
from functools import reduce
from math import gcd

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = int(reduce(lambda x,y: x*y//gcd(x,y), range(1,n+1)))
    print (result)
    
