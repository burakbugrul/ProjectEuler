result = 0

for i in range(100, 1000):
    for j in range(i, 1000):

        number = i*j

        if number > result and str(number) == str(number)[::-1]:
            result = number

print(result)
