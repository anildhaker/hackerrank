import sys
# Although this solution is not optimum but it works for a couple of test cases

def isPalindrome(x):
    return (str(x) == str(x)[::-1])

def maxPal(n):
    num = []
    for i in range(999,99,-1):
        for j in range(100,1000,):
            if (isPalindrome(i*j) and (i*j < n)):
                num.append(i*j)
    return max(num)
            
        
    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(maxPal(n))
    