import sys

M = int(sys.stdin.readline().rstrip())
S = set()

for _ in range(M):
    C = sys.stdin.readline().rstrip().split()
    if len(C) == 1:
        if C[0] == 'all':
            S = set([i for i in range(1, 21)])
        elif C[0] == 'empty':
            S = set()
    else:
        comm = C[0]
        num = int(C[1])

        if comm == 'add':
            S.add(num)

        elif comm == 'remove':
            S.discard(num)

        elif comm == 'check':
            if num in S:
                print(1)
            else:
                print(0)

        elif comm == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)


#
# import sys

# m = int(sys.stdin.readline())
# s = set([])
# for i in range(m):
#     line = sys.stdin.readline().strip().split()
#     command = line[0]
#     if command == "all":
#         s = set(range(1, 21))
#         continue
#     elif command == "empty":
#         s = set([])
#         continue

#     value = int(line[1])
#     if command == "add" and value not in s:
#         s.add(value)
#     elif command == "check":
#         if value in s:
#             print(1)
#         else:
#             print(0)
#     elif command == "remove" and value in s:
#         s.remove(value)
#     elif command == "toggle":
#         if value in s:
#             s.remove(value)
#         else:
#             s.add(value)