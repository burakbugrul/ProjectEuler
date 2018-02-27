def f(index, absent, late):

    if index == n+1:
        return 1

    if dn[index][absent][late] != -1:
        return dn[index][absent][late]

    result = 0

    if late:
        result += f(index+1, 2, 0)
    if absent:
        result += f(index+1, absent-1, late)
    result += f(index+1, 2, late)

    dn[index][absent][late] = result
    return result


n = int(input())
dn = [[[-1]*2 for i in range(3)] for j in range(n+1)]
print(f(1, 2, 1))
