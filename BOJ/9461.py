T = int(input())
table = [0] * 101
table[1] = 1
table[2] = 1
table[3] = 1
table[4] = 2
table[5] = 2

for _ in range(T):
    N = int(input())
    if N < 6:
        print(table[N])
    else:
        for i in range(6, N+1):
            table[i] = table[i-1] + table[i-5]
        print(table[N])