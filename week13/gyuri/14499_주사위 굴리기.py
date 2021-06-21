# 주사위 굴리기
# 크기 n * m 지도
# (r, c)
# 윗면: 1 동쪽: 3 놓여져있는 곳의 좌표: (x,y)
# 주사위를 굴려 0이면 : 주사위 바닥면에 쓰여있는 수가 복사
# 주사위를 굴려 0이 아니면 : 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되고 칸은 0이 된다.
# 주사위를 놓은 곳의 좌표와 이동시키는 명령 : 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램
# 지도 밖으로 나가는 명령은 무시
import sys
input = sys.stdin.readline
n, m, x, y, k = map(int , input().split())
# n * m 지도
arr = [list(map(int, input().split())) for _ in range(n)]
op = list(map(int, input().split()))
# 동1 서2 북3 남4
dice = [0] * 7
# dice[1] - dice[6], dice[2] - dice[5], dice[3] - dice[4]
# (x,y) 좌표에서 시작
top = 1
bottom = 6
right = 3
left = 4
side1 = 2
side2 = 5
for i in range(k):
    # x,y -> op[i] 로 이동
    if op[i] == 1:
        # right가 바닥으로,
        # 동쪽으로 이동
        if 0<=y+1<m:
            bottom, right, top, left = right, top, left, bottom
            if arr[x][y+1] == 0:
                # 주사위 바닥면에 쓰여있는 수가 칸에 복사
                arr[x][y + 1] = dice[bottom]
            else:
                dice[bottom] = arr[x][y+1]
                arr[x][y + 1] = 0
            y += 1
            print(dice[top])
    elif op[i] == 2:
        # 서쪽으로 이동
        if 0<=y-1<m:
            bottom, left, top, right = left, top, right, bottom
            if arr[x][y-1] == 0:
                arr[x][y - 1] = dice[bottom]
            else:
                dice[bottom] = arr[x][y-1]
                arr[x][y - 1] = 0
            y -= 1
            print(dice[top])
    elif op[i] == 3:
        # 북쪽으로 이동
        if 0<=x-1<n:
            bottom, side2, top, side1 = side2, top, side1, bottom
            if arr[x-1][y] == 0:
                arr[x - 1][y] = dice[bottom]
            else:
                dice[bottom] = arr[x - 1][y]
                arr[x - 1][y] = 0
            x -= 1
            print(dice[top])
    else:
        # 남쪽
        if 0 <= x+1 < n:
            bottom, side1, top, side2 = side1, top, side2, bottom
            if arr[x + 1][y] == 0:
                arr[x + 1][y] = dice[bottom]
            else:
                dice[bottom] = arr[x + 1][y]
                arr[x + 1][y] = 0
            x += 1
            print(dice[top])



