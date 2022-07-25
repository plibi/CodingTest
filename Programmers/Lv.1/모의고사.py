def solution(answers):
    answer = []
    number = [0, 0, 0]
    one = [1, 2, 3, 4, 5] * 2001
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1251
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1001
    
    for i in range(len(answers)):
        if answers[i] == one[i]:
            number[0] += 1
        if answers[i] == two[i]:
            number[1] += 1
        if answers[i] == three[i]:
            number[2] += 1
    
    for i in range(len(number)):
        if max(number) == number[i]:
            answer.append(i+1)
            
    return answer