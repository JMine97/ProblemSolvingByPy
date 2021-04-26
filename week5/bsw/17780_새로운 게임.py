'''
1. chess의 0번 인덱스 부터 이동
    if 해당 인덱스의 체스말이 가장 밑에 있을 때
        if 이동 할 칸이 파랑 or 범위밖
            방향 반대로
            if 이동방향이 파랑색 or 범위밖 continue
                else 한칸이동 -> 재귀 X -> pass

        elif 흰색
            if 이동 할 칸에 체스말이 있을경우
                그대로 위에올림
        elif 빨간색
            if 이동 할 칸에 체스말이 있을경우
                뒤집어서 올림

체스판 색깔 
체스판 좌표별 체스말 
체스말 위치 및 현재 이동방향
'''

N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]
chessMap = [[[] for _ in range(N)] for _ in range(N)]
chess = []

for i in range(K):
    x, y, d = map(int, input().split())
    chessMap[x-1][y-1].append(i)
    chess.append([x-1, y-1, d-1])

print(color)
print(chessMap)
print(chess)

cnt = 0
flag = False
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
while cnt <= 1000:
    cnt+=1

    for i in range(len(chess)):
        x, y, d = chess[i] 
        
        if not chessMap[x][y] or i != chessMap[x][y][0]:
            continue
        # 배열을 사용할 때 x축 방향인지 y축 방향인지 꼼꼼히 확인하자
        nx = x + dx[d]
        ny = y + dy[d]

        # 다음칸이 파랑 or 범위 밖
        if (nx< 0 or N<=nx) or (ny<0 or N<=ny) or color[nx][ny] == 2:
            if chess[i][2] == 0:
                chess[i][2] = 1
            elif chess[i][2] == 1:
                chess[i][2] = 0
            elif chess[i][2] == 2: 
                chess[i][2] = 3
            elif chess[i][2] == 3:
                chess[i][2] = 2

            nx = x + dx[chess[i][2]]
            ny = y + dy[chess[i][2]]
            
            if (nx< 0 or N<=nx) or (ny<0 or N<=ny) or color[nx][ny] == 2:
                continue
            chess[i][0] = nx
            chess[i][1] = ny

        # 다음칸이 흰색
        if color[nx][ny] == 0:
            chessMap[nx][ny] = chessMap[nx][ny] + chessMap[x][y]

        # 다음칸이 빨강색
        elif color[nx][ny] == 1:
            chessMap[nx][ny] = chessMap[nx][ny] + list(reversed(chessMap[x][y]))

        # 이동시 업혀있는 모든 체스말들의 좌표 업데이트
        for ch in chessMap[nx][ny]:
            chess[ch][0] = nx
            chess[ch][1] = ny
        
        chessMap[x][y].clear()

        if len(chessMap[nx][ny]) == 4:
            flag = True
            break

    if flag:
        break


if cnt > 1000:
    print(-1)
else:
    print(cnt)
                    


    



