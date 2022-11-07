def solution(n):
    num = n
    ones = len(bin(n)[2:].replace('0', ''))
    
    while True:
        num += 1
        if len(bin(num)[2:].replace('0','')) == ones:
            break
            
    return num