# import sys
# from collections import deque
# input = sys.stdin.readline
# T = int(input())

# for _ in range(T):
#     p = input().rstrip()
#     p = p.replace('RR', '')
#     n = input()
#     temp = input()
#     ls = deque(eval(temp))
#     reverse = 0
#     control = 0
#     for i in p:
#         if i == 'R':
#             reverse += 1
#         else:
#             if ls:
#                 if reverse % 2 == 0:
#                     ls.popleft()
#                 else:
#                     ls.pop()
#             else:
#                 print('error')
#                 control = 1
#                 break
#     if control == 1:
#         continue
#     else:
#         if reverse % 2 == 0:
#             print(list(ls))
#         else:
#             print(list(ls)[::-1])


from collections import deque
import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    p = input().rstrip()
    n = int(input().rstrip())
    ls = input().rstrip()
    l = []
    if n >0:
        l = list(map(int,ls[1:-1].split(',')))
    ans = deque(l)
    p.replace('RR','')
    reverse = 0
    for i in p:
        if i == 'R':
            reverse+=1
        elif i == 'D':
            if len(ans)<1:
                print('error')
                break
            else:
                if reverse%2==0:
                    ans.popleft()
                else:
                    ans.pop()
    else:
        if reverse%2==0:
            print('['+ ','.join(map(str, ans))+']')
        else:
            ans.reverse()
            print('['+ ','.join(map(str, ans))+']')