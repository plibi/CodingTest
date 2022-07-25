def solution(sizes):
    w = []
    h = []
    
    for i, j in sizes:
        w.append(i)
        h.append(j)
        
    for i in range(len(sizes)):
        if max(w) >= max(h):
            max_idx = h.index(max(h))
            if h[max_idx] > w[max_idx]:
                temp = h[h.index(max(h))]
                h[max_idx] = w[max_idx]
                w[max_idx] = temp
            else:
                break
                
        elif max(w) < max(h):
            max_idx = w.index(max(w))
            if w[max_idx] > h[max_idx]:
                temp = w[w.index(max(w))]
                w[max_idx] = h[max_idx]
                h[max_idx] = temp
            else:
                break
    
    return max(w) * max(h)

# 다른 사람의 풀이
# return max(max(x) for x in sizes) * max(min(x) for x in sizes)

# print([max(x) for x in sizes])
# print([min(x) for x in sizes])
# [60, 70, 60, 80]
# [50, 30, 30, 40]