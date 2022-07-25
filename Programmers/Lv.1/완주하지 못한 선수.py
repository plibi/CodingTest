def solution(participant, completion):
    answer = ''
    dict1 = {}
    for i in participant:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
            
    for i in completion:
        dict1[i] -= 1
        
    for key, value in dict1.items():
        if value:
            return key
        
    return participant[0]

# Counter 이용하면 
# from collections import Counter
# def solution(participant, completion):
#     answer = Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]