# 14502 연구소

# 그래프의 최대 크기 64
# 3개의 벽을 설치하는 전체 경우의 수 : 64C3 -> 크기가 작다 -> 모든 경우의 수를 확인가능
# BFS 함수안에서 벽의 설치와 탐색을 한번에 하려 했으나 실패
# -> 탐색 함수와 벽 설치 함수를 따로 구현해서 사용해야한다.



from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
lab = graph[:]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False]*M for _ in range(N)]
q = deque()

zeroCnt = 0 # 안전한 공간
Max = 0
def bfs(x, y):
    visited[x][y] == True
    q.append((x,y))
    global zeroCnt ,Max
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx <M and 0<= ny <N:
                if visited[nx][ny] == False:
                    q.append((nx,ny))
                    if lab[nx][ny] == 0:
                        zeroCnt += 1
                        Max = max(Max, zeroCnt)

def MakeWall(cnt):
    if cnt == 3:
        bfs(0, 0)
        return
    
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                MakeWall(cnt + 1)
                lab[i][j] = 0

cnt = 0
MakeWall(cnt)
print(Max)



