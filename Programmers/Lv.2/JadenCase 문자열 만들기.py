def solution(s):
    answer = ''
    words = s.split(' ')

    for w in words:
        if w:
            w = w.capitalize()
        answer += w + ' '
        
    return answer[:-1]