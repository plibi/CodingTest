import sys

N = int(sys.stdin.readline())
files = []
for _ in range(N):
    files.append(sys.stdin.readline().rstrip())

pattern = []
for i in zip(*files):
    if len(set(i)) != 1:
        pattern.append('?')
    else:
        pattern.append(i[0])

print(''.join(pattern).rstrip())
