import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
sub_sum = {0:0}
sub_sum[1] = nums[0]

for i in range(1, N):
    sub_sum[i+1] = sub_sum[i] + nums[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(sub_sum[j] - sub_sum[i-1])


