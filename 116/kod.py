n = int(input())
red, green, blue = [1, 1] + [0]*n, [1, 1, 1] + [0]*n, [1, 1, 1, 1] + [0]*n
for i in range(1, n+1):
    if i >= 2:
        red[i] += red[i-2] + red[i-1]
    if i >= 3:
        green[i] += green[i-3] + green[i-1]
    if i >= 4:
        blue[i] += blue[i-4] + blue[i-1]
print(red[n] + green[n] + blue[n] - 3)
