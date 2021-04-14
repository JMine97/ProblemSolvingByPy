# 본인 기준 주변 육각형으로 이동 가능함. 
# 
import sys
from collections import deque

n = int(input())

r1, c1, r2, c2 = map(int, input().split()) # 시작점 -> 끝점 

dr = [-2, -2, 0, 0, 2, 2] 
dc = [-1, 1, -2, 2, -1, 1]

dist = [[-1]*(n) for _ in range(n)]

q = deque()
q.append((r1, c1))
dist[r1][c1] = 0 # 시작점 

while q:
  r, c = q.popleft()

  for i in range(6): # 육각형
    nr = r + dr[i]
    nc = c + dc[i]

   
    if 0 <= nr < n and 0 <= nc < n: # 범위 안에 있으면,
      if nr == r2 and nc == c2:
        dist[r2][c2] = dist[r][c] + 1
        print(dist[r2][c2])
        sys.exit() # 종료 

      if dist[nr][nc] == -1 or dist[r][c]+1 < dist[nr][nc]: #아직 안 갔거나 갱신이 되면 더 좋은 경우, 
        dist[nr][nc] = dist[r][c] + 1
        q.append((nr, nc))
      


print(-1) # 제출하고 생각했지만, 좋은 로직은 아닌 듯. 

