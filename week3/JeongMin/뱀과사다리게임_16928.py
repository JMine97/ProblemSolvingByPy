import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m = map(int, input().split())  # 사다리, 뱀

ladder = []
snake = []
graph = [0] * 101
for _ in range(n + m):
    a, b = map(int, input().split())
    graph[a] = b

def bfs():
    q = []
    heappush(q, (0, -1))
    flag = False

    while q:
        cnt, start = heappop(q)
        start = -start
        # print(q)
        if flag==True:
            print(cnt+1)
            return
        for next in range(1, 6 + 1):
            ns = start + next
            if ns <= 100 and graph[ns] != -1:
                if graph[ns] > 0:
                    ns = graph[ns]
                if ns==100:
                    flag=True
                    break
                heappush(q, (cnt + 1, -ns))
                graph[ns] = -1

bfs()

'''''''''''
cnt 값이 작으면서
ns 값이 큰 거 위주로 
'''''''''''
