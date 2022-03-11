n, m = map(int, input().split())
maze = []
visited = [[False for _ in range(m)] for j in range(n)]
for _ in range(n):
    maze.append([int(i) for i in input()])


print(visited)