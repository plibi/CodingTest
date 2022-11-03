import sys
input = sys.stdin.readline

n, m, blocks = map(int, input().split())
ground = []

for i in range(n):
    line = list(map(int, input().split()))
    ground.append(line)

min_time = 1e9
height = 0
for i in range(257):
    used_block = 0
    take_block = 0

    for x in range(n):
        for y in range(m):
            if ground[x][y] > i:
                take_block += ground[x][y] - i
            else:
                used_block += i - ground[x][y]
    
    b = blocks + take_block
    if used_block > b:
        continue

    t = take_block*2 + used_block
    if t <= min_time:
        min_time = t
        height = i

print(min_time, height)