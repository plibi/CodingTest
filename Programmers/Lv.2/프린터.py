from collections import deque
def solution(priorities, location):
    answer = 0
    temp = []
    for i in range(len(priorities)):
        temp.append((priorities[i], i))
    q = deque(temp)
    
    while 1:
        if q[0][0] == max(q)[0]:
            answer += 1
            if q[0][1] == location:
                return answer
            q.popleft()
        else:
            q.rotate(-1)

# Pass했지만 line 10에서 매번 max(q)를 찾아줘야하니 비효율적인 시간복잡도