n = input()
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(len(list(a-b)) + len(list(b-a)))

# 다른 사람의 풀이
# input()
# a = list(input().split())
# b = list(input().split())
# print(2*len(set(a+b)) - (len(a)+len(b)))

# 굳이 int 변환 필요x
# set 연산 최소화