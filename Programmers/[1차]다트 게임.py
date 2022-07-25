import re

def solution(dartResult):
    condition = '[0-9]+[SDT][*#]?'
    score = re.findall(condition, dartResult)
    # print(score)
    
    answer = []
    for game in range(len(score)):
        num = int(re.findall('[0-9]+', score[game])[0])
        sdt = re.findall('[SDT]', score[game])[0]
        special = re.findall('[*#]+', score[game])
        
        if sdt[0] == 'D':
            num = num ** 2
        elif sdt[0] == 'T':
            num = num ** 3
            
        if special:
            if special[0] == '*#' or special[0] == '#*':
                num = num * (-2)
                if game != 0:
                    answer[game-1] *= 2
            elif special[0] == '#':
                num = num * (-1)
            elif special[0] == '*':
                num *= 2
                if game != 0:
                    answer[game-1] *= 2
                
        answer.append(num)
        
    # print(answer)
    return sum(answer)

# 정규표현식 써서 토큰화