import sys
N, *num = open(0)

answer = [int(i) for i in num]
answer.sort()

for i in answer:
    sys.stdout.write(str(i)+'\n')


# positive = [0] * 1000001 나눠서 
# negative = [0] * 1000000