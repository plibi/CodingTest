from itertools import combinations_with_replacement
n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
seqs = list(set(combinations_with_replacement(nums, m)))

seqs.sort()
# print(seqs)
for i in seqs:
    print(*i, sep=' ')