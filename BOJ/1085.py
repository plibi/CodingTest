x, y, w, h = map(int, input().split())

t1 = min(x, w-x)
t2 = min(y, h-y)
print(min(t1, t2))