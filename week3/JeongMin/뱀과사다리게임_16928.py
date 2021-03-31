import sys
from heapq import heappop, heappush
input=sys.stdin.readline

n, m=map(int, input().split()) #사다리, 뱀

ladder=[]
snake=[]
graph=[0]*101
for _ in range(n+m):
    a, b=map(int, input().split())
    graph[a]=b

def bfs():
    q=[]
    heappush(q, (0, -1))

    while q:
        cnt, start=heappop(q)
        start=-start
        if start==100:
            print(cnt); return
        for next in range(1, 6+1):
            ns=start+next
            if ns<=100 and graph[ns]!=-1:
                if graph[ns] != 0:
                    ns=graph[ns]
                heappush(q, (cnt+1,-ns))
                graph[ns]=-1

bfs()