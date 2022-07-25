import sys
import math

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    wear = {}
    for _ in range(N):
        cloth, W = sys.stdin.readline().rstrip().split()
        if W in wear:
            wear[W] += 1
        else:
            wear[W] = 2
    print(math.prod(list(wear.values())) - 1)