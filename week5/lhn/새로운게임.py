import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(chess_num):
    x, y, z = chess[chess_num] #num번째 턴에 움직일 체스

    #입력 받은 말과 말이 있는 곳의 맨밑의 말 번호가 다르면 return
    if chess_num != chess_map[x][y][0]:
        return 0
    
    #다음으로 이동할 칸
    nx = x + dx[z]
    ny = y + dy[z]

    #다음으로 이동했을 때 범위내에 없거나 파란색이면
    if not 0 <= nx < n or not 0 <= ny < n or a[nx][ny] == 2:
        #방향을 전환함
        
        if 0 <= z <= 1: #-> <- 방향으로 움직이는 경우에는
            nz = (z+1) % 2 #각각 <- -> 방향으로 바꿔줌
        else:
            nz = (z-1) % 2 + 2 #위면 아래 아래면 위로 바꿈
        chess[chess_num][2] = nz
        nx = x + dx[nz]
        ny = y + dy[nz]
        #방향을 전환해도 움직일 수 없으면 끝냄
        if not 0 <= nx < n or not 0 <= ny < n or a[nx][ny] == 2:
            return 0

    chess_set = []
    chess_set.extend(chess_map[x][y]) #다음으로 이동할 체스 묶음
    chess_map[x][y] = [] #현재 좌표에서 체스를 없앰

    if a[nx][ny] == 1: #다음으로 이동할 칸이 빨간색이면
        chess_set = chess_set[-1::-1] #말의 업힌 순서 변경

    
    for i in chess_set:
        chess_map[nx][ny].append(i) #체스 판에 말을 추가
        chess[i][:2] = [nx, ny]


    if len(chess_map[nx][ny]) >= 4: #4개 이상 올라탔으면 flag=1로
        return 1
    return 0

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
chess_map = [[[] for _ in range(n)] for _ in range(n)]
chess = [0 for _ in range(k)]

for i in range(k):
    x, y, z = map(int, input().split())
    chess_map[x-1][y-1].append(i)
    chess[i] = [x-1, y-1, z-1]

cnt = 1
while cnt <= 1000:# 게임 턴이 1000 이하여야함
    for i in range(k):
        flag = move(i)
        
        if flag: # 이 턴에 게임이 끝났으면
            print(cnt) #답 출력
            sys.exit()
    cnt += 1
print(-1)
