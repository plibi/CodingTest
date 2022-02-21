N = int(input())

if N % 5 == 0:
    print(N // 5)
else:
    i = N // 5
    while i >= 0:
        if (N - 5 * i) % 3 == 0:
            print(i+(N - 5 * i)//3)
            exit()
        i -= 1
    if N % 3 == 0:
        print(N//3)
    else:
        print(-1)
            