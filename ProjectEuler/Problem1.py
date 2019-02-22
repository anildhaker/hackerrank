import sys

# def sum_total(x):
#     total = 0
#     a = (x-1)//3
#     b = (x-1)//5
#     c = (x-1)//15
#     print(a,b,c)
#     print((a/2)*(6+(a-1)*3),(b/2)*(10+(b-1)*5),(c/2)*(30+(c-1)*15))
#     total = (a/2)*(6+(a-1)*3) + (b/2)*(10+(b-1)*5) - (c/2)*(30+(c-1)*15)
#     print(total)
#     return int(total) 

def sum_multiples(n, k):
    # subtract 1 from n, as range is exclusive
    n = (n-1) // k
    return k * n * (n + 1) // 2

def sum_3s_and_5s(n):
    return sum_multiples(n,3) + sum_multiples(n,5) - sum_multiples(n, 15)


t = int(input().strip())
for _ in range(t):
    print(sum_3s_and_5s(int(input())))
