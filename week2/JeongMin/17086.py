n, m=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
#8방향으로 움직임
move=[[-1, 0], [1, 0], [0, 1],[0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
q=[]
for i in range(n):
    for j in range(m):
        # 상어가 있는 위치를 큐에 넣는다
        if arr[i][j]:
            q.append((i, j, 0))

result=0
while q:
    row, col, cnt = q.pop(0)
    for i in range(len(move)):
        n_r=row+move[i][0]
        n_c=col+move[i][1]

        # 카운트 된 칸은 계산하지 않는다
        if 0<=n_r<n and 0<=n_c<m and not arr[n_r][n_c]:
            arr[n_r][n_c] = cnt+1
            q.append((n_r, n_c, cnt+1))
            if result<cnt+1:
                result=cnt+1
print(result)