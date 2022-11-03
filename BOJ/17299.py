from collections import Counter

n = int(input())
nums = list(map(int, input().split()))
nums_cnt = Counter(nums)

stack = []
answer = [-1] * n

for i in range(n):
    while stack and nums_cnt[nums[i]] > nums_cnt[nums[stack[-1]]]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer)
