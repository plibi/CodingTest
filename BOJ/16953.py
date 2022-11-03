from collections import deque

a, b = map(int, input().split())

if a == b:
    print(1)
    exit()

q = deque()
q.append([a, 0])

while q:
    num, t = q.popleft()
    
    num1 = num*2
    num2 = int(str(num) + '1')
    nums = [num1, num2]
    t += 1
    for n in nums:
        if n > b:
            continue
        elif n == b:
            print(t+1)
            exit()
        q.append([n, t])

print(-1)
    