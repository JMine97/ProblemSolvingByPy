# 16948 데스 나이트

# 그래프 탐색
# BFS

from collections import deque

N = int(input())
x, y, X, Y = map(int, input().split())

# 데스 나이트의 이동가능 경로
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

# 그래프 정보
visited = [[False]*N for _ in range(N)]
dist = [[0]*N for _ in range(N)]
q = deque()
MIN = 999999999

def BFS(x, y):
    global MIN
    visited[x][y] = True
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 오류가 없으면
            if 0<= nx < N and 0 <= ny < N:
                if visited[nx][ny] == False:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                    visited[nx][ny] = True
                # 도착 좌표에 도달했을 경우 최소거리 업데이트
                if (nx, ny) == (X, Y):
                    MIN = min(MIN, dist[nx][ny])

BFS(x,y)

if MIN == 999999999:
    print(-1)
else:
    print(MIN)