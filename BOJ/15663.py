from itertools import permutations
n, m = map(int, input().split())

nums = list(map(int, input().split()))
# nums.sort()
combi = list(permutations(nums, m))
combi = list(set(combi))
combi.sort()

for i in combi:
    print(*i, sep=' ')