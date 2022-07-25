def solution(n):
    # return list(int(i) for i in str(n))[::-1]
    return list(map(int, str(n)))[::-1]