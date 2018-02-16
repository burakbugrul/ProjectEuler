def sieve(limit):
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False

    for i in range(2, limit):
        if is_prime[i]:
            yield i
            for j in range(i*i, limit, i):
                is_prime[j] = False


primes = list(sieve(10 ** 6))
print(primes[int(input())-1])
