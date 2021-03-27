import sys
from collections import deque
input=sys.stdin.readline

n,m,k =map(int, input().split()) #벽 k개까지 부숨
graph=[list(map(int, input().rstrip())) for _ in range(n)]
visited=[[[False]*(k+1) for _ in range(m)] for _ in range(n)]

def bfs():
    q=deque()
    q.append((1, 0, 0, 0)) #지난시간, 부순벽의 수, 현재 인덱스 row,col
    visited[0][0][0]=True
    day=True
    while q:
        p=len(q)
        for _ in range(p):
            time, cnt, row, col = q.popleft()
            if row==n-1 and col==m-1:
                return time

            for dr, dc in [-1, 0], [0, 1], [1, 0], [0, -1]:
                next_r=row+dr
                next_c=col+dc
                # print(next_r, next_c)
                #범위
                if next_r<0 or next_r>=n or next_c<0 or next_c>=m:
                    continue
                # print(next_r, next_c, cnt)
                if graph[next_r][next_c]==1 and cnt<k and not visited[next_r][next_c][cnt+1]:
                    if day:#벽이고 낮이면 부숨
                        visited[next_r][next_c][cnt + 1] = True
                        q.append((time + 1, cnt + 1, next_r, next_c))
                    else: #벽이고 밤이면 기다림
                        q.append((time + 1, cnt, row, col))
                elif graph[next_r][next_c] == 0 and not visited[next_r][next_c][cnt]:
                    q.append((time + 1, cnt, next_r, next_c))
                    visited[next_r][next_c][cnt]=True
        day=not day
    return -1

print(bfs())