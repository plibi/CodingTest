# Data structure(linked list)

import sys

N = int(sys.stdin.readline())
nums = sys.stdin.readline().rstrip().split()
order = []

for i in range(len(nums)):
    order.insert(int(nums[i]), str(i+1))

print(' '.join(order[::-1]))
