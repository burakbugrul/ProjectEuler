def collatz(n):

    if n in dn:
        return dn[n]
    if n == 1:
        return 1

    if n & 1:
        dn[n] = collatz(3*n+1) + 1
    else:
        dn[n] = collatz(n >> 1) + 1

    return dn[n]


limit, answer, result = int(input()), 0, 0
dn = {}

for i in range(1, limit+1):
    length = collatz(i)
    if length > result:
        answer, result = i, length

print(answer, result)
