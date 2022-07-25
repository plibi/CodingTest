import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cnt = 0
str_dict = {}

for i in range(n):
    str_in = input()
    str_dict[str_in] = 1

for i in range(m):
    str_check = input()
    if str_check in str_dict:
        cnt += 1

print(cnt)
