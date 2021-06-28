# 방향 변경 + dfs 
import sys
from collections import deque

n, m = map(int, input().split())

dx = [-1, 0, 1, 0] # 0 1 2 3 상 우 하 좌 
dy = [0, 1, 0, -1]

r, c, d = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
ans = 0

def clean(x, y, d):
  global ans
  if graph[x][y] == 0:
    graph[x][y] = 2 
    ans += 1 
  for _ in range(4):
    nd = (d + 3) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if graph[nx][ny] == 0: # 청소할 곳이 생기면 
      clean(nx, ny, nd)  
      return
    d = nd # 왼 방향으로 회전 
  nd = (d + 2) % 4 # 네 방향이 갈 수 없는 상태면 뒤로 이동 (d+2) 
  nx = x + dx[nd]
  ny = y + dy[nd]
  if graph[nx][ny] == 1: # 그럼에도 청소할 곳이 더 없으면
    return # 종료
  clean(nx, ny, d)

clean(r, c, d)
print(ans)
