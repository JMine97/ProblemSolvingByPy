 # 시간 제한 1초, 메모리 256MB. input은 1000이나 되기 때문에 단순 BFS이 가능한 지는 모르겠음. 
 

 # idea
 # 탐색으로 풀어야 함.
 # 근데 풀다 보니까 DP가 됨.(DP + BFS) -> 오른쪽으로 갈수록 무조건 값이 커질 수 밖에 없기 때문. 
 # -1이 나오는 경우도 생각해보자.  -> 0이 나타날 때.

import sys
from collections import deque

n = int(input())
li = list(map(int, input().split()))

dist = [-1]*n # 끝자리가 -1이면 결국 닿지 못하고 종결. 

q = deque()
q.append(0)

dist[0] = 0

while q:
  now = q.popleft() # 인덱스 
  jump = li[now] # 현재 자리에서 점프할 수 있는 최대 거리. 
  for i in range(jump, 0, -1): # 최대 거리에서 한 칸씩 줄이면서 탐색. 
    if now+i < n and dist[now+i] == -1: # now+i는 인덱스, dist[now+i]는 해당 자리를 들린 수. -> 아직 들리지 않았으면,  
      dist[now+i] = dist[now] + 1 # 해당 자리를 전 자리+1 
      q.append(now+i) # 새로운 자리를 큐에 추가 


print(dist[-1]) # 마지막 인덱스 출력. -1이면 닿지 못한 것. 

