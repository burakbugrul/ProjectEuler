from math import gcd

n, result = int(input()), 1

for i in range(2, n+1):
    result = (result*i)//gcd(result, i)

print(result)
