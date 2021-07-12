N,M,T = map(int, input().split())
INF = 1e9
graph = [list(map(int, input().split())) for _ in range(N)]
times = [[INF for _ in range(M)] for _ in range(N)]
times[0][0] = 0
# print(times)
# print('')

from collections import deque
q=deque()

# r, c
q.append((0, 0))
answer2=1e9
while q:
    r, c = q.popleft()

    for dr, dc in (1,0), (0,1), (-1,0), (0,-1):
        nr, nc = r + dr, c + dc

        if 0<=nr<N and 0<=nc<M:

            if times[nr][nc] != 1e9:
                continue

            if graph[nr][nc] == 1:
                continue
            
            # 칼
            if graph[nr][nc] == 2:
                answer2 = times[r][c] + 1 + ((N-1)-nr) + ((M-1)-nc)
            

            q.append((nr,nc))
            times[nr][nc] = times[r][c] + 1

# print(graph)
# print(times)

times[N-1][M-1] = min(times[N-1][M-1], answer2)

if times[N-1][M-1] > T:
    print('Fail')
else:
    print(times[N-1][M-1])
