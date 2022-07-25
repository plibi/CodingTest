def solution(arr1, arr2):
    temp = []
    for i in range(len(arr1)):
        temp2 = []
        for j in zip(arr1[i], arr2[i]):
            temp2.append(sum(j))
        temp.append(temp2)
            # print(sum(j))
            
        # temp.append(sum(i))
        
    # 이중루프    
    # temp = []
    # for i in range(len(arr1)):
    #     temp2 = []
    #     for j in range(len(arr1[i])):
    #         temp2.append(arr1[i][j]+arr2[i][j])
    #     temp.append(temp2)
    # print(temp)
    
    return temp