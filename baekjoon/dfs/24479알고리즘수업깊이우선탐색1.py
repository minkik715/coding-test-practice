import sys
sys.setrecursionlimit(1000000)

n, m, r = map(int, sys.stdin.readline().rstrip().split())
check = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int,  sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)
count = 1


def dfs(node):
    global count
    check[node] = count
    graph[node].sort()
    for t in graph[node]:
        if not check[t]:
            count += 1
            dfs(t)


dfs(r)

for i in check[1:]:
    print(i)

