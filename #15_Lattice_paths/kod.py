from math import factorial


def combination(a, b):
    return factorial(a)//(factorial(a-b) * factorial(b))


n, m = map(int, input().split())
print(combination(n+m, n))
