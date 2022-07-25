# 이중 for문은 시간초과 => 적당한 stack을 만들어서 for문 한번만 돌면서 해결할수 있도록
# stack 리스트에 값이 아니라 인덱스를 저장!! (몇번 본 트릭같다)
# answer 리스트를 -1로 초기화 해주면 

n = int(input())
nums = list(map(int, input().split()))
stack = []
answer = [-1] * n

for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer, sep=' ')