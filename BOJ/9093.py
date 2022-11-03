import sys

input = sys.stdin.readline
n = int(input())

for i in range(n):
    sentence = input().rstrip()
    words = sentence.split()
    answer = ''
    for w in words:
        answer += w[::-1] + ' '
    print(answer.rstrip())