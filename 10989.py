import sys
N = int(sys.stdin.readline().rstrip())
answer = [0]*10001

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    answer[num] += 1

for i in range(len(answer)):
    if answer[i] != 0:
        for j in range(answer[i]):
            print(i)

# 메모리초과
# N, *n = open(0)
# n.sort()
# print(*n, sep='', end='')