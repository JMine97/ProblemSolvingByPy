# 집은 각자의 노드 , x 점 찍고 돌아오기 

import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = [0]*(n+1)
dist = [INF] *(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b)) # cost, end 

def dijk(start, end):
    dist = [INF] *(n+1)
    q = []
    heapq.heappush(q, (0, start)) # cost, node
    dist[start] = 0

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[0] # i[0] : cost, i[1] : node
            if cost < dist[i[1]]:
                dist[i[1]] = cost
                heapq.heappush(q, (cost, i[1])) 

    return dist[end]

for i in range(1, n+1):
    result[i] = dijk(i, x) + dijk(x, i) # 각 노드의 거리수를 담음. 

print(max(result))



