import sys

input = sys.stdin.readline
string = input().rstrip()
n = int(input())
cursor = len(string)

def L(cursor):
    return cursor if cursor == 0 else cursor -1

def D(string, cursor):
    if cursor < len(string):
        return cursor + 1
    else:
        return cursor

def B(string, cursor):
    if cursor != 0:
        string = string[:cursor-1] + string[cursor:]
        return string, cursor - 1
    else:
        return string, cursor

def P(string, cursor, c):
    string = string[:cursor] + c + string[cursor:]
    return string, cursor + 1
 
for i in range(n):
    command = input().rstrip()
    if command == 'L':
        cursor = L(cursor)
    elif command == 'D':
        cursor = D(string, cursor)
    elif command == 'B':
        string, cursor = B(string, cursor)
    else:
        string, cursor = P(string, cursor, command[-1])

print(string)
