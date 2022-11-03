import sys
input = sys.stdin.readline

n = int(input())
paper = []
for i in range(n):
    line = list(map(int, input().split()))
    paper.append(line)

check_blue = 0
check_white = 0

def findPaper(x, y, N):
    global check_blue, check_white
    check = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if check != paper[i][j]:
                findPaper(x, y, N//2)
                findPaper(x+N//2, y, N//2)
                findPaper(x, y+N//2, N//2)
                findPaper(x+N//2, y+N//2, N//2)
                return
    
    if check == 1:
        check_blue += 1
    else:
        check_white += 1

x = findPaper(0, 0, n)
print(check_white)
print(check_blue)

