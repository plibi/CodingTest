# dp[1] = 1
# dp[2] = 2: 2번 카드 1개, 1번 카드 2개를 쓰는 것 중 큰 수 이다.
# dp[3] = 3: 3번 카드 1개, 1과 dp[2]를 쓰는 것 중 큰 수이다. 여기서 1,1,1로 3을 만드는 경우, 1,2로 3을 만드는 경우는 dp[2]에서 처리가 끝난 것
# dp[n] = n: n번 카드 1개 or 1과 dp[n-1] or dp[2]와 dp[n-2], ..dp[i]와 dp[n-i] 중 max

n = int(input())
prices = list(map(int, input().split()))
prices.insert(0, 0)

dp = [0] * (n+1)
dp[0] = 0
dp[1] = prices[1]
dp[2] = max(prices[2], dp[1] + prices[1])

for i in range(3, n+1):
    dp[i] = prices[i]
    for j in range(1, i):
        dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[-1])
