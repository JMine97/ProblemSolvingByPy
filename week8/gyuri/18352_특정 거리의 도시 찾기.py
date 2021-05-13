'''
18352_특정 거리의 도시 찾기.py
N번 도시, M개의 단방향 도로
x 출발 거리가 K인 도시
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
answer = []
n, m, k, x = map(int, input().split())
dist = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def function(s):
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0
    while q:
        cost, city = heapq.heappop(q)
        if dist[city] < cost:
            continue
        for i in graph[city]:
            if 1 + cost < dist[i]:
                dist[i] = 1+cost
                heapq.heappush(q, (dist[i], i))
function(x)
for i, v in enumerate(dist):
    if v == k:
        answer.append(i)
if not answer:
    print('-1')
else:
    answer.sort()
    for i in answer:
        print(i)



