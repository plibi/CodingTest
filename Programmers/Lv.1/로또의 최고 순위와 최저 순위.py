def solution(lottos, win_nums):
    answer = []
    count = 0
    poten = 0
    lottos.sort()
    win_nums.sort()
    # print(lottos)
    # print(win_nums)
    for i in lottos:
        if i != 0:
            if i in win_nums:
                count += 1
        if i == 0:
            poten += 1
    if count != 0:
        answer = [7-count-poten, 7 - count]
    else:
        if poten == 0:
            answer = [6, 6]
        else:
            answer = [1, 6]
    
    return answer