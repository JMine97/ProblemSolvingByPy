#15686번_치킨 배달
# 크기 N * N
# 빈칸0 or 집1 or 치킨집2
# (r, c) 1부터 시작
# 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리 = 모든 집의 치킨 거리의 합
# |r1 - r2| + |c1 - c2|
# M개의 치킨 집 나머지는 폐업

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int , input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 순서
# 각 집의 치킨거리를 구하고
# 치킨 집 중에서 관련없는 치킨 집 폐업
# 폐업당한 치킨집으로 인한 치킨거리 다시 갱신하기
def dfs_total(x, y):
    dir = [[0,1], [1,0], [0,-1], [-1,0]]
    deq = deque()
    deq.append([x,y])
    visit = [[0] * n for _ in range(n)]
    while deq:
        r, c = deq.pop()
        for i, j in dir:
            if 0<=r+i<n and 0<=c+j<n:
                if visit[r+i][c+j] == 1:
                    continue
                if arr[r+i][c+j] == 2:
                    dist[r+i][c+j] += abs(x - (r+i)) + abs(y - (c+j))
                deq.append([r+i, c+j])
                visit[r + i][c + j] = 1

def dfs(x,y):
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    deq = deque()
    deq.append([x, y])
    dist = [[INF] * n for _ in range(n)]
    visit = [[0] * n for _ in range(n)]
    while deq:
        r, c = deq.pop()
        for i, j in dir:
            if 0 <= r + i < n and 0 <= c + j < n:
                if visit[r + i][c + j] != 0:
                    continue
                if arr[r + i][c + j] == 2:
                    dist[x][y] = min(abs(x - (r + i)) + abs(y - (c + j)), dist[x][y])
                deq.append([r + i, c + j])
                visit[r + i][c + j] = 1

    return dist[x][y]

# 1. 각집의 치킨거리 구하기
INF = int(1e9)
dist = [[0] * n for _ in range(n)]
c = [[INF] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            dfs_total(i,j)

# 2. 폐업 하기
total_dist = []
for i in range(n):
    for j in range(n):
        if dist[i][j] != 0:
            total_dist.append(dist[i][j])

if len(total_dist) > m:
    # 폐업하기
    cnt = len(total_dist)
    total_dist.sort()
    total_dist = total_dist[m:]
    print(total_dist)
    for i in range(n):
        for j in range(n):
            if dist[i][j] in total_dist:
                arr[i][j] = 0
                cnt -= 1
            if cnt == m :
                break

# 3. 최단 경로 구하기
answer = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            answer += dfs(i,j)

print(answer)
