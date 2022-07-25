def solution(nums):
    
    pick = len(nums) // 2
    nums = list(set(nums))
    
    if pick >= len(nums):
        answer = len(nums)
    else:
        answer = pick
    
    return answer

#   return min(len(set(nums)), len(nums)//2)