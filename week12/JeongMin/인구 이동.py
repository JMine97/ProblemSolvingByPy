from collections import deque

n, L, R = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

'''
L이상 R이하

변수명 중복되지 않게 짓기

반례
6 25 43
24 27 20 31 24 26 
29 94 31 36 28 9 
19 43 55 6 66 76 
57 38 31 42 90 83 
40 11 1 86 8 40 
100 85 48 89 67 61 
'''
cnt=0
while True: #BFS 탐색
    visit = [[False] * n for _ in range(n)]
    flag = True
    for mr in range(n):
        for mc in range(n):
            if not visit[mr][mc]:
                q = deque()
                q.append((mr, mc)) #탐색할 좌표
                req=[(mr, mc)] #생성된 연합의 좌표
                visit[mr][mc]=True
                sumv = a[mr][mc] #생성된 연합의 합
                while q:
                    r, c = q.popleft()
                    for dr, dc in [-1, 0], [1, 0], [0, -1], [0, 1]:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < n and 0 <= nc < n and not visit[nr][nc]:
                            if L<=abs(a[nr][nc]-a[r][c])<=R:
                                visit[nr][nc] = True
                                q.append((nr, nc))
                                req.append((nr, nc))
                                sumv += a[nr][nc]
                if len(req)>1:
                    flag=False #인구이동이 있었는지 없었는지 판별하는 식별자
                    avg=sumv//len(req)
                    for qr, qc in req: #생성된 연합에 속한 연합국들 인구 갱신
                        a[qr][qc]=avg
    if flag:
        break
    cnt += 1
print(cnt)
