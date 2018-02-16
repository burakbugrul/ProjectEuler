R, C = 20, 20
ar = [list(map(int, input().split())) for _ in range(C)]
result = 0

for i in range(R):
    for j in range(C):
        if i < R-3:
            result = max(result, ar[i][j]*ar[i+1][j]*ar[i+2][j]*ar[i+3][j])
        if j < C-3:
            result = max(result, ar[i][j]*ar[i][j+1]*ar[i][j+2]*ar[i][j+3])
        if i < R-3 and j < C-3:
            result = max(result, ar[i][j]*ar[i+1][j+1]*ar[i+2][j+2]*ar[i+3][j+3])
        if i < R-3 and j > 2:
            result = max(result, ar[i][j]*ar[i+1][j-1]*ar[i+2][j-2]*ar[i+3][j-3])

print(result)
