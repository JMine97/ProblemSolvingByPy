M, N = map(int, input().split())

graph=[]
for _ in range(N):
    string=input()
    tmp=[]
    for s in string:
        tmp.append(int(s))
    graph.append(tmp)
dist = [[999999999 for _ in range(M)]for range_ in range(N)]
dist[0][0] = 0
import heapq

print(graph)
print(dist)

pq=[]

heapq.heappush(pq, (0,0,0))

broken=0
while pq:
    cost, x, y = heapq.heappop(pq)

    for dy, dx in (1,0), (0,1), (-1,0), (0,-1):
        nx, ny = x+dx, y+dy

        if nx<0 or N<=nx or ny<0 or M<=ny:
            continue
        if graph[nx][ny] == 1:
            if dist[nx][ny] > cost + 1:
                dist[nx][ny] = cost + 1
                heapq.heappush(pq, (cost+1, nx, ny))
        
        elif graph[nx][ny] == 0:
            if dist[nx][ny] > cost:
                dist[nx][ny] = cost
                heapq.heappush(pq, (cost, nx, ny))
        
print(dist[N-1][M-1])
