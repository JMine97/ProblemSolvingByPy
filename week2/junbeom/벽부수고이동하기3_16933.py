# 오답입니다** 
# 시간 2초, 메모리 512로 넉넉한 편. (DFS/BFS 및 브루트포스 가능)
# BFS 

# idea
# BFS로 풀이. 거리를 나타내는 dist 그래프를 추가로 만들어서 -1로 초기화한 다음, dist[n-1][m-1]을 답으로 제출.(dist[n-1][m-1] = -1 이면 벽에 막혀 마지막까지 못 왔다는 뜻.)
# 낮밤을 구별해서 4방향 탐색. 

import sys
from collections import deque
input = sys.stdin.readline # -> 마지막 개행문자까지 딸려오니까 rstrip 사용

# 0, 0 -> n-1, m-1 
n, m, k = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input().rstrip()))) # 마지막 개행문자 제거.

dist = [[-1]*m for _ in range(n)]

dist[0][0] = 1 # 시작점이기 때문에 시작 카운트로 부여  (1로 시작한다는 점을 주의.)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()
q.append((0, 0))

def bfs():
  global wallCount
  wallCount = k # 벽을 깨는 수
  day = True # 낮   
  while q: 
    print(q)
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        
        if graph[nx][ny] == 0 and dist[nx][ny] == -1: # 낮밤 무시하고 이동 가능할 때 -> 벽이 없고 아직 가지 않았을 때.
          dist[nx][ny] = dist[x][y] + 1 # 거리 증가 
          q.append((nx, ny)) # 큐에 추가 
          
        if day: # 낮이면 
          # print("DAY")
          if graph[nx][ny] == 1 and dist[nx][ny] == -1:
            if wallCount > 0: # 벽을 깰 수 있는 카운트가 남아 있으면,
              wallCount -= 1  # -= 1 
              dist[nx][ny] = dist[x][y] + 1 # 이동
              q.append((nx, ny)) # 큐에 추가 
            else: # wall Count 더 없으면, 
              dist[x][y] += 1 # 해당 자리에서 += 1
              q.append((x, y)) # 그 자리를 큐에 추가 

        else: # 밤이면
          # print("NIGHT")
          # print((x, y))
          # print((nx, ny))
          if graph[nx][ny] == 1 and dist[nx][ny] == -1: # 벽이 있는 경우. ** 여기에 안들어 감.
            dist[x][y] = dist[x][y] + 1 # 해당 자리를 + 1
            q.append((x, y)) # 큐에 추가. 
          # print("sfsdfsdfsdsdfsdfsdf")
        
        # print(graph)
        # print(dist) 
        # print("this is day == " + str(day))
        day = not day # 낮밤 변경


bfs() 
print(dist[n-1][m-1])