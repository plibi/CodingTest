import sys
input = sys.stdin.readline

# move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# def bfs(x, y):
#     q = [(x, y)]
#     field[x][y] = 0
#     while q:
#         x, y = q.pop(0)
#         for a, b in move:
#             mov_x = x + a
#             mov_y = y + b
#             print('-----')
#             print(mov_x, mov_y)
#             if mov_x < 0 or mov_x >= m or mov_y < 0 or mov_y >= n:
#                 continue

#             if field[mov_x][mov_y]:
#                 q.append((mov_x, mov_y))
#                 field[mov_x][mov_y] = 0

#             # if 0 <= mov_x < len(field)-1 and 0 <= mov_y < len(field[0])-1:
#             #     if field[mov_x][mov_y]:
#             #         q.append((mov_x, mov_y))
#             #         field[mov_x][mov_y] = 0
                    
T = int(input())
# for i in range(T):
#     M, N, K = map(int,input().split())
#     matrix = [[0]*(N) for _ in range(M)]
#     cnt = 0

#     for j in range(K):
#         x,y = map(int, input().split())
#         matrix[x][y] = 1
#     print(matrix)
for _ in range(T):
    m, n, k = map(int, input().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for _ in range(k):
        a, b = map(int, input().split())
        field[b][a] = 1
    print(field)
    # for i in range(m):
    #     for j in range(n):
    #         if field[i][j]:
    #             bfs(i,j)
    #             count += 1
    # print(count)