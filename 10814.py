N = int(input())
members = []

for i in range(N):
    m = input().rstrip().split()
    m.append(i+1)
    members.append(m)
members.sort(key= lambda x:(int(x[0]), x[2]))

for i in members:
    print(i[0], i[1])

    