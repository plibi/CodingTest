import sys

N = int(sys.stdin.readline())
area = [[False]*100 for _ in range(100)]
answer = 0

for _ in range(N):
    paper_x, paper_y = map(int, sys.stdin.readline().split())

    for i in range(paper_x, paper_x+10):
        for j in range(paper_y, paper_y+10):
            area[i][j] = True

for i in area:
    answer += i.count(True)

print(answer)
