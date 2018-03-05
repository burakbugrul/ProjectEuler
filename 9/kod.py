n, result = int(input()), 0

for i in range(1, n):

    if (i * i) % (n - i) == 0:
        a, b, c = i, (n - i - ((i * i) // (n - i))) // 2, (n - i + ((i * i) // (n - i))) // 2
        if a * a + b * b == c * c and a + b + c == n and a < b < c:
            result = max(result, a * b * c)

print(result)
