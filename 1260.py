from collections import deque

N, M, V = map(int, input().split())
graph = [[]]
visited = [False] * 6

def dfs(graph, n, visited):
    visited[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if not visited[i]:  # visited[i]
            dfs(graph, i, visited)

def bfs(graph, n, visited):
    queue = deque([n])
    visited[n] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not graph[i]:
                queue.append(i)
                visited[i] = True

for _ in range(M):
    graph.append(list(map(int, input().split())))

dfs(graph, 1, visited)
visited = [False] * 6
bfs(graph, 1, visited)
