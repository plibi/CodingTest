import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
book = {}

for i in range(N):
    name = sys.stdin.readline().rstrip()
    book[name] = i+1
    book[str(i+1)] = name

for _ in range(M):
    print(book[sys.stdin.readline().rstrip()])