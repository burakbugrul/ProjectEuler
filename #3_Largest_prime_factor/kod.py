n = int(input())
tmp, result, i = n, 1, 2

while i*i <= n and tmp != 1:

    if tmp % i == 0:

        result = i

        while tmp % i == 0:
            tmp /= i

    i += 1

if tmp != 1:
    result = max(result, tmp)

print(result)
