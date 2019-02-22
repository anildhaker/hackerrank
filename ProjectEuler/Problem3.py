#!/bin/python3

import sys
import math

def prime_factors(n):
    l = []
    while (n%2 == 0):
        l.append(2)
        n = n/2
    
    for i in range(3,int(math.sqrt(n))+1,2):
        while (n%i == 0):
            l.append(i)
            n = n/i
    if n>2:
        l.append(n)
    return (int(max(l)))



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(prime_factors(n))
    