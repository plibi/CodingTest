N = int(input())
waiting = list(map(int,input().split()))
waiting.sort()
time = 0

for i in range(len(waiting)):
    time += waiting[-(i+1)] * (i+1)

print(time)