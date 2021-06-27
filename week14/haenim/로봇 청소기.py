"""
빈칸 0 벽 1
바라보는 방향: 0 북, 1 동, 2 남, 3 서


"""



def solution():
    count = 1
    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    board[x][y] =  2 #현재 위치 청소

    dx, dy = [-1,0,1,0], [0,1,0,-1]
    
    while True:
        fail = True

        for i in range(4):
           
            nd = (d+3)%4 # 다음 방향
            nx,ny = x + dx[nd], y + dy[nd] #그 방향으로 이동
            d = nd

            if nx >= n or ny >= m:
                continue
                
            
            elif board[nx][ny] == 0 : #빈칸이면
                board[nx][ny] = 2 #청소
                x,y = nx,ny
                count += 1
                fail = False
                break


        # 네 방향 모두 청소 못했으면
        if fail == True:
            nd = (d + 2) % 4 #후진
            nx,ny = x + dx[nd], y + dy[nd]

            if nx >= n or ny >= m or board[nx][ny] == 1:
                return count
            
            else :
                x,y = nx, ny
                
    return count

print(solution())
        



