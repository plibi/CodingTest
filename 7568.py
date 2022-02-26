import sys
input = sys.stdin.readline
N = int(input())

weights = []
answer = []

for _ in range(N):
    x, y = map(int, input().rstrip().split())
    weights.append((x, y))

for i in range(len(weights)):
    rank = 1
    for j in range(len(weights)):
        if i == j:
            continue
        if weights[i][0] < weights[j][0] and weights[i][1] < weights[j][1]:
            rank += 1
    answer.append(rank)

print(*answer)

