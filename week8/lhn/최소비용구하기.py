"""
o(n)

"""

import sys
from heapq import heappush, heappop


def dijkstra(start, end):
    heap = []
    heappush(heap, (0, start))  # 출발지로 가는데 0원의 비용
    distance = [sys.maxsize] * (N + 1)  # 출발 도시에서 다른 도시까지 최단으로 이동할 때 드는 비용
    distance[start] = 0  # 시작 지점 0으로 초기화

    while heap:
        curr_cost, curr_node = heappop(heap) #현재 node까지 가는데 비용
        for end, cost in bus[curr_node]: #node에서 end로 가는데 필요한 cost
            if distance[end] > curr_cost + cost: # 현재 출발지에서 end까지 가는 최단 거리가 현재비용 + 이동비용보다 크면
                distance[end] = curr_cost+ cost # 출발지에서 end까지 가는데 드는 비용을 curr_cost+cost로 업데이트
                heappush(heap, (curr_cost + cost, end)) # end까지 가는데 curr_cost+cost의 비용
    return distance[end]



N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수
bus = [[] for _ in range(N + 1) #버스의 정보
       ]
for _ in range(M): 
    start, end, cost = map(int, input().split())  # 출발지 번호 , 도착지 번호, 버스 비용
    bus[start].append((end, cost)) 
    
start, end = map(int, input().split())  # 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호(출발지, 도착지)

print(dijkstra(start, end))
