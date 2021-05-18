import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
# n = 도시의 개수 m = 버스의 개수 

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
dist = [INF] *(n+1)
for _ in range(m): # 단방향성 문제. 
    s, e, c = map(int, input().split()) # 시작, 도착, 비용 
    graph[s].append((e, c)) # 노드, 거리 
    # graph[e].append((s,c))

a, b = map(int, input().split()) # 출발 , 도착 


def dijk(start):
    q = []
    heapq.heappush(q, (0, start)) # 초기화
    dist[start] = 0 # 초기 위치 거리 cost 0

    while q:
        d, now = heapq.heappop(q) # 거리, 노드 
        if dist[now] < d: 
            continue

        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijk(a)
print(dist[b])
