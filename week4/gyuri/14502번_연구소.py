# 14502번_연구소.py
'''
문제 요약
바이러스 확산을 막기 위해 벽 세우기
'''
import sys
import copy
from collections import deque

input = sys.stdin.readline
dx=[1,-1,0,0]
dy=[0,0,1,-1]
ans = 0
empty_list = []
virus_list = []
EMPTY = 0
WALL = 1
VIRUS = 2

def bfs():
    # 바이러스가 얼마나 퍼졌는지 check하는 함수
    global ans
    w = copy.deepcopy(a)
    for v in virus_list:
        q.append(v)

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if w[nx][ny] == EMPTY:
                    w[nx][ny] = VIRUS
                    q.append([nx, ny])
    cnt = 0
    for i in w:
        cnt += i.count(0)
    ans = max(ans, cnt)

def wall():
    # 새로 세울 수 있는 벽의 개수는 3
    # 모든 경우의 수를 확인
    print(len(empty_list))
    # 안전한 지역에다가 벽 3개를 세워야 하기 때문에, 안전한 지역 3개의 조합을 싹다 뽑음
    # empty_list = list(combinations(empty_list, 3)) 으로 대체 가능 
    for i in range(len(empty_list)):
        for j in range(i):
            for k in range(j):
                # 3개의 벽을 만든다
                # print(i,j,k)
                x1, y1 = empty_list[i]
                x2, y2 = empty_list[j]
                x3, y3 = empty_list[k]

                a[x1][y1] = WALL
                a[x2][y2] = WALL
                a[x3][y3] = WALL

                bfs()

                a[x1][y1] = EMPTY
                a[x2][y2] = EMPTY
                a[x3][y3] = EMPTY

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == EMPTY:
            empty_list.append([i, j])
        if a[i][j] == VIRUS:
            virus_list.append([i, j])

q = deque()
wall()
print(ans)
