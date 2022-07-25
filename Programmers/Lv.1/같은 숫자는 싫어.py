def solution(arr):
    # answer = []
    # ans = ''.join(map(str,arr))
    # for i in ans:
    #     print(i)
    #     ans = ans.replace(i+i, i)
    # print(ans)
    # answer = list(map(int, ans))
    
    answer = [arr[0]]
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
    return answer