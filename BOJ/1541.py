N = input()
temp = N.split('-')
t = []
for i in temp:
    t.append(sum(list(map(int,i.split('+')))))

answer = t[0]
for i in t[1:]:
    answer -= i
print(answer)

