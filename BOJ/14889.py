import sys
input = sys.stdin.readline

from itertools import combinations
n = int(input())
player = [i for i in range(n)]
start = list(combinations(player, n//2))
link = []
for i in start:
    link.append(tuple(set(player) - set(i)))

print(start)
print(link)

power = []
for i in range(n):
    line = list(map(int, input().split()))
    power.append(line)
print(power)

power_gap = []
for i in range(len(start)):
    s_team = power[start[i][0]][start[i][1]] + power[start[i][1]][start[i][0]]
    l_team = power[link[i][0]][link[i][1]] + power[link[i][1]][link[i][0]]
    gap = abs(s_team - l_team)
    power_gap.append(gap)

print(power_gap)
print(min(power_gap))