names = list(sorted(map(lambda x: x[1:len(x)-1], input().split(","))))
result = 0

for i in range(len(names)):
    result += sum(map(lambda x: ord(x)-ord('A')+1, names[i])) * (i+1)

print(result)
