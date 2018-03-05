n = int(input())
dn = [1] + [0]*n
for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
    for i in range(n-coin+1):
        dn[i+coin] += dn[i]
print(dn[n])
