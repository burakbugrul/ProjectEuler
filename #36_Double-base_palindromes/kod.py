n, result = int(input()), 0
for i in range(n):
    if str(i) == str(i)[::-1] and str(bin(i))[2:] == str(bin(i))[:1:-1]:
        result += i
print(result)
