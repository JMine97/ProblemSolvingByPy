import heapq

def solution(n, s, a, b, fares):
    INF = int(1e9) 
    graph = [[] for _ in range(n+1)]
    for x, y, z in fares:
        graph[x].append((z, y))
        graph[y].append((z, x))

    def dijkstra(start):
        dist = [INF] * (n + 1)
        dist[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))
        while heap:
            value, destination = heapq.heappop(heap)
            if dist[destination] < value:
                continue

            for v, d in graph[destination]:
                next_value = value + v
                if dist[d] > next_value:
                    dist[d] = next_value
                    heapq.heappush(heap, (next_value, d))
        return dist

    dp = [[]] + [dijkstra(i) for i in range(1, n+1)]
    # print(dp)
    answer = INF
    for i in range(1, n+1):
        answer = min(dp[i][a] + dp[i][b] + dp[i][s], answer)

    return answer

'''
두명이 같은 위치에서 택시를 타고 같이 내린다.
그 후 각자 택시를 타 최소 요금으로 각자 목적지에 도착한다.

가중치가 있는 그래프 -> 다익스트라

'''
