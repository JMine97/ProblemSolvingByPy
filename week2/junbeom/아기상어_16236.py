# 삼성 역량테스트의 대표적인 유형으로, 풀이를 눈에 익혀 놓으면 좋음. 

# idea
# 먹을 것이 많다면 가장 가까운 것부터 먹음. -> 최단거리 알고리즘을 사용해야 함. -> BFS로 최단거리를 먼저 뽑음.
# 그 다음, 먹고자 하는 고기를 먼저 찾아가야 하기 때문에 find 함수를 짬.
# 더 먹을 물고기를 찾을 수 없을 때까지 반복. 

# mistake
# 1. [i][j] 비교 연산할 때, str - int 를 비교하여 오류가 뜸. int로 받았으면 제대로 비교할 것. 
# 2. 하단 while 문 내에서만 now_x, now_y를 사용하였고 상단에서는 start_x, start_y를 사용하였는데 이것이 갱신이 되지 않아서 반영이 안됨.
# 3. 물고기를 먹을 때 크기로 계산해 낭패를 봄. 문제 잘 읽는 능력도 기를 것.
# 4. dist를 -1로 줬으면, -1이면 절대 적용이 되면 안 됨. 
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

# 상어의 위치 : 9 (시작점)
# 더 큰 상대를 지나갈 수 없음. 같은 크기는 지나갈 수 있음. 먹을 수 있는 물고기는 자기보다 작은 물고기 
# 자기 크기 만큼 물고기를 먹으면, 크기가 1 커짐. (물고기의 마리 수임. 헷갈림 주의)
# 먹을 것이 많다면 가장 가까운 것부터 먹음. -> 최단거리 알고리즘을 사용해야 함. -> BFS로 최단거리를 먼저 뽑음.
# 더 먹을 것이 없으면 종료. 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
  for j in range(n):
    if graph[i][j] == 9: # int로 input을 받았기 때문에 string으로 사용하면 인식하지 못할 수 있음.(주의) 
      now_x, now_y = i, j # 아기 상어의 위치가 시작 위치.
      graph[i][j] = 0 # 아무것도 없게끔 처리.


vol = 2 # 아기상어의 현재 크기.
exp = 0 # 아기상어의 경험치.
count = 0 # 엄마 상어를 부를 초. 

# 최단거리를 작성하는 알고리즘.
def bfs(): 
  q = deque()
  q.append((now_x, now_y))
  
  dist = [[-1] * n for _ in range(n)]
  dist[now_x][now_y] = 0 # 현재 위치(시작점)에서는 -1 -> 0. 
  
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n: # 범위 안에서만. 
        if dist[nx][ny] == -1 and graph[nx][ny] <= vol: # 물고기가 없거나 물고기가 본인이랑 사이즈가 똑같으면,
          dist[nx][ny] = dist[x][y] + 1 # 거리 +1 
          q.append((nx, ny)) 
  
  return dist

# 먹을 물고기를 찾는 함수. 
def find(dist):
  fish_x, fish_y = 0, 0
  min_dist = 1e9 # 절대값으로 초기화
  #거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다. -> 이 조건은 i, j 순서대로 진행하면 자동으로 적용.
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 0 or graph[i][j] == vol: # 나랑 같은 크기이거나 0이면 지나감. 
        continue
      if dist[i][j] != -1 and graph[i][j] < vol: # *** dist[i][j] != -1 조건 잊지 말 것!! *** dist가 -1이라는 것은 아기 상어가 접근할 수 없는 곳이라는 뜻. 
        if dist[i][j] < min_dist:
          fish_x, fish_y = i, j
          min_dist = dist[i][j] # 최단 거리 갱신

  if min_dist == 1e9: 
    return None # 먹을 물고기가 없으면, None 리턴해서 종료 준비. 
  else: 
    return fish_x, fish_y, min_dist    



while True: 
  fish = find(bfs()) # 먹을 물고기의 위치와 거리 

  if fish == None: # 먹을 물고기가 없으면 
    print(count) 
    sys.exit() # 종료 
  
  else:
    now_x, now_y = fish[0], fish[1] 
    count += fish[2]     
    exp += 1 # 경험치 상승
    if exp >= vol:
      vol += 1 # 크기 +1
      exp = 0 # 경험치 초기화 
    graph[now_x][now_y] = 0 # 물고기를 먹고 해당 자리를 0으로 바꿈.
    
