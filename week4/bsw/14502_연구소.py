# 14502 연구소

# 그래프의 최대 크기 64
# 3개의 벽을 설치하는 전체 경우의 수 : 64C3 -> 크기가 작다 -> 모든 경우의 수를 확인가능
# BFS 함수안에서 벽의 설치와 탐색을 한번에 하려 했으나 실패
# -> 영역 탐색과 벽 설치를 따로 구현해서 사용해야한다.
#
# combination 사용 연습필요



from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
ans = 0
def bfs():
    Cgraph = copy.deepcopy(graph)

    # 바이러스 초기 위치
    for i in range(N):
        for j in range(M):
            if Cgraph[i][j] == 2:
                q.append((i, j))
              
    # 확산
    global ans
    while q:
        x, y = q.popleft()
        # visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx <N and 0<= ny <M and Cgraph[nx][ny] == 0:
                Cgraph[nx][ny] = 2
                q.append((nx, ny))
               
    # 안전 영역 측정
    safeArea = 0
    for i in range(N):
        for j in range(M):
            if Cgraph[i][j] == 0:
                safeArea += 1
    
    ans = max(ans, safeArea)
    


def MakeWall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                MakeWall(cnt + 1)
                graph[i][j] = 0

MakeWall(0)
print(ans)



