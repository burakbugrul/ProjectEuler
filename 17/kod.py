numbers1 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers10 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
numbers20 = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

result = 0

for i in range(1, 1000):
    if i < 10:
        result += len(numbers1[i])
    elif i < 20:
        result += len(numbers10[i-10])
    elif i < 100:
        result += len(numbers20[i//10]) + (len(numbers1[i % 10]) if i % 10 else 0)
    elif i % 100 == 0 and i < 1000:
        result += len(numbers1[i//100]) + len("hundred")
    elif i - 100*(i//100) < 10:
        result += len(numbers1[i//100]) + len("hundred") + len("and") + len(numbers1[i - 100*(i//100)])
    elif i - 100*(i//100) < 20:
        result += len(numbers1[i//100]) + len("hundred") + len("and") + len(numbers10[i - 100*(i//100) - 10])
    elif i - 100*(i//100) < 100:
        result += len(numbers1[i//100]) + len("hundred") + len("and") + len(numbers20[(i - 100*(i//100)) // 10]) \
                  + (len(numbers1[i % 10]) if i % 10 else 0)

print(result + len("onethousand"))
