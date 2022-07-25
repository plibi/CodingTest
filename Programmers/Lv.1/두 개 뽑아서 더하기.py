def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if i != j:
                answer.append(numbers[i]+numbers[j])
    
    return sorted(list(set(answer)))