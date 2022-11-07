def solution(s):
    nums = [int(i) for i in s.split()]
    ans = f'{min(nums)} {max(nums)}'
    return ans