# 앞의 숫자가 0,
# 앞의 숫자가 1~8,
# 앞의 숫자가 9일때로 나눠서 생각
n = int(input())

dp = [[0 for _ in range(10)] for _ in range(101)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]
mod = 1000000000

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1] % mod
        elif j == 9:
            dp[i][j] = dp[i-1][8] % mod
        else:
            dp[i][j] = dp[i-1][j-1] % mod + dp[i-1][j+1] % mod

print(sum(dp[n]) % mod)