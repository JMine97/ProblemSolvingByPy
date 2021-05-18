import sys
input = sys.stdin.readline

#시간초과
# heap사용 -> why?
N = int(input())
M = int(input())

graph = {}
cost = [[-1 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())

    cost[s][e] = c
    
    if s not in graph:
        graph[s] = [e]
        continue
    graph[s].append(e)

#print(graph)
#print(cost)

start, end = map(int,input().split())
#1 2 4 / 2 2 
#1 3 4 / 3 1
from collections import deque

q=deque([start])
distance = [-1]*(N+1)
distance[start] = 0

while q:
    cur = q.popleft()

    if cur not in graph:
        continue
    for next in graph[cur]:
        if distance[next] == -1:    
            distance[next] = distance[cur] + cost[cur][next]
        else:
            distance[next] = min(distance[next], distance[cur] + cost[cur][next])
        q.append(next)

print(distance[end])