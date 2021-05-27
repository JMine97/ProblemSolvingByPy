import sys
import heapq as hq

input = sys.stdin.readline
INF = 10 ** 9

m, n = map(int, input().split())
maze = []

for _ in range(n):
    maze.append(list(map(int, list(input().strip()))))

q = []
hq.heappush(q, (0, 0, 0))
wall = [[INF] * m for _ in range(n)]
wall[0][0]=0

while q:
    wall_cnt, r, c = hq.heappop(q)

    for dr, dc in [1, 0], [-1, 0], [0, 1], [0, -1]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < m:
            cost = wall_cnt + maze[nr][nc]
            if wall[nr][nc] > cost:
                hq.heappush(q, (cost, nr, nc))
                wall[nr][nc] = cost

print(wall[-1][-1])
