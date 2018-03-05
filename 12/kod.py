def number_of_divisors(n):

    i = 1
    count = 0

    while i*i <= n:

        if n % i == 0:
            count += 2
        if i*i == n:
            count -= 1

        i += 1

    return count


limit = int(input())

i = 1

while number_of_divisors((i*(i+1)) // 2) <= limit:
    i += 1

print(i, (i*(i+1)) // 2, number_of_divisors((i*(i+1)) // 2))
