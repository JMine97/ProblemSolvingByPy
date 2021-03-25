import sys
from heapq import heappop, heappush
input=sys.stdin.readline

n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]
q = []  # 거리, row, col
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            heappush(q, [0, i, j])
            graph[i][j]=0
            break
size = 2
cnt=0
feed=0
visit = [[False] * n for _ in range(n)]
while q:
    d, r, c = heappop(q)

    if 0<graph[r][c]<size:
        feed+=1
        if feed==size:
            size+=1
            feed=0
        cnt+=d
        d=0
        graph[r][c]=0
        if len(q)!=0:
            q=[]
        visit = [[False] * n for _ in range(n)]
    for dr, dc in [-1, 0], [1, 0], [0, -1], [0, 1]:
        next_r = r + dr
        next_c = c + dc
        if 0 <= next_r < n and 0 <= next_c < n and not visit[next_r][next_c] and graph[next_r][
            next_c] <= size:  # 그래프 범위 안, 아기상어보다 작으면
            heappush(q, [d + 1, next_r, next_c])
            # 크기가 같으면
            visit[next_r][next_c] = True

print(cnt)
