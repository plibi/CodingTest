# 주유소 가격 list를 만들고
# 다음 주유소의 가격이 더 비싸면 이전 주유소 가격으로 대체

n = int(input())
length = list(map(int, input().split()))
station = list(map(int, input().split()))
cost = 0

for i in range(n-1):
    if station[i] < station[i+1]:
        station[i+1] = station[i]

for i in range(n-1):
    cost += station[i] * length[i]
    
print(cost)