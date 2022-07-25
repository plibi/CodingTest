N = input()
points = list(map(int, input().split()))
temp = sorted(list(set(points)))

for i in points:
    print(temp.index(i), end=' ')
    
# for i in points:
#     answer.append(temp.index(i))
# print(answer)