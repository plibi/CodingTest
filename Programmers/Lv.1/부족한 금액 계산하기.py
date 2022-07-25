def solution(price, money, count):
    answer = -1
    
#     total_cost = [price*i for i in range(1, count+1)]
#     answer = sum(total_cost) - money
    
    # 등차수열의 합    
    total_cost = count*(price+price*count) // 2
    answer = total_cost - money     
    
    return answer if answer > 0 else 0