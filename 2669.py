area = [[False]*100 for _ in range(100)]
answer = 0

for i in range(4):
    x1, y1, x2, y2 = map(int,input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            area[i][j] = True

for i in area:
    answer += i.count(True)

print(answer)    