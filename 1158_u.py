# from collections import deque
# N, K = map(int, input().split())

# josep = deque([i for i in range(1, N+1)])

from bisect import bisect_left, bisect_right

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
find = list(map(int, input().split()))

for i in find:
    print(bisect_right(arr, i) - bisect_left(arr, i), end=' ')