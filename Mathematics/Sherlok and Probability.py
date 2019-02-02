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
        # S.count('1'
        # for j in range(1,n+1):
        #     combos.append((i,j))
        #     if abs(i-j)<=k: 
        #         if s[i-1]=='1' and s[j-1]=='1':
        #             prob.append((i,j))
    # print(len(combos))

    if prob==0: 
        # print(Fraction(0,1))
        # return str(Fraction(0,len(combos)))
        return str(0)+'/'+str(1) 
    # elif len(prob)==1: 
    #     # print(Fraction(0,1))
    #     # return str(Fraction(0,len(combos)))
    #     return str(1)+'/'+str(len(combos)) 
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
