#!/bin/python3

import os
import sys
from fractions import Fraction

# Complete the solve function below.
def solve(n,k,s): 
    s = str(s)
    n = len(s)
    combos = n*n
    prob = 0
    for i in range(n):
        if s[i]=='1':
            prob += s.count('1',max(0,i-k),min(n,i+k+1))
        

    if prob==0: 
        return str(0)+'/'+str(1) 
    
    else: 
        if prob==combos:
            return str(1)+'/'+str(1)
        # print(Fraction(len(prob),len(combos)))
        return str(Fraction(prob,combos))
        # return str(len(prob))+'/'+str(len(combos))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        s = input()

        result = solve(n, k, s)

        fptr.write(result + '\n')

    fptr.close()
