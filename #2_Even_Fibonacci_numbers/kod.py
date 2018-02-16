first, second, result = 1, 1, 0
limit = int(input())
while second <= limit:

    if second % 2 == 0:
        result += second

    first, second = second, first+second
print(result)
