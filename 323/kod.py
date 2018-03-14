result, last = 0, 0
for i in range(1, 10000):
    prob = (1 - 0.5**i)**32
    result += i*(prob-last)
    last = prob
print("{:.10f}".format(result))
