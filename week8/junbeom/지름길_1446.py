# idea : 지름길의 길이가 다 다름 . 양수(음수면은 벨만포드나 플로이드워셜을 생각해야함, 역주행 할 수 없음 -> 단방향이라는 뜻)
# 지름길이 통과하는 그 도착 지점에서 그냥 온 거리와 비교할 것.
# 도착길이가 넘어가면 무시할 것.

# 시간 복잡도 : ElogV : 10^4 * (log 10^4)
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, D = map(int, input().split())

dist = [INF] * (D+1)
graph = [[] for _ in range(D+1)] 
for _ in range(n):
    a, b, c = map(int, input().split()) # 시작위치, 도착위치, 거리 
    if b > D: # 도착위치가 주어진 고속도로의 길이보다 길다면 
        continue  
    graph[a].append((b, c))

for i in range(D):
    graph[i].append((i+1,1)) # 0부터 d까지 다 cost 1로 연결하기 위함.  graph  - (노드, 거리)


def dijk(start):
    q = []
    heapq.heappush(q, (0, start)) # q - (거리, 노드)
    
    while q:
        now, d = heapq.heappop(q)        
        
        if dist[now] < d: # 거리 테이블에서 같은 노드가 여러개 있더라도, 가장 작은 거리수를 가진 것만 탐색. (BFS의 방문처리와 같음.)
            continue 
        
        for i in graph[now]: # 노드, 거리 
            cost = d + i[1]

            if cost < dist[i[0]]: # 거리 테이블의 기존 거리보다 cost가 더 작으면 
                dist[i[0]] = cost # 갱신
                heapq.heappush(q, (i[0], cost)) # 
            
    return dist[D]

print(dijk(0)) # 시작점 0 

