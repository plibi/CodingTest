import sys
from itertools import combinations
input = sys.stdin.readline

while 1:
    cnt, *nums = map(int, input().split())

    if cnt == 0:
        break
    
    com = combinations(nums, 6)
    for i in com:
        print(*i, sep=' ')

    print()