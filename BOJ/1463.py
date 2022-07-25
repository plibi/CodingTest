# Dynamic Programming
import sys

N = int(sys.stdin.readline().rstrip())

table = [0] * 1000001
table[1] = 0
table[2] = 1
table[3] = 1
table[4] = 2


for i in range(5, 1000001):
    a, b = 100000, 100000
    if i % 3 == 0:
        a = table[i//3]
    if i % 2 == 0:
        b = table[i//2]

    table[i] = min(a, b, table[i-1]) + 1

print(table[N])
