limit, result = 10**7, 0
for i in range(2, limit):
    if sum(map(lambda x: int(x)**5, str(i))) == i:
        result += i
print(result)
