# Brute force, Sorting
import sys
from itertools import combinations

dwarfs = []

for _ in range(9):
    dwarfs.append(int(sys.stdin.readline().rstrip()))

combination = list(combinations(dwarfs, 7))

for i in combination:
    if sum(i) == 100:
        print(*sorted(i), sep='\n')
        break

