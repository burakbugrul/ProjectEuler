def sieve(limit):
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False

    for i in range(2, limit):
        if is_prime[i]:
            yield i
            for j in range(i*i, limit, i):
                is_prime[j] = False


primes = set(sieve(10000))
start, end = 1000, 10000
for i in range(start, end):
    if i in primes:
        for j in range(1, (end-i)//2):
            if i+j in primes and i+j+j in primes and \
                    sorted(str(i)) == sorted(str(i+j)) and sorted(str(i)) == sorted(str(i+j+j)):
                print(i, i+j, i+j+j)
