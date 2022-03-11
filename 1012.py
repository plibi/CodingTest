import sys
input = sys.stdin.readline

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(x, y):
    q = [(x, y)]
    field[x][y] = 0
    while q:
        x, y = q.pop(0)
        for a, b in move:
            mov_x = x + a
            mov_y = y + b
            if mov_x < 0 or mov_x >= n or mov_y < 0 or mov_y >= m:
                continue

            if field[mov_x][mov_y]:
                q.append((mov_x, mov_y))
                field[mov_x][mov_y] = 0

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for _ in range(k):
        a, b = map(int, input().split())
        field[b][a] = 1
    
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j]:
                bfs(i,j)
                count += 1
    print(count)