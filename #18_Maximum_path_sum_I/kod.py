n = int(input())
ar = [list(map(int, input().split())) for _ in range(n)]
for i in range(n-1, 0, -1):
    for j in range(0, len(ar[i])-1):
        ar[i-1][j] += max(ar[i][j], ar[i][j+1])
print(ar[0][0])
