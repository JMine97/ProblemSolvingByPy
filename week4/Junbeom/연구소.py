import sys
from itertools import combinations # 라이브러리가 막힐 수도 있음. 
from collections import deque
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

z = [] # 0을 담아두는 자리. 해당 자리를 기억해 조합을 만들어 낼 예정.
t = [] # 2를 담아 두는 자리 

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0: 
      z.append([i, j])
    elif graph[i][j] == 2:
      t.append([i, j])

z = list(combinations(z, 3)) # 0이 담겨져 있는 자리 중 3개를 조합으로 만들어 냄.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0 

def bfs(start, end):
  q = deque()
  q.append([start, end])
  score_board[start][end] = 1

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if score_board[nx][ny] != 1 and temp[nx][ny] == 0:
          temp[nx][ny] = 2 
          score_board[nx][ny] = 1
          q.append([nx, ny])

for i in z:
  temp = copy.deepcopy(graph)
  s1, s2, s3 = i
  score_board = [[0]*m for _ in range(n)]
  count = 0

  s11, s12 = s1
  s21, s22 = s2
  s31, s32 = s3

  temp[s11][s12] = 1
  temp[s21][s22] = 1
  temp[s31][s32] = 1

  for j in t:
    j1, j2 = j
    bfs(j1, j2)
    
  for k in temp:
    count += k.count(0)

  result = max(result, count)

print(result)
