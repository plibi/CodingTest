import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * 125250
dp[0] = int(input())

t = 0
for i in range(n):
    floor = list(map(int, input().split()))
    t += len(floor)-1
    for j in range(len(floor)):
        if j == 0:
            dp[t+j] = dp[t-len(floor)+1] + floor[j]
        elif j == len(floor)-1:
            dp[t+j] = dp[t-1] + floor[j]
        else:
            dp[t+j] = max(dp[t+j-len(floor)], dp[t+j-len(floor)+1]) + floor[j]
         
print(max(dp[:]))


# DP문제는 점화식 찾는것이 중요
# Binary Tree가 아니라 1씩 증가하는 tree라 인덱싱이 헷갈려 오래걸림
# DP 테이블을 2차원으로 만들어 풀면 더 쉽게 풀 수 있는데
# 기존 방식처럼 풀다가 오기가 생겨 1차원 array로 해결함...