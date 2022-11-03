import sys
input = sys.stdin.readline

n = int(input())

dp = [[0, 0, 0] for _ in range(n)]

# r g b
# r b g
# g r b
# g b r
# b r g
# b g r
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))
# print(cost)

dp[0] = [cost[0][0], cost[0][1], cost[0][2]]

for i in range(1, n):
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])
# print(dp)

print(min(dp[-1]))


    
