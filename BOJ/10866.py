import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
de = deque()

for _ in range(N):
    command = input().split()
    if command[0] == 'push_front':
        de.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        de.append(int(command[1]))
    elif command[0] == 'pop_front':
        print(de.popleft() if de else -1)
    elif command[0] == 'pop_back':
        print(de.pop() if de else -1)
    elif command[0] == 'size':
        print(len(de))
    elif command[0] == 'empty':
        print(0 if de else 1)
    elif command[0] == 'front':
        print(de[0] if de else -1)
    else:
        print(de[-1] if de else -1)
