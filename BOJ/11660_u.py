import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[0] * n for i in range(n)] 

# make table
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if i == 0:
            if j == 0:
                dp[i][j] = line[j]
            else:
                dp[i][j] = dp[i][j-1] + line[j]
        else:
            if j == 0:
                dp[i][j] = dp[i-1][-1] + line[j]
            else:
                dp[i][j] = dp[i][j-1] + line[j]
print(dp)

# find sum
for i in range(m):
    answer = 0
    find = list(map(int, input().split()))

    if find[0]-2 < 0 and find[1]-2 < 0:
        answer = dp[find[2]-1][find[3]-1]
    elif find[1]-2 < 0:
        row = find[0]-1
        col = len(dp)-1
        answer = dp[find[2]-1][find[3]-1] - dp[row][col]
    else:
        row = find[0]-1
        col = find[1]-1
        answer = dp[find[2]-1][find[3]-1] - dp[row][col]
    
    # answer = dp[find[2]-1][find[3]-1] - dp[row][col]
    # if find[0] == find[2] and find[1] == find[3]:
    #     answer = dp[find[0]-1][find[1]-1]

    # else:
    #     for j in range(find[0]-1, find[2]):
    #         if find[1]-2 < 0:
    #             answer += dp[find[-1]-1][find[3]-1]
    #             break
    #         else:
    #             answer += dp[j][find[3]-1] - dp[j][max(find[1]-2, 0)]

    print(answer)

