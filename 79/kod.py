from collections import defaultdict

in_degree = defaultdict(int)
graph = defaultdict(list)

with open("keylog.txt", "r") as f:
    for line in f.readlines():
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[2])
        in_degree[line[1]] += 1
        in_degree[line[2]] += 1
        if line[0] not in in_degree:
            in_degree[line[0]] = 0

while len(in_degree):
    node = min(in_degree, key=lambda x: in_degree[x])
    for adj in graph[node]:
        in_degree[adj] -= 1
    del in_degree[node]
    del graph[node]
    print(node, end="")
print()
