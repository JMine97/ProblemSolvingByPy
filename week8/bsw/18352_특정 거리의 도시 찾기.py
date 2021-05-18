# readline으로 풀면 시간초과 안남
import sys
input = sys.stdin.readline

N, M, K, start = map(int, input().split())

#### 그래프
dic=dict()
for _ in range(M):
    key, val = map(int, input().split())

    if key not in dic:
        dic[key] = [val]
        continue
    dic[key].append(val)

print(dic)
# {1: [2, 3], 
#  2: [3, 4]}

#### 순회
from collections import deque
q=deque([start])
dist = [-1]*(N+1)
dist[start] = 0
while q:
    cur = q.popleft()
    
    if cur not in dic:
        continue
    for next in dic[cur]:
        # BFS 탐색이기 때문에 next 노드에는 항상 start와의 최소거리가 저장됨
        if dist[next] == -1:
            # 방문한 노드인 경우 재탐색하지 않는다
            q.append(next)
            dist[next] = dist[cur] + 1


if K not in dist:
    print(-1)
    exit()

for i in range(1, len(dist)):
    if dist[i] == K:
        print(i)
