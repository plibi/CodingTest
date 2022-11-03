# dp[1] = 1
# dp[2] = 2 (1+1, 2)
# dp[3] = 3 (1+1+1, 2+1, 1+2, 3)
# dp[4] = 7 (1+1+1+1, 2+1+1, 1+2+1, 3+1, 1+1+2, 2+2, 1+3)
# dp[n] = dp[n-1] + dp[n-2] + dp[n-3] (n-1에 +1 n-2에 +2 ...)
import sys
input = sys.stdin.readline

t = int(input())
mod = 1000000009

dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = dp[i-1]%mod + dp[i-2]%mod + dp[i-3]%mod

for i in range(t):
    case = int(input())
    print(dp[case]%mod)