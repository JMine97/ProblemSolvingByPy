'''
주의!!
지름길을 타지 않을 수 있다.
예제1의 경우 0->50(10) + 50->100(10) + 100->150(50) 으로 70이 나온다

최대 입력 10^4, 시간제한 10^16
다익스트라 알고리즘 O(ElogV)이므로 10^4*log(10^4)=4*10^4이 된다
모든 노드를 다 순회해도 넉넉히 시간이 남는다

graph의 역할 : 노드들이 몇의 가중치로 연결돼있는지 확인
distance의 역할 : 시작노드 (고정)-> 도착노드(인덱스값)까지의 최단 거리 담음
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,d = map(int, input().split())
graph = [[] for i in range(d + 1)]
distance = [INF]*(d + 1)

for _ in range(n):
    a, b, c = map(int, input().split())
    if b>d:
        continue
    graph[a].append((b, c))
for i in range(d):
    graph[i].append((i+1, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(0)

print(distance[-1])
