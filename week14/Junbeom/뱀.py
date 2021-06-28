# 3190 뱀
# idea : 1. 자신에 부딪히면 안되므로 뱀을 2로 부여해서 조건을 넣는다. 2. 시간이 되면 방향을 바꿔주어야 하는데 방향벡터로 시계방향 반시계방향을 만들어 놓는다. 3. 덱으로 뱀의 길이조절을 한다. 
import sys
from collections import deque


# index - 0: 북, 1: 동, 2: 남, 3: 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
board = [[0] * N for _ in range(N)]
for _ in range(K):
  a, b = map(int, sys.stdin.readline().split())
  board[a-1][b-1] = 1  # 사과 1로 저장

L = int(sys.stdin.readline())

times = {} # dictionary

for i in range(L):
  X, C = sys.stdin.readline().split()
  times[int(X)] = C

dir = 1  # 초기의 방향 - default
time = 1  # 시간
y = x = 0
snake = deque([[y, x]])  # 방문 위치
board[y][x] = 2 # 뱀은 2로 표시

while True:
  y, x = y + dy[dir], x + dx[dir]
  if 0 <= y < N and 0 <= x < N and board[y][x] != 2: # 보드 안에 있거나, 자신을 만나지 않는 경우 
    if board[y][x] == 0:  # 사과가 없는 경우
      tail_y, tail_x = snake.popleft() # 꼬리를 미리 떼서 뱀 크기 유지
      board[tail_y][tail_x] = 0  # 꼬리 제거
    
    board[y][x] = 2 # 진행방향은 뱀으로 바꿈
    snake.append([y, x]) # 늘려줌. 
    if time in times.keys(): # 방향을 바뀔 시간이 되면, 
      if times[time] == "D" : # Default일 때
        dir = (dir+1) % 4 # overflow 방지해서 modulo 사용
      else: # Left일 때
        dir = (dir+3) % 4 
    
    time += 1
  else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우 종료. 
    print(time)
    exit(0)


  


