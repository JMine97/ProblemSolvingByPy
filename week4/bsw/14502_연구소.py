# 14502 연구소

# 그래프의 최대 크기 64
# 3개의 벽을 설치하는 전체 경우의 수 : 64C3 -> 크기가 작다 -> 모든 경우의 수를 확인가능
# BFS 함수안에서 벽의 설치와 탐색을 한번에 하려 했으나 실패
# -> 탐색 함수와 벽 설치 함수를 따로 구현해서 사용해야한다.

'''
1. 그래프에 벽을 설치
    1-2. 매번 새로운 벽을 설치해야 한다 -> 그래프를 복사해서 사용
2. 벽이 3개 설치됐을때마다 바이러스전염 및 공간카운트
3. 

'''

from collections import deque
import copy

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

virus = deque()
zero = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append((i,j))
        elif graph[i][j] == 0:
            zero.append((i,j))

maxSize = 0
def bfs():
    global maxSize
    lab = copy.deepcopy(graph)    
    visited = [[False]*M for _ in range(N)]

    # 바이러스 전파
    while virus:
        x, y = virus.popleft()
        visited[x][y] = True    

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                virus.append((nx, ny))

                lab[nx][ny] = 2
    
    # 안전영역 탐색
    zeroCnt = 0
    for col in lab:
        zeroCnt += col.count(0)
    maxSize = max(maxSize, zeroCnt)

    #lab = copy.deepcopy(graph)


def MakeWall(cnt):
    # 벽을 모두 설치한 경우
    if cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if (i, j) in zero:
                zero.remove((i, j))
                graph[i][j] = 1
                MakeWall(cnt + 1)
                graph[i][j] = 0
                
MakeWall(0)
print(maxSize)

'''
[[2, 0, 0, 0, 1, 1, 0], 
 [0, 0, 1, 0, 1, 2, 0], 
 [0, 1, 1, 0, 1, 0, 0], 
 [0, 1, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1, 1], 
 [0, 1, 0, 0, 0, 0, 0], 
 [0, 1, 0, 0, 0, 1, 1]]



 (1,2)
 (2,3)
 (3,4)
 '''
