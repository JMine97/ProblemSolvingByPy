# 16948 데스 나이트
# (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동
# N * N, (r1, c1) -> (r2, c2)

# 풀이
# 최단 경로
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
dist = [[-1] * n for _ in range(n)]
deq = deque()
deq.append([r1, c1])
dist[r1][c1] = 0

d_x = [-2,-2, 0, 0, 2, 2]
d_y = [-1, 1,-2, 2,-1, 1]
while deq:
  x,y = deq.popleft()
  for i, j in zip(d_x,d_y):
    px = i + x
    py = j + y
    if 0 <= px < n and 0 <= py < n:
      if dist[px][py] == -1:
        dist[px][py] = dist[x][y] + 1
        deq.append([px, py])
      elif dist[px][py] > dist[x][y] + 1:
        dist[px][py] = dist[x][y] + 1
        deq.append([px, py])

print(dist[r2][c2])
