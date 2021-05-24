# 4485번_녹색 옷 입은 애가 젤다지?.py
# 50% 에서 틀림

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
answer = []
d_x = [-1,1,0,0]
d_y = [0,0,-1,1]

def dijkstra(g):
    q = []
    dist = [[INF] * n for _ in range(n)]
    heapq.heappush(q, (g[0][0], 0, 0))
    dist[0][0] = g[0][0]
    while q:
        cost, px, py = heapq.heappop(q)
        if cost > dist[px][py]:
            continue
        for i, j in zip(d_x, d_y):
            row = i + px
            col = j + py
            if 0 <= row < n and 0 <= col< n:
                if dist[row][col] > cost + g[row][col]:
                    dist[row][col] = cost + g[row][col]
                    heapq.heappush(q, (dist[row][col], row, col))

    return dist[-1][-1]

while n:
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    answer.append(dijkstra(graph))
    n = int(input())

for i, v in enumerate(answer):
    print("Problem ", i, ": ", v)
