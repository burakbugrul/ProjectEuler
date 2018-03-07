def combination(n, k):

    result = 1

    for i in range(k):
        result *= n-i
    for i in range(1, k+1):
        result //= i

    return int(result)


n, answer = int(input()), 99

for i in range(3, n+1):
    answer += combination(i+8, 8) + combination(i+9, 9) - 10

print(answer)
