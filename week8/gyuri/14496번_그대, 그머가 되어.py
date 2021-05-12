# 14496번 그대, 그머가 되어
'''
최단 경로를 구하는 문제
양방향
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
a, b = map(int, input().split())
n, m = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

for _ in range(m):
    p1, p2 = map(int, input().split())
    graph[p1].append([p2, 1])
    graph[p2].append([p1, 1])

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로를 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # heap에서 거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 업데이트가 필요없을 정도로 거리가 짧으면 continue
        if distance[now] < dist :
            continue
        for i, d in graph[now]:
            cost = dist + d
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
dijkstra(a)
distance[b] = distance[b] if distance[b]!=INF else -1
print(distance[b])
