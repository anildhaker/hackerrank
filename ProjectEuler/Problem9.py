def maxProduct(n):
    product = 1
    for a in range(1,n+1):
        for b in range(a,n+1):
            for c in range(b,n+1):
                if (a**2 + b**2 == c**2 and a + b + c == n):
                    prod = a*b*c
                    if prod > product:
                        product = prod
    if (product == 1):
        return -1
    else:
        return product
            
    

#input1
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(maxProduct(n))