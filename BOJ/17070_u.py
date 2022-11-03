from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
house = []

dp = [[[0] * n for _ in range(n)] for _ in range(3)]
print(dp)

for i in range(n):
    line = list(map(int, input().split()))
    house.append(line)
# print(house)

dp[0][1][0] = 1
print(dp)

for i in range(2, n):
    if house[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for r in range(1, n):
    for c in range(1, n):
        # 현재위치가 대각선인 경우
        if house[r][c] == 0 and house[r][c - 1] == 0 and house[r - 1][c] == 0:
            # dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
            dp[r][c][2] = dp[r - 1][c - 1][0] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

        if house[r][c] == 0:
            # 현재 위치가 가로인 경우
            # dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
            dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
            # 현재 위치가 세로인 경우
            # dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]
            dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]
# print(dp)
for i in dp:
    print(i)
print(sum(dp[i][n - 1][n - 1] for i in range(3)))





# for i in range(n):
#     for j in range(n):
#         house[i][j] = house[i][j-1][0] + house[i-1][j][1] + house[i-1][j-1][2]

# cnt = 0
# for i in range(n):
#     line = list(map(int, input().split()))
#     house.append(line)

# house[0][0] = 1
# house[0][1] = 1

# moves = {
#     'r' : [[0, 1], [1, 1]],
#     'v' : [[1, 0], [1, 1]],
#     'd' : [[0, 1], [1, 0], [1, 1]]
# }

# q = deque()
# q.append(['r', 0, 1])

# while q:
#     # print(q)
#     direction, x, y = q.popleft()
    
#     for m in moves[direction]:
#         dx = x + m[0]
#         dy = y + m[1]
#         if 0 <= dx < n and 0 <= dy < n:
#             # print(dx, dy)
#             if house[dx][dy] == 1:
#                 continue
#             if m == [1, 1]:
#                 if house[dx-1][dy] == 1 or house[dx][dy-1] == 1:
#                     continue
#             if dx == n-1 and dy == n-1:
#                 cnt += 1
#                 continue

#             # house[dx][dy] = 1
#             direc = ''
#             if m == [0, 1]:
#                 direc = 'r'
#             elif m == [1, 0]:
#                 direc = 'v'
#             else:
#                 direc = 'd'
#             q.append([direc, dx, dy])
            
# print(cnt)


