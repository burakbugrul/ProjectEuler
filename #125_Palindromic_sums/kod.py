limit, numbers = int(input()), set()

for i in range(1, limit):
    current = i*i
    for j in range(i+1, limit):
        current += j*j
        if current >= limit:
            break
        if str(current) == str(current)[::-1]:
            numbers.add(current)

print(sum(numbers))
