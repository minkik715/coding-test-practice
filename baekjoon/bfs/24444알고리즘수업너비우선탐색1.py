import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().rstrip().split())

check = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)
queue = deque([r])
order = 0
while len(queue) != 0:
    node = queue.popleft()
    if check[node] == 0:
        order += 1
        check[node] = order
        graph[node].sort()
        for i in graph[node]:
            if check[i] == 0:
                queue.append(i)


for i in check[1:]:
    print(i)
