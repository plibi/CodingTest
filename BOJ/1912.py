# dp[n]를 n번째까지의 최대합
# dp[n]이 0이 되면 초기화

import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

dp = [-1e9 for _ in range(100001)]
dp[0] = seq[0]

for i in range(1, n):
    if dp[i-1] <= 0:
        dp[i] = seq[i]
    else:
        dp[i] = seq[i] + dp[i-1]

print(max(dp))