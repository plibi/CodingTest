import heapq
import sys
N = int(sys.stdin.readline().rstrip())

heap = []

for _ in range(N):
    C = int(sys.stdin.readline().rstrip())
    if C == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -C)

