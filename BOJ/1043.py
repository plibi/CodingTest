import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = set(input().split()[1:])
# print(k)

parties = []
for i in range(m):
    parties.append(set(input().split()[1:]))
# print(parties)


for _ in range(m):
    for party in parties:
        if party & k:
            k = k.union(party)

cnt = 0
for party in parties:
    if party & k:
        continue
    cnt += 1

print(cnt)
        