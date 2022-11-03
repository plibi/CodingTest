# 이전 타일선택에서 아무것도 선택 x, 왼쪽, 오른쪽
# dp[1] = 3 (1 + 1 + 1)
# dp[2] = 7 (1 + 4 + 2)
# dp[3] = 17 (1 + 6 + 8 + 2)
# dp[4] = 41 (1 + 8 +  + ... + 2)

n = int(input())
mod = 9901
dp = [[0, 0, 0] for _ in range(n+1)]
dp[1] = [1, 1, 1]

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0]%mod + dp[i-1][1]%mod + dp[i-1][2]%mod
    dp[i][1] = dp[i-1][0]%mod + dp[i-1][2]%mod
    dp[i][2] = dp[i-1][0]%mod + dp[i-1][1]%mod

print(sum(dp[n])%mod)