import sys
input = sys.stdin.readline
n, m = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    i.sort()

for t in range(1, n+1):
    if not visited[t]:
        q = [t]
        visited[t] = True
        while q:
            v = q.pop(0)
            for i in graph[v]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
        count += 1
print(count)