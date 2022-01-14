import sys
N, r, c = map(int, sys.stdin.readline().rstrip().split())

K = (r+1) * (c+1) - 1
print(K)
print(K%4)

