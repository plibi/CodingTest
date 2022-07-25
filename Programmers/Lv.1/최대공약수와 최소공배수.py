import math

def solution(n, m):

    # answer = [math.gcd(n, m), n*m/math.gcd(n, m)]
        #     a = b*q + r
        # gcd(a, b) == gcd(b, r)
    # Euclidean algo
    a, b = max(n, m), min(n, m)
    while b != 0:
        r = a % b
        a = b
        b = r
    answer = [a, n*m/a]
    
    return answer