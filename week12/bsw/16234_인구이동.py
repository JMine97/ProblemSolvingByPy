
N, L, R = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

from collections import deque

cnt=0
while 1:
    flag = True
    visited = []
    
    for i in range(N):
        for j in range(N):
            union = [(i,j)] # 연합국 
            visited.append((i,j)) # 방문 국가 != 연합국
                                  # 따로 처리해야한다
            q=deque([(i,j)])
            summ = graph[i][j]
            while q:
                r, c = q.popleft()
                
                for dr, dc in (1,0), (0,1), (0,-1), (-1,0):
                    nr, nc = r+dr, c+dc

                    if (nr,nc) in visited:
                        continue
                    if nr<0 or N<=nr or nc<0 or N<=nc:
                        continue
                    if R < abs(graph[nr][nc]-graph[r][c]) or abs(graph[nr][nc] - graph[r][c]) < L:
                        continue
                    union.append((nr,nc))
                    q.append((nr,nc))
                    visited.append((nr,nc))
                    summ += graph[nr][nc]
    
            if len(union) == 1:
                continue
            
            avg = summ//len(union)
            for r,c in union:
                graph[r][c] = avg
            flag = False

    if flag:
        break
    cnt+=1

print(graph)
print(cnt)
