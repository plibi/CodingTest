# Data structure, Hash table, Set
import sys

N, M = map(int, sys.stdin.readline().split())
noHear = [sys.stdin.readline().rstrip() for _ in range(N)]
noSee = [sys.stdin.readline().rstrip() for _ in range(M)]
noHearnoSee = list(set(noHear) & set(noSee))
noHearnoSee.sort()
print(len(noHearnoSee))
for i in noHearnoSee:
    print(i)

# 중복된 원소를 찾을 때 합집합을 이용할 수도 있음