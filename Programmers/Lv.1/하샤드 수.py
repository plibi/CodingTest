def solution(x):
    # test = 0
    # for i in str(x):
    #     test += int(i)
    test = sum([int(i) for i in str(x)])
    return True if x % test == 0 else False