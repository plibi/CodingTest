from itertools import permutations
N, M = map(int, input().split())
num = [int(i) for i in input().split()]
per = list(permutations(num, M))
per.sort()
for i in per:
    print(*i)