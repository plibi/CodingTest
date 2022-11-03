import math
n, m = map(int, input().split())

combi = math.factorial(n) // math.factorial(m) // math.factorial(n-m)
print(combi)