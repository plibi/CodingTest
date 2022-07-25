N = input()

def switch_change(ls):
    for i in range(len(ls)):
        if ls[i] == 1:
            ls[i] = 0
        else:
            ls[i] = 1


switches = list(map(int, input().split()))
num_students = int(input())

for i in range(num_students):
    sex, get = map(int, input().split())
    if sex == 1:
        for j in range(get-1, len(switches), get):
            switches[j] = 1 if switches[j] == 0 else 0
    else:

        i = 0
        while i < min(len(switches)-get, get-1)+1:
            i += 1
            if switches[get-1-i] != switches[get-1+i]:
                switch_change(switches[get-1-i:get-1+i])
                break
            
    
        print(i)
        switch_change(switches[get-1-i:get-1+i])
        

    print(*switches)
                

print(*switches)

