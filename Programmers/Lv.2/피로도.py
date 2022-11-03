# 비교적 간단한 완전탐색 문제
from itertools import permutations
def solution(k, dungeons):
    m = 0
    all_case = list(permutations(dungeons, len(dungeons)))
    for i in all_case:
        temp_k = k
        temp_m = 0
        for j in i:
            if temp_k < min(i)[0]:
                break
            if temp_k >= j[0]:
                temp_k = temp_k - j[1]
                temp_m += 1
        if temp_m > m:
            m = temp_m
    return m

# (최소필요피로도 - 소모피로도)가 큰 순으로 정렬해서 해결하려했던 접근은 실패
# dungeons.sort(key=lambda x: (x[0] - x[1]), reverse=True)
# for i in dungeons:
#     if k < min(dungeons)[0]:
#         break
#     if k >= i[0]:
#         k = k - i[1]
#         answer += 1