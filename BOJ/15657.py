from itertools import combinations_with_replacement
n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
seqs = list(combinations_with_replacement(nums, m))
# print(seqs)
seqs.sort()
for i in seqs:
    print(*i, sep=' ')