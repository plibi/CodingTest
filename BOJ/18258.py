from collections import deque
import sys
N = int(sys.stdin.readline().rstrip())
queue = deque([])

for _ in range(N):
    command = sys.stdin.readline().rstrip().split()

    if len(command) == 2:
        queue.append(int(command[1]))
    else:
        if command[0] == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif command[0] == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        else:
            if queue:
                print(queue[-1])
            else:
                print(-1)
