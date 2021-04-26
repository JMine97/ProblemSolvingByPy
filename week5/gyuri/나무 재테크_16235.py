# 나무 재테크_16235
# N * N 크기의 땅
# (r, c)
# 가장 처음에 양분은 모든 칸에 5만큼 들어 있다.
# M개의 나무

# 봄 -> 자신의 나이만큼 양분을 먹고, 나이가 1 증가
# 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다
# 땅에 양분이 부족해 자신의 나이 만큼 양분을 먹을 수 없으면 나무는 죽는다.

# 여름 -> 봄에 죽은 나무가 양분으로, 나이//2

# 가을 -> 나무가 나이 % 5 == 0, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.

# 겨울 -> A[r][c]양의 양분 추가
import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
nut = [[5]*n for _ in range(n)]
tree = []
dead = deque()
for _ in range(m):
    x, y, z = map(int, input().split())
    tree.append([z, x-1, y-1])

def spring():
    # 자신의 나이만큼 양분을 먹고, 나이가 1 증가
    tree.sort
    for i in range(len(tree)):
        # 양분 먹기
        if tree[i][0] != 0:
            if tree[i][0] <= nut[tree[i][1]][tree[i][2]]:
                nut[tree[i][1]][tree[i][2]] -= tree[i][0]
                tree[i][0] += 1
            else :
                dead.append(tree[i])
def summer():
    while dead:
        p = dead.pop()
        nut[p[1]][p[2]] += (p[0] // 2)

def fall():
    dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for i in range(len(tree)):
        # 양분 먹기
        if tree[i][0] != 0:
            x = tree[i][1]
            y = tree[i][2]
            if tree[i][0] % 5 == 0:
                for i ,j in dir:
                    nx = x + i
                    ny = y + j
                    if 0 <= nx < n and 0 <= ny < n:
                        tree.append([1, nx, ny])

def winter():
    for i in range(len(tree)):
        if tree[i][0] != 0:
            x = tree[i][1]
            y = tree[i][2]
            nut[x][y] += a[x][y]

for year in range(k):
    # 봄이랑 여름 같이
    spring()
    summer()
    fall()
    winter()
num = 0
for i in range(len(tree)):
    if tree[i][0] != 0:
        num+=1
print(num)
