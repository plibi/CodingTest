import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

t = list(map(int, input().split()))

dist = [[1e9 for _ in range(n)] for _ in range(n)]
for i in range(r):
    a, b, l = map(int, input().split())

    dist[a-1][b-1] = l
    dist[b-1][a-1] = l

for i in range(n):
    dist[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if dist[j][k] > dist[j][i] + dist[i][k]:
                dist[j][k] = dist[j][i] + dist[i][k]

# for i in dist:
#     print(i)

max_item = 0
for i in range(n):
    temp = 0
    for j in range(n):
        if dist[i][j] <= m:
            temp += t[j]
    if temp > max_item:
        max_item = temp

print(max_item)

