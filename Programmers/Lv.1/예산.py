def solution(d, budget):

    if len(d) == 1:
        if d[0] > budget:
            return 0
    d.sort()
    for i in range(1, len(d)+1):
        if sum(d[:i]) > budget:
            return i-1
    return len(d)