n = int(input())
ar = [[0]*(n+3) for _ in range(n+3)]
i, j, number, result = (n+1)//2, (n+1)//2, 1, 0

while number <= n*n:
    
    ar[i][j] = number

    if i == j or i+j == n+1:
        result += number

    number += 1

    u, r, d, l = ar[i-1][j], ar[i][j+1], ar[i+1][j], ar[i][j-1]

    if (d and not r) or not (u | r | d | l):
        j += 1
    elif l and not d:
        i += 1
    elif u and not l:
        j -= 1
    elif r and not u:
        i -= 1

print(result)
