# 16235 나무 재테크

N, M, K = map(int, input().split())

food = [[5 for _ in range(N)] for _ in range(N)]
addfood = [list(map(int, input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]


for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)


def addFood():
    for i in range(N):
        for j in range(N):
            food[i][j] += addfood[i][j]


# print(food)
# print(tree)

for _ in range(K):
    # 나무 크기 정렬
    for i in range(N):
        for j in range(N):
            tree[i][j].sort()
    
    # 봄, 여름
    for i in range(N):
        for j in range(N):
            flag = 10
            for l in range(len(tree[i][j])):
                if tree[i][j][l] <= food[i][j]:
                    food[i][j] -= tree[i][j][l]
                    tree[i][j][l] += 1
                else:
                    flag = min(flag, l)
                    food[i][j] += tree[i][j][l] // 2
            tree[i][j] = tree[i][j][:flag]


    # 가을
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(N):
        for j in range(N):
            for l in range(len(tree[i][j])):
                if tree[i][j][l] % 5 ==0:
                    for d in range(8):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if 0<=nx<N and 0<=ny<N :
                            tree[nx][ny].append(1)
    
    # 겨울
    addFood()



print(tree)
print(food)


ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])
print(ans)

'''
3 1 15
100 100 100 
100 100 100
100 100 100
1 1 1

[[[4, 4, 4, 4, 4, 4, 8, 8, 8, 16], [2, 4, 4, 4, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 8, 8]], 
 [[2, 4, 4, 4, 4, 4, 4, 4, 4, 4], [2, 4, 4, 4, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 4, 4, 4, 8]], 
 [[4, 4, 4, 4, 4, 4, 8, 8], [4, 4, 4, 4, 4, 4, 4, 4, 4, 8], [4, 4, 4, 4, 4, 4, 8]]]

[[1265, 1358, 1413], 
 [1358, 1353, 1408], 
 [1413, 1408, 1441]]
83

'''