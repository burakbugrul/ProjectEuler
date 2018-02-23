n = int(input())
dn = [1] + [0]*n
for i in range(1, n+1):
    if i >= 1:
        dn[i] += dn[i-1]
    if i >= 2:
        dn[i] += dn[i-2]
    if i >= 3:
        dn[i] += dn[i-3]
    if i >= 4:
        dn[i] += dn[i-4]
print(dn[n])
