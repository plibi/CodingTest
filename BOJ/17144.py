import sys
r, c, t = map(int, input().split())

room = []

for i in range(r):
    room.append(list(map(int, input().split())))

cleaner = []
for i in range(r):
    for j in range(c):
        if room[i][j] == -1:
            cleaner.append(i)
            break

def makeRoom(r, c):
    room_sub = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] // 5 >= 1:
                div = room[i][j] // 5
                cnt = 0
                diffusion = [[-1, 0], [0, -1], [1, 0], [0, 1]]
                for x, y in diffusion:
                    try:
                        if 0 <= i+x < r and 0 <= j+y < c:
                            if room[i+x][j+y] != -1:
                                room_sub[i+x][j+y] += div
                                cnt += 1
                    except:
                        continue
                room[i][j] -= div * cnt

    for i in range(r):
        for j in range(c):
            room[i][j] += room_sub[i][j]

    return room

def cleaning(room, x):
    row = len(room)-1 
    col = len(room[0])-1
    for i in range(x-1, 0, -1):
        room[i][0] = room[i-1][0]
    
    for i in range(0, col):
        room[0][i] = room[0][i+1]
    
    for i in range(0, x):
        room[i][col] = room[i+1][col]
    
    for i in range(col, 1, -1):
        room[x][i] = room[x][i-1]
    room[x][1] = 0

    
    for i in range(x+2, row):
        room[i][0] = room[i+1][0]

    for i in range(0, col):
        room[row][i] = room[row][i+1]

    for i in range(row, x+1, -1):
        room[i][col] = room[i-1][col]
    
    for i in range(col, 1, -1):
        room[x+1][i] = room[x+1][i-1]
    room[x+1][1] = 0

    return room
    

result = 0
for i in range(t):
    room = makeRoom(r, c)
    result = cleaning(room, cleaner[0])

# for i in result:
#     print(i)

ans = 0
for i in result:
    ans += sum(i)
print(ans+2)
