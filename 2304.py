N = int(input())

poles = [list(map(int, input().split())) for _ in range(N)]
poles.sort()
print(poles)