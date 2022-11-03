import sys, re

input = sys.stdin.readline
sentence = input().rstrip()

stack = []
check = False
temp = ''
for i in range(len(sentence)):
    if sentence[i] == '<':
        stack.append(temp)
        temp = ''
        check = True
        temp += sentence[i]
    elif sentence[i] == '>':
        check = False
        stack.append(temp + '>')
        temp = ''
    elif check:
        temp += sentence[i]
    elif sentence[i] == ' ':
        if temp:
            stack.append(temp)
            stack.append(' ')
            temp = ''
        else:
            stack.append(' ')
    else:
        temp += sentence[i]

stack.append(temp)

for i in stack:
    if i.startswith('<'):
        print(i, end='')
    else:
        print(i[::-1], end='')
    
