import sys


# def sumSqaured(x):
#     l = (i for i in range(1, x+1))
#     return sum(l)**2


# def squaredSum(x):
#     l = (i**2 for i in range(1, x+1))
#     return sum(l)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # print(sumSqaured(n)-squaredSum(n))
    print((3*(n**4) + 2*(n**3) - 3*(n**2) - 2*n)//12)
