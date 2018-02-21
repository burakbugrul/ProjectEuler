n, first, second = int(input()), 1, 1
for _ in range(n):
    first, second = second, first+second
print(second)
