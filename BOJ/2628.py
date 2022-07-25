import sys
from itertools import combinations

row, col = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

rows = [0, row]
cols = [0, col]

for _ in range(N):
    cut, num = map(int, sys.stdin.readline().split())
    if cut == 0:
        cols.append(num)
    else:
        rows.append(num)

rows.sort()
cols.sort()
rs = []
cs = []

for i in range(len(rows)-1):
    rs.append(rows[i+1]-rows[i])
for i in range(len(cols)-1):
    cs.append(cols[i+1]-cols[i])

print(max(rs)*max(cs))