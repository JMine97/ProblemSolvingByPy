import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)


n, m = map(int, input().split())
k = int(input()) # start
graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split()) # 시작, 도착, 가중치
    graph[u].append((v, w)) # 노드, 가중치 

def dijk(start):
    q = []
    heapq.heappush(q, (0, start)) # 초기 거리, 초기 노드
    dist[start] = 0 

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in graph[now]: # i[0] = 노드 i[1] = 가중치 
            cost = d + i[1]
            if cost < dist[i[0]]: # dist[node] -> 가중치
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijk(k)

for i in range(1, n+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])

