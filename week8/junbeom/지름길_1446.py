# idea : 지름의 길이가 다 다름 . 양수(음수면은 벨만포드나 플로이드워셜을 생각해야함, 역주행 할 수 없음 -> 단방향이라는 뜻)
# 지름길이 통과하는 그 도착 지점에서 그냥 온 거리와 비교할 것.
# 도착길이가 넘어가면 무시할 것.

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, D = map(int, input().split())

dist = [INF] * (D+1)
graph = [[] for _ in range(D+1)] # D+1이 되려나..?
for _ in range(n):
    a, b, c = map(int, input().split())
    if b > D:
        continue
    graph[a].append((b, c))

for i in range(D):
    graph[i].append((i+1,1)) # 0부터 d까지 다 1로 이음. 


# print(graph)

def dijk(start):
    q = []
    heapq.heappush(q, (0, start))
    

    while q:
        now, d = heapq.heappop(q)        
        
        if dist[now] < d:
            continue
        
        for i in graph[now]: # 노드, 거리 
            cost = d + i[1]

            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (i[0], cost))
            
    return dist[D]

print(dijk(0)) # 시작점은 0이니까 

