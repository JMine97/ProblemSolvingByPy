# 14503_로봇 청소기.py
'''
로봇 청소기가 청소하는 영역
N * M
현재 좌표와 방향이 입력되면 청소할 수 있는지 확인
청소할 수 있으면 0 -> 2로 바꾸고 cnt += 1을 더한다
(현재 방향 + 3) % 4가 왼쪽 방향이다.
뒤로 이동 : (현재 방향 + 2) % 4

'''
import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, d):
    global ans
    if a[x][y] == 0:
        a[x][y] = 2
        ans += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if a[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if a[nx][ny] == 1:
        return
    clean(nx, ny, d)


n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
clean(x, y, d)
print(ans)
