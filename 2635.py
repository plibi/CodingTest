# Brute force
N = int(input())
table = []

if N == 1:
    print(4)
    print(1, 1, 0, 1)
elif N == 2:
    print(5)
    print(2, 1, 1, 0, 1)
else:    
    for i in range(N//2+1, N):
        seq = []
        temp_num = N
        temp_i = i
        seq.append(temp_num)
        while temp_num-temp_i >= 0:
            temp_num, temp_i = temp_i, temp_num-temp_i
            seq.append(temp_num)
        temp_num, temp_i = temp_i, temp_num-temp_i
        seq.append(temp_num)
        table.append(seq)

    ans = sorted(table, key=lambda x: len(x))
    print(len(ans[-1]))
    print(*ans[-1])
