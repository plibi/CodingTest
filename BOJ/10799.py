import sys
input = sys.stdin.readline

batch = input().rstrip()
steal = []
total = 0

for i in range(len(batch)):
    if batch[i] == '(':
        steal.append('(')
    else:
        if batch[i-1] == '(':
            steal.pop()
            total += len(steal)
        else:
            steal.pop()
            total += 1
            
print(total)