'''
1753_최단 경로.py
방향그래프, 시작점에서 다른 모든 정점으로의 최단 경로
'''
import sys
import heapq
input = sys.stdin.readline
# 정점의 개수 v, 간선의 개수 e
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
INF = int(1e9)
dist = [INF] * (v+1)
for _ in range(e):
    # u -> v , 가중치 w
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

def function(s):
    q = []
    dist[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        cost, v = heapq.heappop(q)
        if dist[v] < cost:
            continue
        for i, j in graph[v]:
            if cost + j < dist[i]:
                dist[i] = cost + j
                heapq.heappush(q, (dist[i],i))

function(start)
for i in range(1, len(dist)):
    if dist[i] == INF:
        print('INF')
    else :
        print(dist[i])
