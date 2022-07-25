def solution(n):
    answer = 0
    ternary = ''
    while n >= 1:
        n, rest = divmod(n, 3)
        ternary += str(rest)
        
    answer = int(ternary, 3)

    return answer


# 진수 변환
# 10진수 -> n진수
# 37 % 2 = 18 * 2 + "1"
# 18 % 2 = 9 * 2 + "0"
# 9 % 2 = 4 * 2 + "1"
# 4 % 2 = 2 * 2 + "0"
# 2 % 2 = 2 * 1 + "0"
# 1 % 2 = 2 * 0 + "1"
# => 37 = 100101_(2)