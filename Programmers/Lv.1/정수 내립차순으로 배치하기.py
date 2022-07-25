def solution(n):
    answer = sorted(str(int(n)))[::-1]
    return int(''.join(answer))

# def solution(n):
#     ls = list(str(n))
#     ls.sort(reverse = True)
#     return int("".join(ls))