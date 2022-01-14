# Data structure, Hash table
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
name = {}
answer = []
for _ in range(N):
    name[sys.stdin.readline().rstrip()] = 'not H'

for _ in range(M):
    T = sys.stdin.readline().rstrip()
    if name.get(T) == 'not H':
        answer.append(T)

print(len(answer))
answer.sort()
for i in answer:
    print(i)
