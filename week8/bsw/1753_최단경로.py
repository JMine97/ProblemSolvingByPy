V, E = map(int, input().split())
s = int(input())

# 시간초과

graph = {}
for _ in range(E):
    start, end, cost = map(int, input().split())

    if start not in graph:
        graph[start] = [(end, cost)]
    else:
        graph[start].append((end, cost))

distance = [999999999]*(V+1)
distance[s] = 0

from collections import deque
q=deque([s])
# print(graph)
# print(distance)
while q:
    cur = q.popleft()

    if cur not in graph:
        continue
    for next, cost in graph[cur]:
        if distance[next] < distance[cur] + cost:
            continue
        distance[next] = min(distance[next], distance[cur] + cost)
        q.append(next)

for i in range(1, V+1):
    if distance[i] == 999999999:
        print('INF')
    else:
        print(distance[i])