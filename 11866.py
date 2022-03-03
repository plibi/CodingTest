from collections import deque
n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
answer = []

while queue:
    queue.rotate(-(k-1))
    answer.append(queue[0])
    queue.popleft()
    
print('<', end='')    
print(*answer, sep=', ', end='')
print('>')