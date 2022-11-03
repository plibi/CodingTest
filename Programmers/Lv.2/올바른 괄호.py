def solution(s):
    
    if s[0] == ')':
        return False

    check = []
    for i in s:
        if i == ')':
            if not check or check[-1] == ')':
                return False
            check.pop()
        else:
            check.append(i)
    if check:
        return False
    else:
        return True