from math import factorial

result, limit = 0, factorial(9)*8

for i in range(3, limit):
    if sum(map(lambda x: factorial(int(x)), str(i))) == i:
        result += i

print(result)
