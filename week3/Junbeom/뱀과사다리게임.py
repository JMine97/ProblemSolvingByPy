# 작은 input (15, 15) 넉넉한 메모리 (512) -> 탐색 가능 (bfs or dfs)

from collections import deque

n, m = map(int, input().split()) # n : ladder / m : snake 
# graph = [*range(101)]
graph = list(range(101))
dist = [-1]*101
dist[1] = 0 # 시작점 
for _ in range(n+m): #  
  a, b =  map(int, input().split())
  graph[a] = b

q = deque()
q.append(1)

while q:
  now = q.popleft()
  
  for i in range(1,7):
    nxt = now+i
    if nxt > 100: break
    nxt = graph[nxt] 
    if dist[nxt] == -1 or dist[nxt] > dist[now]+1: # 방문을 안했거나, 방문을 했지만 갱신되는 값이 더 좋은 효율일 때 
      dist[nxt] = dist[now] + 1 
      q.append(nxt)

print(dist[-1])
