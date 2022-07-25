def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    # print(new_id[-1])
    
    for i in new_id:
        if i.isalnum() or i == '-' or i == '_' or i == '.':
            answer += i
    while '..' in answer:
        answer = answer.replace('..', '.')

    while answer.startswith('.'):
        answer = answer[1:]
    while answer.endswith('.') :
        answer = answer[:-1]

    if answer == '':
        answer = 'a'
            
    answer = answer[:15]
    while answer.endswith('.') :
        answer = answer[:-1]

    while len(answer) < 3:
        answer = answer + answer[-1]

    return answer


# regex를 사용하면 좀 더 간단하게 해결할 수 있을 것 같다
# answer = new_id
# answer를 re.sub()로 바꿔나가면 좋을 것 같음