# idea: BFS가 아닌 다익스트라로 풀어볼 것. 

import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijk(start):
    q = []
    heapq.heappush(q, (0, start)) # (거리, 노드)
    dist[start] = 0 # 거리 초기화

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d: continue # 거리 테이블을 점검하는 것. visited[]와 같은 방문처리를 하는 것에 대한 리스트를 선언하지 않고 이를 처리함. 

        for i in graph[now]:
            # cost = d + i[1] # edge당 차이가 있는 경우
            cost = d + 1 # 거리가 1로 고정이니까
            if cost < dist[i]:
                dist[i] = cost # 갱신을 해줌. 
                # heapq.heappush(q, (cost, i[0])) # 도착점과 간선이 나와있는 경우 
                heapq.heappush(q, (cost, i))
    

dijk(x)

print(dist)
if k not in dist: 
  print("-1")

for i in range(1, n+1):
  if dist[i] == k:
    print(i)
