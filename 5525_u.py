N = int(input())
M = int(input())
S = input()

P = 'I' + ('OI' * N)

# 50점
count = 0
idx = 0
while True:
    if S.find(P, idx) != -1:
        count += 1
        idx = S.find(P, idx)+1 
    else:
        break
print(count)

# while True:
#     if len(S) < len(P):
#         break
#     if S.startswith(P):
#         count += 1
#     S = S[1:]

# print(count)
