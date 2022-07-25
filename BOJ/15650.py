from itertools import permutations, combinations
N, M = map(int, input().split())
num = [i for i in range(1, N+1)]

per = list(combinations(num, M))
per.sort()

for i in per:
    print(*i)