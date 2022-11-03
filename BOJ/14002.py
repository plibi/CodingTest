import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
dp = [1 for _ in range(1001)]

for i in range(1, n):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

longest_idx = dp.index(max(dp))
value = []
target = max(dp)
for i in range(longest_idx, -1, -1):        # dp를 역순으로 돌면서 dp[i]와 target이 같으면 저장
    if dp[i] == target:
        value.append(seq[i])
        target -= 1
print(*value[::-1])