'''
1916_최소비용 구하기.py
N개의 도시 , M개의 버스
A번째 도시 -> B번째 도시까지 최소 비용
'''
import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
dist = [INF] * (n+1)
for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append([e, cost])
a, b = map(int, input().split())

def function(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        cost, v = heapq.heappop(q)
        if dist[v] < cost:
            continue
        for i, c in graph[v]:
            if c + cost < dist[i]:
                dist[i] = c + cost
                heapq.heappush(q,(dist[i], i))
function(a)
#print(dist)
print(dist[b])
