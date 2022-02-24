from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def dfs(graph, n, visited):
    visited[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, n, visited):
    queue = deque([n])
    visited[n] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in graph:
    i.sort()

dfs(graph, V, visited)
print()
visited = [False] * (N+1)
bfs(graph, V, visited)
