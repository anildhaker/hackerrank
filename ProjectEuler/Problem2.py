def sum_even_fib(x):
    a, b = 1, 1
    total = 0
    while a <=x:
        if a % 2 == 0:
            total += a
        a, b = b, a+b  
    return total

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_even_fib(n))
    
