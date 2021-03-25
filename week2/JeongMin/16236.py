import sys
from heapq import heappop, heappush
from collections import deque

input = sys.stdin.readline


def bfs():
    # 거리를 알기 위한 완전탐색
    m = deque()  # 움직일 좌표를 담아두는 m
    m.append([0, shark[0], shark[1]])
    visit = [[False] * n for _ in range(n)]
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visit[shark[0]][shark[1]] = True
    while m:
        dist, row, col = m.popleft()
        for i in range(4):
            next_r = row + move[i][0]
            next_c = col + move[i][1]
            if 0 <= next_r < n and 0 <= next_c < n and not visit[next_r][next_c] and graph[next_r][next_c] <= size:  # 그래프 범위 안
                if 0 < graph[next_r][next_c] < size:  # 먹을 수 있는 물고기들 담음
                    heappush(q, [dist + 1, next_r, next_c])
                # 크기가 같으면
                visit[next_r][next_c] = True
                m.append([dist + 1, next_r, next_c])


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 아기상어가 있는 위치
shark = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark.append(i)
            shark.append(j)
            graph[i][j] = 0
size = 2
q = []  # 먹을 수 있는 물고기들을 담아두는 q(거리, row, col)
cnt = 0
feed = 0
while True:
    bfs()  # 먹을 수 있는 물고기들을 담아온다
    if not q:
        break
    # 가장 거리가 짧고 위에, 왼쪽에 있는 물고기 먹음
    dist, r, c = heappop(q)
    cnt += dist
    shark[0], shark[1] = r, c
    graph[r][c] = 0
    feed += 1
    q = []
    if feed == size:
        size += 1
        feed = 0
print(cnt)