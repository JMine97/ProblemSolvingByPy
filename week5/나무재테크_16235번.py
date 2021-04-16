import sys
input=sys.stdin.readline

'''''
봄&여름을 한 번에 구현하고
가을&겨울을 한 번에 구현했습니다
pypy 제출로 통과했습니다.
'''''

#처음 양분 5

##봄
#자신의 나이만큼 양분 먹고 나이+1
#나이가 어린 나무부터 양분 먹음
#양분이 부족한 나무는 죽는다

##여름
#죽은 나무 -> 양분
#양분+=죽은나무 나이//2

##가을
#나이%5==0 인 나무 번식
#인접한 8개 칸에 나이가 1인 나무 생성
#범위 벗어나면 안 생김

##겨울
#a[r][c]만큼 양분 추가

#k년이 지난 후 살아남은 나무 수

n, m, k = map(int, input().split())
move=[[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1],[1, -1], [1, 0],[1, 1]]
food_add=[]
for _ in range(n):
    food_add.append(list(map(int, input().split())))
# print(food_add)
food=[[5 for _ in range(n)] for _ in range(n)]
tree=[[[] for _ in range(n)] for _ in range(n)] #양분, 나무 나이
live_tree=0
for _ in range(m):
    x, y, z = map(int, input().split()) #위치, 나무의 나이
    tree[x-1][y-1].append(z)
    live_tree+=1

for _ in range(k):
    for i in range(n):
        for j in range(n):
            tree[i][j].sort()
            tre=tree[i][j]
            live=[]
            for l in range(len(tre)):
                if tre[l]<=food[i][j]:#봄
                    food[i][j]-=tre[l]
                    live.append(tre[l]+1)

                else: #여름
                    for m in range(l, len(tre)): ##뒤에 나무 다 죽이기
                        food[i][j] += (tre[m]//2)
                        live_tree -= 1
                    break
            tree[i][j]=live

    for i in range(n):
        for j in range(n):
            tre = tree[i][j]
            for l in range(len(tre)):
                if tre[l]%5==0: #가을
                    r, c = i, j
                    for dr, dc in move:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<n and 0<=nc<n:
                            tree[nr][nc].append(1)
                            live_tree+=1

            food[i][j]+=food_add[i][j] #겨울
    # print(tree)

print(live_tree)


