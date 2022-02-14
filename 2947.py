# Bubble sort

# order = input().split()

# while order != ['1', '2', '3', '4', '5']:
#     for i in range(len(order)-1):
#         if order[i+1] < order[i]:
#             order[i+1], order[i] = order[i], order[i+1]
#             print(' '.join(order))


order = list(map(int,input().split()))

while order != [1, 2, 3, 4, 5]:
    for i in range(len(order)-1):
        if order[i+1] < order[i]:
            order[i+1], order[i] = order[i], order[i+1]
            print(*order)
