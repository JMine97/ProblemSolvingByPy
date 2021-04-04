# 16928 뱀과 사다리 게임
from collections import deque

N , M = map(int, input().split())
nxt = {} #사다리 및 뱀 좌표

for _ in range(N+M):
    key, val = map(int, input().split())
    nxt[key] = val

#BFS
dist = [-1]*101 # 위치 별 이동 횟수
dist[1] = 0 #시작 위치
q= deque()
q.append(1)

while(q):
    flag = q.popleft()
    for diceNum in range(1, 7):
        nxtFlag = flag + diceNum
        if nxtFlag > 100:
            break
        if nxtFlag in nxt:
            nxtFlag = nxt[nxtFlag]
        if dist[nxtFlag] == -1:
            dist[nxtFlag] = dist[flag] + 1
            q.append(nxtFlag)

print(dist)