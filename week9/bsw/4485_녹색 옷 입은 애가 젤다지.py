cnt=1
while 1:
    N = int(input())
    if N == 0:
        break
    
    graph=[]
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    # sol
    from heapq import heappop, heappush
    pq = []
    heappush(pq, (graph[0][0], 0, 0))
    
    distance = [[999999999] * N for _ in range(N)]
    distance[0][0] = graph[0][0]
    
    while pq:
        cost, x, y = heappop(pq)
        
        for dy, dx in (1,0), (0,1), (-1, 0), (0,-1):
            nx, ny = x+dx, y+dy

            if N<=nx or nx<0 or N<=ny or ny<0:
                continue
            
            if distance[nx][ny] > distance[x][y] + graph[nx][ny]:
                distance[nx][ny] = distance[x][y]+graph[nx][ny]
                heappush(pq, (distance[nx][ny],nx,ny))
                
            
    print("Problem {}: {}" .format(cnt, distance[N-1][N-1]))
    cnt+=1