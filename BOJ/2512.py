import sys
n = int(sys.stdin.readline())
budgets = [int(i) for i in sys.stdin.readline().split()]
m = int(sys.stdin.readline())

start = 1
end = max(budgets)
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in budgets:
        if i >= mid:
            total += mid
        else:
            total += i
    if total <= m:
        start = mid+1
        answer = mid
    else:
        end = mid-1

print(answer)
