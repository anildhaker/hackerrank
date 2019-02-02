#!/bin/python3

import os
import sys

def solve(y,n1):
    y=sorted(y)
    v = 0
    prev = 0
    for i, yi in enumerate(y):
        if yi != prev:
            prev = yi
            vi = n1 / (n1 - i)
        v += vi
    return("{:.2f}".format(v))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        y_count = int(input())+1

        y = list(map(int, input().rstrip().split()))

        result = solve(y,y_count)

        fptr.write(''.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
