# Dynamic programming

import sys
N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

up_table = [0] * N
up_table[0] = 1
down_table = [0] * N
down_table[0] = 1

for i in range(N-1):
    if seq[i+1] >= seq[i]:
        up_table[i+1] = up_table[i]+1
    else:
        up_table[i+1] = 1
    if seq[i+1] <= seq[i]:
        down_table[i+1] = down_table[i]+1
    else:
        down_table[i+1] = 1

print(max(max(up_table), max(down_table)))

