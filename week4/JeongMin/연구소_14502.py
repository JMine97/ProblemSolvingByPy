import sys
import copy
from collections import deque
input=sys.stdin.readline

n, m = map(int, input().split()) #가,세
#0빈칸, 1벽, 2바이러스
map=[list(map(int, input().split())) for _ in range(n)]
virus=deque()
zero=deque()
#바이러스의 위치를 저장해 놓는다
for i in range(n):
    for j in range(m):
        if map[i][j]==2:
            virus.append((i, j))
        elif map[i][j]==0:
            zero.append((i, j))
max_safe=0

def bfs():
    cmap=copy.deepcopy(map)
    cvirus=copy.deepcopy(virus)
    #바이러스 퍼뜨리기
    while cvirus:
        r, c=cvirus.popleft()
        for dr, dc in [0, -1], [0, 1], [1, 0],[-1, 0]:
            nr, nc=r+dr, c+dc
            if 0<=nr<n and 0<=nc<m and not cmap[nr][nc]:
                cvirus.append((nr, nc))
                cmap[nr][nc]=2

    cnt=0
    #안전영역 구하기
    for i in range(n):
        for j in range(m):
            if cmap[i][j]==0:
                cnt+=1
    global max_safe
    max_safe=max(max_safe, cnt)

#벽을 세울 수 있는 경우
def wall(cnt, s):
    if cnt==0:
        #바이러스 검사
        bfs()
        return
    for i in range(s, len(zero)):
        r=zero[i][0]
        c=zero[i][1]
        map[r][c]=1
        wall(cnt-1, i+1)
        map[r][c]=0


wall(3, 0)
print(max_safe)