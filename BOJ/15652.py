from itertools import combinations_with_replacement
n, m = map(int, input().split())

nums = [i for i in range(1, n+1)]

seqs = list(combinations_with_replacement(nums, m))
# print(seqs)

for i in seqs:
    print(*i, sep=' ')


def dfs(idx, m):
    ...