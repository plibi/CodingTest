n = int(input())
cards = [int(i) for i in input().split()]
dict1 = {}
for i in cards:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
m = int(input())
find = [int(i) for i in input().split()]

for i in find:
    print(dict1.get(i, 0), end=' ')