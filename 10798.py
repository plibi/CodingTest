words = [input() for _ in range(5)]
max_len = max([len(i) for i in words])
temp = []
answer = []

for i in range(max_len):
    temp.append([j[i:i+1] for j in words])
for i in temp:
    answer.append(''.join(i))
    
print(''.join(answer))