# 2초, 512MB -> 넉넉한 시간과 넉넉한 메모리. -> BFS, DFS 가능
# n 제한이 작으므로 각 m에서 bfs를 돌려도 input이 50 이하이기 때문에 Brute Force 도 가능함. 

# idea
# 1. 각 자리에서 최단거리를 구하는 알고리즘을 BFS로 구한다. BFS로 구하면 상어들에게 퍼지는 것을 우선으로 부여해 안전거리를 수월하게 확인할 수 있다. 
# 2. 그래프 전체에서 최대의 안전거리를 뽑아낸다. 

# mistake
# 문제를 잘 읽자. 1과 1 사이의 거리를 리턴하는 것으로 오해했다. 

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

dx = [0, 0, -1, -1, -1, 1, 1, 1]
dy = [-1, 1, 1, 0, -1, 1, 0, -1] # 8 방향 

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))
    
dist = [[-1] * m for _ in range(n)] # 거리를 나타내는 그래프. -1로 모두 초기화. 

def bfs(shark): # 아기 상어의 자리를 담은 큐를 인자로 받음. 
  q = shark
  while q:
    x, y = q.popleft()
    
    for i in range(8): # 8방향으로 탐색 
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if dist[nx][ny] == -1: # 아직 탐색이 된 곳이 아니면 ,
          dist[nx][ny] = dist[x][y] + 1 # 탐색
          q.append((nx, ny)) # 큐에 담아줌.
  
  return


shark = deque() # 상어의 위치를 담을 큐
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      shark.append((i, j)) # 아기 상어 위치를 다 넣음.
      dist[i][j] = 0 # 현재 위치를 0으로 세팅 

bfs(shark) # shark 큐에 담긴 모든 위치를 계속 넣음. 그 다음 가장 작은 위치에서 만나는 것을 리턴. 
max_dist = 0
for row in dist: 
  max_dist = max(max(row), max_dist) # 최대 안정거리 (답)

print(max_dist)