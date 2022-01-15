N = int(input())
M = int(input())
S = input()

P = 'I' + ('OI' * N)
# print(P)
# print(S.count(P))
count = 0

while True:
    if len(S) < len(P):
        break
    if S.startswith(P):
        count += 1
    S = S[1:]

print(count)