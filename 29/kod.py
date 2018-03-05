n, m = map(int, input().split())
powers = set()

for i in range(2, n+1):
    for j in range(2, m+1):
        powers.add(i**j)

print(len(powers))
