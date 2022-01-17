import sys

M = int(sys.stdin.readline().rstrip())

S = set()
for _ in range(M):
    C = sys.stdin.readline().rstrip()

    if C.split()[0] == 'add':
        S.add(C.split()[1])

    elif C.split()[0] == 'remove':
        S.discard(C.split()[1])

    elif C.split()[0] == 'check':
        if C.split()[1] in S:
            print(1)
        else:
            print(0)

    elif C.split()[0] == 'toggle':
        if C.split()[1] in S:
            S.discard(C.split()[1])
        else:
            S.add(C.split()[1])

    elif C.split()[0] == 'all':
        S = set([i for i in range(1, 21)])
    elif C.split()[0] == 'empty':
        S = set()


# S = set([1, 2, 3])
# S.discard(4)
# print(S)