# 수열의 i번째 수와 i 이전의 j번째 수들과 비교해서 길이를 dp에 저장
# _ _ _ _ _ i ...
# _ _ j _ _         => seq[i] > seq[j]면 dp[i] = max(dp[i], dp[j]+1)

# 참고 블로그
# https://velog.io/@djagmlrhks3/Algorithm-BaekJoon-11053.-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-by-Python

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