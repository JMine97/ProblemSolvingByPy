import sys
import heapq as hq
input=sys.stdin.readline
INF=10**9

'''
??? : 역방향 그래프를 저장하는데 그게 어떻게 되는지 질문

점마다 다익스트라 모두 돌리면

다익스트라 시간복잡도 elogv
10^4*log(10^3)*10^3
== 3*10^7*log(10^3) 니까 될 듯
'''

n, m, x = map(int, input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append([t, e])

q=[]
def dijkstra(start):
    hq.heappush(q, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0

    while q:
        dist, now = hq.heappop(q)
        for i in graph[now]:
            cost = dist + i[0]
            target = i[1]
            if cost < distance[target]:
                hq.heappush(q, (cost, target))
                distance[target] = cost
    return distance

return_distance=dijkstra(x)

result=0
for start in range(1, n + 1):
    if start==x:
        continue
    start_distance=dijkstra(start)
    cost=start_distance[x]+return_distance[start]
    result=max(result, cost)

print(result)
