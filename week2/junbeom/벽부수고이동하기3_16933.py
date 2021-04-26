
# idea
# BFS로 풀이. 거리를 나타내는 dist 그래프를 추가로 만들어서 -1로 초기화한 다음, dist[n-1][m-1]을 답으로 제출.(dist[n-1][m-1] = -1 이면 벽에 막혀 마지막까지 못 왔다는 뜻.)
# 낮밤을 구별해서 4방향 탐색. 
  
#  벽부술 수 있는 카운트 : K  <-  
# 2. 낮에만 벽을 깰 수 있음 . 낮밤이 카운트를 할때마다 . 
#   
from sys 
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(input()) for _ in range(n)]
check = [[[False]*(k+1) for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
def bfs():
    q = deque()
    q.append((0, 0, 0, 1))
    check[0][0][0] = True # 시작점 방문
    day = True # 낮부터 시작 
    while q:
        p = len(q) 
        for _ in range(p):  
            x, y, wallCount, d = q.popleft() # wallCount = 벽을 부순 개수,  d = distance (answer)
            if x == n-1 and y == m-1:
                return d
      
            for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              if 0 <= nx < n and 0 <= ny < m:
                  if graph[nx][ny] == '1' and wallCount < k and not check[nx][ny][wallCount+1]: # 벽이고 
                      if day:
                          q.append((nx, ny, wallCount+1, d+1))
                          check[nx][ny][wallCount+1] = True
                      else:
                          q.append((x, y, wallCount, d+1))
                  if graph[nx][ny] == '0' and not check[nx][ny][wallCount]:
                      q.append((nx, ny, wallCount, d+1))
                      check[nx][ny][wallCount] = True
        
        day = not day
    return -1

print(bfs())