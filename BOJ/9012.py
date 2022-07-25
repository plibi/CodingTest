import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    stack = []
    check = True
    parentheses = input().rstrip()

    for i in parentheses:
        if i == ')':
            if not stack or stack.pop() != '(':
                check = False
                break
        else:
            stack.append('(')
    if stack:
        check = False

    if check:
        print('YES')
    else:
        print('NO')