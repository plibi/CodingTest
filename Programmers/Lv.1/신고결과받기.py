# dictionary 사용
def solution(id_list, report, k):
    rep_list = {}
    
    for user in id_list:
        rep_list[user] = [[], 0, 0]
        
    for rep in set(report):
        user, rep_user = rep.split()
        rep_list[user][0].append(rep_user)
        rep_list[rep_user][1] += 1
    
    for key, val in rep_list.items():
        if val[1] >= k:
            for val in rep_list.values():
                if key in val[0]:
                    val[2] += 1
    
    answer = []
    for user in id_list:
        answer.append(rep_list[user][2])
            
    return answer