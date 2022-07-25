import sys
input = sys.stdin.readline
n = int(input())
grid = []
normal_cnt = 0
blind_cnt = 0

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# 일반사람
def normal(grid, r, c):
    queue = [(r, c)]
    while queue:
        x, y = queue.pop(0)
        color = grid[x][y]
        # 같은곳을 돌지 않기위해 R,G,B -> r,g,b로 변경
        grid[x][y] = color.lower()
        # x, y를 기준으로 move
        for dx, dy in move:
            mov_x = x + dx
            mov_y = y + dy
            # 이동한 범위가 grid를 벗어나지 않는지 체크
            if 0 <= mov_x < len(grid) and 0 <= mov_y < len(grid[0]):
                # 이동한 곳이 R,G,B 대문자이며 같은 색상이면 queue에 append
                if grid[mov_x][mov_y].isupper() and grid[mov_x][mov_y] == color:
                    queue.append((mov_x, mov_y))
                    

def blind(grid, r, c):
    queue = [(r, c)]
    while queue:
        x, y = queue.pop(0)
        color = grid[x][y]
        grid[x][y] = 'N'
        for dx, dy in move:
            mov_x = x + dx
            mov_y = y + dy
            if 0 <= mov_x < len(grid) and 0 <= mov_y < len(grid[0]):
                if grid[mov_x][mov_y].islower() and grid[mov_x][mov_y] == color:
                    queue.append((mov_x, mov_y))
    

for _ in range(n):
    colors = [i for i in input().rstrip()]
    grid.append(colors)

for i in range(n):
    for j in range(n):
        if grid[i][j].isupper():
            normal(grid, i, j)
            normal_cnt += 1

# 색약인 사람은 r == g
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'g':
            grid[i][j] = 'r'

for i in range(n):
    for j in range(n):
        if grid[i][j] != 'N':
            blind(grid, i, j)
            blind_cnt += 1

print(normal_cnt, blind_cnt)