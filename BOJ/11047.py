import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coins = []

for _ in range(N):
    coins.append(int(input()))

count = 0
for i in coins[::-1]:
    count += K // i
    K = K % i

print(count)