import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
r1, c1, r2, c2 = map(int, input().split())
visited=[[False]*n for _ in range(n)]

def bfs(r1, c1, r2, c2):
    move=[[-2, -1],[-2,1],[0,-2],[0,2],[2,-1],[2,1]]
    q=deque()
    q.append([r1, c1, 0])
    visited[r1][c1]=True
    while q:
        r, c, cnt=q.popleft()
        for i in range(6):
            nr=r+move[i][0]
            nc=c+move[i][1]
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                if nr==r2 and nc==c2:
                    print(cnt+1); return 1
                q.append([nr, nc, cnt+1])
                visited[nr][nc]=True
    return 0
ret = bfs(r1, c1, r2, c2)
if not ret:
    print(-1)
