import sys
input = sys.stdin.readline

N, D = map(int, input().split())

graph = {}
graph_cost = {}
for _ in range(N):
    start, end, cost = map(int, input().split())
    if end>D:
        continue

    if start not in graph:
        graph[start] = [(end, cost)]
    else:
        graph[start].append((end, cost))
        
#print(graph)

#distance = [0]*(D+1)
distance = [i for i in range(D+1)]

#print(distance)

for i in range(D+1):
    if distance[i] != 0:
        distance[i] = min(distance[i], distance[i-1]+1)
    if i not in graph:
        continue
    for next, cost in graph[i]:
        if distance[next] > distance[i] + cost:    
            distance[next] = distance[i] + cost

print(distance[D])