import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
memo = {}

for _ in range(N):
    url, password = sys.stdin.readline().rstrip().split()
    memo[url] = password

for _ in range(M):
    print(memo[sys.stdin.readline().rstrip()])