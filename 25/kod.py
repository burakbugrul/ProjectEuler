first, second, index = 1, 1, 2

while len(str(second)) < 1000:
    first, second, index = second, first+second, index+1

print(index)