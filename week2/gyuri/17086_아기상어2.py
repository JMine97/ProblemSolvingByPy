# n*m 크기의 공간
# 어떤 칸의 안전 거리 : 그 칸과 가장 거리가 가까운 아기 상어와의 거리 (대각선포함)

from collections import deque

n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
deq = deque()
d_x = [-1,1,0,0,-1,1,-1,1]
d_y = [0,0,-1,1,-1,1,1,-1]

for i in range(n):
    for j in range(m):
        if a[i][j]:
            deq.append([i,j])

while deq:
    x,y = deq.popleft()
    for i,j in zip(d_x, d_y):
        if 0<=x + i<n and 0<=y + j<m:
            if not a[x+i][y+j]:
                deq.append([x+i,y+j])
                a[x+i][y+j] = a[x][y] + 1

#print(a)
print(max(map(max, a))-1)

# appendleft , append 확인하면서 사용하기!
