n, m, k = map(int, input().split())
result = [[1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):

        ar = [[0]*m for _ in range(n)]
        ar[i][j] = 1

        for _ in range(k):

            tmp = [[0]*m for _ in range(n)]

            for x in range(n):
                for y in range(m):
                    if 0 < x < n-1 and 0 < y < m-1:
                        tmp[x+1][y] += ar[x][y]/4
                        tmp[x-1][y] += ar[x][y]/4
                        tmp[x][y+1] += ar[x][y]/4
                        tmp[x][y-1] += ar[x][y]/4
                    elif (x == 0 or x == n-1) and (y == 0 or y == m-1):

                        if x == 0:
                            tmp[x+1][y] += ar[x][y]/2
                        else:
                            tmp[x-1][y] += ar[x][y]/2

                        if y == 0:
                            tmp[x][y+1] += ar[x][y]/2
                        else:
                            tmp[x][y-1] += ar[x][y]/2
                    else:
                        if x == 0:
                            tmp[x+1][y] += ar[x][y]/3
                            tmp[x][y+1] += ar[x][y]/3
                            tmp[x][y-1] += ar[x][y]/3
                        elif x == n-1:
                            tmp[x-1][y] += ar[x][y] / 3
                            tmp[x][y+1] += ar[x][y] / 3
                            tmp[x][y-1] += ar[x][y] / 3
                        elif y == 0:
                            tmp[x][y+1] += ar[x][y]/3
                            tmp[x+1][y] += ar[x][y]/3
                            tmp[x-1][y] += ar[x][y]/3
                        elif y == m-1:
                            tmp[x][y-1] += ar[x][y] / 3
                            tmp[x+1][y] += ar[x][y] / 3
                            tmp[x-1][y] += ar[x][y] / 3

            ar = tmp

        for x in range(n):
            for y in range(m):
                result[x][y] *= (1-ar[x][y])

answer = 0

for i in range(n):
    for j in range(m):
        answer += result[i][j]

print("%.6f" % answer)
