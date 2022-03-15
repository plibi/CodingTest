n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append([int(i) for i in input()])

count = 0
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(x, y):
    q = [(x, y)]
    count = 0
    while q:
        x, y = q.pop(0)
        
        for i, j in move:
            mov_x = x + i
            mov_y = y + j

            if 0 <= mov_x < len(maze) and 0 <= mov_y < len(maze[0]):
                if maze[mov_x][mov_y] == 1:
                    q.append((mov_x, mov_y))
                    maze[mov_x][mov_y] = maze[x][y]+1
                    count += 1
    return maze[n-1][m-1]

print(bfs(0, 0))

