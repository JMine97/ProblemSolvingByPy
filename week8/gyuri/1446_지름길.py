import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
# 지름길, 고속도로
n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]
dist = [INF] * (d+1)
for _ in range(n):
    s, e, cost = map(int, input().split())
    graph[s].append([e, cost])
for i in range(d):
    graph[i].append([i+1, 1])

def function(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        cost, v = heapq.heappop(q)
        if dist[v] < cost:
            continue
        for i, way in graph[v]:
            if i > d:
                continue
            if way + cost < dist[i]:
                dist[i] = way + cost
                heapq.heappush(q, (dist[i],i))

function(0)
print(dist[d])
