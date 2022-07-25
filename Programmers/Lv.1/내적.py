def solution(a, b):
    answer = 0
    answer = [i*j for i,j in zip(a, b)]
    return sum(answer)