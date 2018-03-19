def cycle_length(number):

    i = 0
    current = 1000
    dn = {}

    while current:

        if current in dn:
            return i-dn[current]

        dn[current] = i

        current = (current % number) * 1000
        i += 1

    return 0


n = int(input())
result = max((cycle_length(i), i) for i in range(2, n))
print(result[1])
