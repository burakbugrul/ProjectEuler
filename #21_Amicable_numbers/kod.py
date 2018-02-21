def d(number):

    i, result = 1, 0

    while i*i < number:
        if number % i == 0:
            result += i + number//i
        i += 1

    if i*i == number:
        result += i

    return result-number


n, result = int(input()), 0
amicable = [False]*n

for i in range(1, n):
    pair = d(i)
    if d(pair) == i and pair != i:
        amicable[i] = True
        if pair < n:
            amicable[pair] = True

for i in range(1, n):
    if amicable[i]:
        result += i

print(result)
