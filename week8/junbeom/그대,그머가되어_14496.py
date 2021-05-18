# 특정 거리의 도시 찾기와 동일한 문제로 생각. 근데 상호로 연결이 되어있는 문제

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
a, b = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
dist = [INF] *(n+1)

for i in range(m):  # 여길 n으로 기입해서 계속 오답이 나왔음. 실수하지 않기 
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# print(graph)
def dijk(start):
    q = []
    heapq.heappush(q, (0, start)) # 거리와 노드를 넣어준다. 
    dist[start] = 0 # 시작 위치의 거리 테이블을 0으로 부여한다. 

    while q:
        d, now = heapq.heappop(q) # 현재 위치까지 온 거리와 현재 노드를 뽑아 준다. 
        if dist[now] < d:
            continue # 새로 조회하는 노드가 기존에 점검한 노드이고, 기존 점검한 노드가 더 효율이 좋으면 넘어감. 

        for i in graph[now]:
            cost = d + 1 
            if cost < dist[i]: # 갱신 조건
                dist[i] = cost
                heapq.heappush(q, (cost, i))


dijk(a)
if dist[b] == INF:
    print(-1)
    sys.exit(0)
else : print(dist[b])

