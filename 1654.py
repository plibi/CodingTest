import sys
n, m = map(int, sys.stdin.readline().split())
lengths = [int(sys.stdin.readline()) for _ in range(n)]

left = 1        # ZeroDivisionError
right = max(lengths)
answer = 0

while left <= right:
    mid = (left + right) // 2
    quantity = 0
    for i in lengths:   
        quantity += i // mid        # i > mid일 필요x

    if quantity < m:
        right = mid - 1
    else:
        answer = mid
        left = mid + 1

print(answer)