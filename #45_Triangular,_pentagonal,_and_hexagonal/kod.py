t, p, h = set(), set(), set()
for i in range(100000):
    t.add((i*(i+1)) // 2)
    p.add((i*(3*i-1))//2)
    h.add(i*(2*i-1))
print(t.intersection(p.intersection(h)))