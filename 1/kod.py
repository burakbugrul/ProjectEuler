def sums(n, k):
    return ((n//k * ((n//k)+1))//2)*k


n = int(input()) - 1
print(sums(n, 3) + sums(n, 5) - sums(n, 15))
