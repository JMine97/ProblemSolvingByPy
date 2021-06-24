n, m = map(int, input().split())
r, c, d = map(int, input().split()) #북 동 남 서
graph=[] #0 빈칸, 1 벽, 2 청소함
for _ in range(n):
    graph.append(list(map(int, input().split())))

move=[[-1, 0],[0, 1], [1, 0], [0, -1]]
graph[r][c]=2
ret=1

while 1:
    cnt=0
    for _ in range(4):
        d-=1
        if d<0: d=3
        nr, nc = r+move[d][0], c+move[d][1]
        if 0<=nr<n and 0<=nc<m and graph[nr][nc]==0:
            r, c = nr, nc
            graph[r][c] = 2
            ret+=1
            break
        cnt+=1

    tmp_d=d
    if cnt==4:
        tmp_d-=2
        if tmp_d<0:
            tmp_d=4+tmp_d
        nr, nc = r + move[tmp_d][0], c + move[tmp_d][1]
        if 0<=nr<n and 0<=nc<m and graph[nr][nc]!=1: #후진을 할 수 있는 경우
            r, c = nr, nc
            continue
        break
print(ret)