import sys
n, m = map(int, sys.stdin.readline().split())
lengths = [int(i) for i in sys.stdin.readline().split()]

left = 0
right = max(lengths)
answer = 0

while left <= right:
    mid = (left + right) // 2
    total = 0
    for i in lengths:
        if i > mid:
            total += i - mid
    if total < m:
        right = mid - 1
    else:
        answer = mid
        left = mid + 1

print(answer)