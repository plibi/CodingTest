import math

# def solution(n):
    # answer = math.sqrt(n).is_integer()
    # return (math.sqrt(n)+1)**2 if math.sqrt(n).is_integer() else -1

def solution(n):
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1