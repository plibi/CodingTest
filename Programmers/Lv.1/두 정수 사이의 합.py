def solution(a, b):
    a, b = min(a,b), max(a,b)
    
    # answer = [i for i in range(a, b+1)]
    # return sum(answer)
    B = b*(b+1)//2
    A = a*(a-1)//2
    # print(B, A)
    answer = B-A
    
    return answer