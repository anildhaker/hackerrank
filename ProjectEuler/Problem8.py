import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    s = str(num)
    largestProduct = 0

    for i in range(0, len(s) - k):

        product = 1

        for j in range(i, i + k):
            product *= int(s[j: j + 1])

        if product > largestProduct:
            largestProduct = product

    print (largestProduct)