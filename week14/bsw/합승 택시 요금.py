# 가중치 그래프 -> 다익스트라
#
# 다른사람 풀이 보고 작성
# 다익스트라 연습이 더 필요

def solution(n, s, a, b, fares):
    answer = 1e9
    INF = 1e9
    from heapq import heappush, heappop
    
    graph=[[] for _ in range(n+1)]
    
    for fare in fares:
        src, dst, cost = fare
        graph[src].append((dst, cost))
        graph[dst].append((src, cost))
    
    def dijk(s, d):
        dists = [INF for i in range(n+1)]
        dists[s] = 0
        pq = []
        heappush(pq, (dists[s], s))
    
        while pq:
            cur_dist, cur_dst = heappop(pq)
        
            if dists[cur_dst] < cur_dist:
                continue
        
            for new_dst, new_dist in graph[cur_dst]:

                if cur_dist + new_dist < dists[new_dst]:
                    dists[new_dst] = cur_dist + new_dist
                    heappush(pq, (dists[new_dst], new_dst))
        
        return dists[d]
    
    for i in range(1, n+1):
        answer = min(dijk(s, i) + dijk(i,a) + dijk(i,b), answer)
    
    return answer