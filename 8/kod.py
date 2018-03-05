with open("number.txt", "r") as f:
    number = f.read()

result = 0

for i in range(len(number)-12):

    current = 1

    for j in range(i, i+13):
        current *= int(number[j])

    result = max(result, current)

print(result)