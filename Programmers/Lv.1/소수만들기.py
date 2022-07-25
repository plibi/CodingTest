from itertools import combinations

def solution(nums):
    answer = []
    s = list(combinations(nums, 3))
    for i in range(len(s)):
        answer.append(sum(s[i]))
    
    # check the prime number
    answer.sort()
    sol = []
    check = 0
    # print(answer)
    for i in answer:
        for j in range(2, i):
            if i % j == 0:
                check = 1
                print(i)
                break
        if check == 0:
            sol.append(i)
        check = 0
    # print(sol)
    
    return len(sol)


# combinations as cb 로 줄이면 좋을 것 같다