# BOJ_11052와 같은 접근

n = int(input())
prices = list(map(int, input().split()))
prices.insert(0, 0)

dp = [0] * (n+1)
dp[0] = 0
dp[1] = prices[1]
dp[2] = min(prices[2], dp[1] + prices[1])

for i in range(3, n+1):
    dp[i] = prices[i]
    for j in range(1, i):
        dp[i] = min(dp[i], dp[j] + dp[i-j])

print(dp[-1])
