from collections import deque

n, m, t = map(int, input().split())
graph=[] #0 빔, 1 벽, 2 그람
for _ in range(n):
    graph.append(list(map(int, input().split())))

#최단 거리 vs 그람까지 최단 거리 + 그람에서 도착지까지 최단거리
def bfs():
    tmp=float('inf')
    q=deque()
    q.append([0, 0])
    visited=[[0]*m for _ in range(n)]

    while q:
        r, c=q.popleft()
        if graph[r][c]==2:
            tmp=visited[r][c]+abs(n-1-r)+abs(m-1-c)
        if r==n-1 and c==m-1:
            return min(visited[r][c], tmp)
        for dr, dc in [0, -1], [0, 1], [1, 0], [-1, 0]:
            nr, nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<m and graph[nr][nc]!=1 and not visited[nr][nc]:
                q.append([nr, nc])
                visited[nr][nc]=visited[r][c]+1
    return tmp

result=bfs()

if result<=t:
    print(result)
else:
    print("Fail")
