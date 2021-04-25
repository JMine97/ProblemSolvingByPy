n, m, k = map(int, input().split())
soil = [[5]*n for _ in range(n)] # 초기값 
a = [] # 겨울마다 줄 양분 
for _ in range(n):
    a.append(list(map(int, input().split())))
tree = [[[] for _ in range(n)] for _ in range(n)]


for _ in range(m):
    x,y,z = map(int, input().split())
    tree[x-1][y-1].append(z)

dx = [-1, 0, 1, 0, 1, 1, -1, -1]
dy = [0, -1, 0, 1, 1, -1, 1, -1]
# 봄 : 자신의 나이만큼 양분을 먹고 나무가 있는 곳의 양분만 먹을 수 있음. 못먹으면 죽음, 나이가 어린 묘목부터 양분을 얻음. 
# 여름 : 죽은 나무가 양분으로 변함 
# 가을 : 8방향으로 번식
# 겨울 : 양분을 더해줌
for _ in range(k):
    # 봄
    for i in range(n):
        for j in range(n):
            if len(tree[i][j]) <= 0 : continue
            tree[i][j].sort() # 나이가 어린 묘목부터 양분을 얻게 하기 위해 sort
            idx = 0
            while idx < len(tree[i][j]):
                if soil[i][j] >= tree[i][j][idx]:
                    soil[i][j] -= tree[i][j][idx]
                    tree[i][j][idx] += 1
                    idx += 1
                else: 
                    dead = tree[i][j][idx:] # 여름. 죽은 나무들은 양분이 된다.
                    for now in dead:
                        soil += (now//2) # 양분이 되어 더해짐. 
                    tree[i][j] = tree[i][j][:idx] # 남은 나무들만 다시 넣어줌. 
                    
    # 가을 
    for i in range(n):
        for j in range(n):
            cnt = 0
            if tree[i][j]:
                for now in tree[i][j]:
                    if now%5 == 0: # 5의 배수이면 번식 
                        cnt += 1
            if cnt > 0:
                for idx in range(8):
                    nx = i + dx[idx]
                    ny = j + dy[idx]

                    if 0 <= nx < n and 0 <= ny < n:
                        for _ in range(cnt):
                            tree[nx][ny].append(1)
    # 겨울
    for i in range(n):
        for j in range(n):
            soil[i][j] += a[i][j]

ans=0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])
print(ans)
