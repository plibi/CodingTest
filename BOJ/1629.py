# x^(n+m) = x^n * x^m
# (x*y)mod n = (x mod n * y mod n)mod n

a, b, c = map(int, input().split())

def mod(n):
    if n == 1:
        return a % c
    if n % 2 == 0:
        r = mod(n // 2)
        return r * r % c
    else:
        r = mod(n // 2)
        return r * r * a % c

print(mod(b))
