N = int(input())
table = [0] * (N+1)

if N < 3:
    print(N)
else:
    table[1] = 1
    table[2] = 2
    for i in range(3, N+1):
        table[i] = table[i-1] + table[i-2]
    print(table[N] % 10007)
