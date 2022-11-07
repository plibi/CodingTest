def solution(s):
    answer = []
    cnt = 0
    zeros = 0
    while s != '1':
        prev = len(s)
        s = s.replace('0', '')
        aft = len(s)
        s = bin(aft)[2:]
        cnt += 1
        zeros += prev - aft
    answer.append(cnt)
    answer.append(zeros)
    return answer