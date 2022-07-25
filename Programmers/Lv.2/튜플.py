def solution(s):
    answer = []
    temp = s[1:-2].split('},{')
    temp.sort(key = lambda x: len(x))
    # print(temp)
    
    for i in temp:
        if '{' in i:
            i = i.replace('{', '')
        t = i.split(',')
        for j in t:
            if int(j) not in answer:
                answer.append(int(j))
    # print(answer)
    
    return answer