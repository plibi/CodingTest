import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dist = [[1e9 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)

for i in range(n):
    dist[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            dist[j][k] = min(dist[j][i]+dist[i][k], dist[j][k])
        

for i in dist:
    for j in i:
        if j == 1e9:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()
