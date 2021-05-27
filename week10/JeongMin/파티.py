'''
1차 시도(2020ms) : 점마다 다익스트라 돌림
2차 시도(88ms) : 역방향 그래프(집에서 파티 장소로 가는 거리)
         + 정방향 그래프(파티 장소에서 집으로 오는 거리) 두 개 이용
https://kangmin1012.tistory.com/8
'''
import sys
import heapq as hq
input=sys.stdin.readline
INF=10**9

n, m, x = map(int, input().split())
graph=[[] for _ in range(n+1)]
reverse_graph=[[] for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append([t, e])
    reverse_graph[e].append([t, s])

q=[]
def dijkstra(start, graph):
    hq.heappush(q, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0

    while q:
        dist, now = hq.heappop(q)

        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost = dist + i[0]
            target = i[1]
            if cost < distance[target]:
                hq.heappush(q, (cost, target))
                distance[target] = cost
    return distance

distance_a=dijkstra(x, reverse_graph) #집에서 파티 장소로 가는 최단거리
distance_b=dijkstra(x, graph) #파티가 끝나고 집으로 오는 최단거리

ret=0
for i in range(1, n+1):
    ret=max(ret, distance_a[i]+distance_b[i])

print(ret)



'''
1차 시도 코드
'''
# import sys
# import heapq as hq
# input=sys.stdin.readline
# INF=10**9
#
# '''
# ??? : 역방향 그래프를 저장하는데 그게 어떻게 되는지 질문
# 점마다 다익스트라 모두 돌리면
# 다익스트라 시간복잡도 elogv
# 10^4*log(10^3)*10^3
# == 3*10^7*log(10^3) 니까 될 듯
# '''
#
# n, m, x = map(int, input().split())
# graph=[[] for _ in range(n+1)]
#
# for _ in range(m):
#     s, e, t = map(int, input().split())
#     graph[s].append([t, e])
#
# q=[]
# def dijkstra(start):
#     hq.heappush(q, (0, start))
#     distance = [INF] * (n + 1)
#     distance[start] = 0
#
#     while q:
#         dist, now = hq.heappop(q)
#         for i in graph[now]:
#             cost = dist + i[0]
#             target = i[1]
#             if cost < distance[target]:
#                 hq.heappush(q, (cost, target))
#                 distance[target] = cost
#     return distance
#
# return_distance=dijkstra(x)
#
# result=0
# for start in range(1, n + 1):
#     if start==x:
#         continue
#     start_distance=dijkstra(start)
#     cost=start_distance[x]+return_distance[start]
#     result=max(result, cost)
#
# print(result)
