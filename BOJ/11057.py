# dp[2] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 
n = int(input())
mod = 10007

num = [1]*10

for i in range(n-1):
    for j in range(1, 10):
        num[j] += num[j-1]

print(sum(num)%10007)