V = int(input())
E = int(input())
graph = [[] for _ in range(V+1)]

def dfs(graph, n, visited):
    visited[n] = 1
    for i in graph[n]:
        if not visited[i]:
            dfs(graph, i, visited)

for _ in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for i in graph:
    i.sort()


visited = [0]*(V+1)
dfs(graph, 1, visited)
print(sum(visited)-1)