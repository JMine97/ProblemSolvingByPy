from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

def check(x1, y1, x2, y2):
    if abs(x1 - x2) + abs(y1 - y2) > 1000:
        return False
    elif abs(x1 - x2) + abs(y1 - y2) <= 1000:
        return True

for _ in range(T):
    n = int(input())

    point = []
    graph = {}
    
    #정점
    for _ in range(n+2):
        x, y = map(int, input().split())
        point.append((x,y))

    for i in range(n+2):
        x1, y1 = point[i]
        for j in range(n+2):
            if i==j:
                continue
            x2, y2 = point[j]

            if check(x1, y1, x2, y2):
                if not (x1, y1) in graph:
                    graph[(x1, y1)] = []
                graph[(x1, y1)].append((x2, y2))

    
    q = deque()
    visited = {}

    q.append(point[0])
    for p in point:
        visited[p] = 0
    visited[point[0]] = 1

    while q:
        x, y = q.popleft()

        if (x, y) not in graph:
            continue
        for nx, ny in graph[(x, y)]:
            if visited[(nx, ny)] == 1:
                continue
            q.append((nx, ny))
            visited[(nx, ny)] = 1

    if visited[point[-1]] == 1:
        print('happy')
    elif visited[point[-1]] == 0:
        print('sad')


            




    