def solution(n, arr1, arr2):
    answer = [''] * n
    map1 = [''] * n
    map2 = [''] * n
    
    for i in range(n):
        n1 = arr1[i]
        while n1 >= 1:
            n1, rest = divmod(n1, 2)
            map1[i] += str(rest)
        map1[i] = map1[i].ljust(n, '0')
        n2 = arr2[i]
        while n2 >= 1:
            n2, rest = divmod(n2, 2)
            map2[i] += str(rest)
        map2[i] = map2[i].ljust(n, '0')
        
    for i in range(len(map1)):
        for j in range(len(map1[i])):
            if map1[i][j] == '1' or map2[i][j] == '1':
                answer[i] += '#'
            else:
                answer[i] += ' '
        answer[i] = answer[i][::-1]
        
    return answer

# 다른 사람의 풀이