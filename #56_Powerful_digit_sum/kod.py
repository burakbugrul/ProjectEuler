n, maximum = int(input()), 0
for i in range(1, n):
    for j in range(1, n):
        maximum = max(maximum, sum(map(int, str(pow(i, j)))))
print(maximum)
