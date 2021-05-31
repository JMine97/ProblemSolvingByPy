# 1238번_파티.py
'''
N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다
N명의 학생이 X번 마을에 모여서 파티를 벌이기로 했다.
M개의 단방향 도로들, Ti의 시간 소비
최단 시간에 오고가기를 원한다.

각 학생들의 왕복 최단 시간을 구하고 그 중 가장 오래걸린 학생을 반환
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, m, x = map(int, input().split())
# 각 지점이 갈수있는 마을과 시간을 graph에 저장
graph = [[] for _ in range(n)]
answer = [0] * n
for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s-1].append([e-1, t])

def function(start, end):
    q = []
    dist = [INF] * n
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        cost, v = heapq.heappop(q)
        if dist[v] < cost:
            continue
        for e, t in graph[v]:
            if dist[e] > cost + t:
                dist[e] = cost + t
                heapq.heappush(q, (dist[e], e))
    return dist[end]



# 모든 학생의 거리를 구할 수 있게
for i in range(n):
    # x 마을로 가기
    answer[i] = function(i, x-1)
    # 집에 오기
    answer[i] += function(x-1, i)

print(max(answer))
