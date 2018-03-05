def d(number):

    i, result = 1, 0

    while i*i < number:
        if number % i == 0:
            result += i + number//i
        i += 1

    if i*i == number:
        result += i

    return result-number


limit, result = 28123, 0
abundant, sums = [], [False]*(limit+1)

for i in range(12, limit):
    if d(i) > i:
        abundant.append(i)

for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        if abundant[i] + abundant[j] < limit:
            sums[abundant[i]+abundant[j]] = True

for i in range(limit):
    if sums[i] == False:
        result += i

print(result)
