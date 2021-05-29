# 1261번_알고스팟.py
'''
N * M 크기
운영진은 모두 같은 방에 있어야 한다.
최소로 벽 부수어  n,m로 이동
모든 경우의 수
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(m)]
d_x = [-1,1,0,0]
d_y = [0,0,-1,1]
d = [[INF] * n for _ in range(m)]

# 백트래킹?
# 일단 최단 경로를 구하자
q = []
heapq.heappush(q, (0,0,0))
d[0][0] = 0
while q:
    cost, x, y = heapq.heappop(q)
    if d[x][y] < cost :
        continue
    for i, j in zip(d_x, d_y):
        xi = x + i
        yj = y + j
        if 0 <= xi < m and 0 <= yj < n:
            # 빈 방
            if d[xi][yj] > cost + graph[xi][yj]:
                d[xi][yj] = cost + graph[xi][yj]
                heapq.heappush(q, (d[xi][yj], xi, yj))

print(d[-1][-1])
