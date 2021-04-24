# 17780 새로운 게임

N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)] # 체스판색깔
graph = [[[] for _ in range(N)] for _ in range(N)] # 체스말 위치
chess = [0 for _ in range(K)] # 체스말 위치와 방향

d = dict()
d[1] = (1,0)
d[2] = (-1,0)
d[3] = (0,1)
d[4] = (0,-1)

#print(graph)
loc=[]
for i in range(K):
    x, y, z = map(int, input().split())
    graph[x-1][y-1].append(i)
    chess[i] = [x-1, y-1, z]

cnt = 0
# 012 흰빨파
while 1:
    cnt+=1
    for i in range(len(chess)):
        x, y, z = chess[i]
        dx, dy = d[z]
        
        # print(graph)
        # print (graph[x][y])
        print(chess)
        print(graph)
        
        if i == graph[x][y][0]:
            nx = x + dx
            ny = y + dy

            if 0<=nx<N and 0<=ny<N:
                
                # 흰색 타일 만남
                if color[nx][ny] == 0:
                    graph[nx][ny] += graph[x][y]
                    chess[i][0] = nx
                    chess[i][1] = ny 
                    
                    graph[x][y].clear()
                    
                
                # 빨강 타일 만남
                elif color[nx][ny] == 1:
                    graph[x][y].reverse()
                    graph[nx][ny] += graph[x][y]
                    chess[i][0] = nx
                    chess[i][1] = ny
                    graph[x][y].clear()
                
                # 파랑 타일 만남
                elif color[nx][ny] == 2:
                    if z == 1:
                        chess[i][2] = 2
                    elif z == 2:
                        chess[i][2] = 1
                    elif z == 3:
                        chess[i][2] = 4
                    else:
                        chess[i][2] = 3

    if len(graph[nx][ny]) == 4:
        if cnt > 1000:
            print(-1)
        else:
            print(cnt)
        break
    

