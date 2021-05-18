a, b = map(int, input().split())
N, M = map(int, input().split())

graph={}
# 치환이므로 양방향 통행 가능
for _ in range(M):
    x, y = map(int, input().split())

    if x not in graph:
        graph[x] = []
    if y not in graph:
        graph[y] = []
    
    graph[x].append(y)
    graph[y].append(x)

print (graph)

from collections import deque

q=deque([a])
distance = [-1]*(N+1)
distance[a] = 0

while q:
    cur = q.popleft()

    if cur not in graph:
        continue
    for next in graph[cur]:
        if distance[next] == -1:
            q.append(next)
            distance[next] = distance[cur] + 1

print(distance[b])

