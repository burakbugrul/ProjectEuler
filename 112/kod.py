def is_bouncy(number):

    ar = (lambda number: [int(x) for i, x in enumerate(number) if i == 0 or number[i - 1] != number[i]])(number)

    for i in range(1, len(ar)-1):
        if ar[i-1] < ar[i] > ar[i+1] or ar[i-1] > ar[i] < ar[i+1]:
            return True

    return False


n, m = map(int, input().split())
i, cnt = 99, 0

while cnt/i != n/m:
    i += 1
    cnt += is_bouncy(str(i))

print(i)
