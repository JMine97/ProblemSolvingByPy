# 17780번_새로운 게임

# 체스판과 말을 이용해서 새로운 게임
# 체스판 : N * N, 말의 개수 : K
# 하나의 말 위에 다른 말을 올릴 수 있다.->함께이동
# 체스판은 3가지색  : 흰색, 빨간색, 파란색

# 게임은 체스판 위에 말 K개를 놓고 시작한다
# 말의 이동 방향은 미리정해져 있다. // 상하좌우
# 1~k번 말까지 이동
# 가장 아래에 있는 말만 이동 할 수 있다.

# 흰색인 경우
# 이동하려는 칸에 말이 이미 있는 경우 A번 말을 가장 위에 올려 놓는다
# A번 말 위에 말이 있으면 같이 이동

# 빨간색인 경우
# A번 말과 그 위에 모든 말의 쌓여 잇는 순서가 반대로 바뀐다
# 반대로 바뀌고 나서 이동

# 파란색인 경우 or 벗어나려고 하는 경우
# A번 말의 이동 방향을 반대로 하고 한 칸 이동한다.

# 0은 흰색, 1은 빨간색, 2는 파란색

import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(num):
    x, y, d = horse[num]
    # 맨 위일 경우에 만 실행되도록
    if num != horse_map[x][y][0]:
        return 0

    nx = x + dx[d]
    ny = y + dy[d]
    # 범위 밖일 경우 or 파란색일 경우
    if not 0 <= nx < n or not 0 <= ny < n or board[nx][ny] == 2:
        if 0 <= d <= 1:
            nd = (d+1) % 2
        else:
            nd = (d-1) % 2 + 2
        horse[num][2] = nd
        nx = x + dx[nd]
        ny = y + dy[nd]
        # 또 범위밖 or 파란색일 경우 방향만 바꾸고 위치는 안바꿈
        if not 0 <= nx < n or not 0 <= ny < n or board[nx][ny] == 2:
            return 0

    chess_set = []
    chess_set.extend(horse_map[x][y])
    horse_map[x][y] = []
    # 빨간색일 경우
    if board[nx][ny] == 1:
        # a[a:b:c] -> index a부터 index b까지 의 간격으로 배열을 만들어라
        # c가 음수라면 첫 index까지라는 으미
        chess_set = chess_set[::-1]

    for i in chess_set:
        horse_map[nx][ny].append(i)
        horse[i][:2] = [nx, ny]

    if len(horse_map[nx][ny]) >= 4:
        return 1
    return 0

n, k = map(int, input().split())
board= [list(map(int, input().split())) for _ in range(n)]
horse_map = [[[] for _ in range(n)] for _ in range(n)]
horse = [0 for _ in range(k)]

for i in range(k):
    x, y, d = map(int, input().split())
    horse_map[x-1][y-1].append(i)
    horse[i] = [x-1, y-1, d-1]

cnt = 1
while cnt <= 1000:
    for i in range(k):
        flag = move(i)
        if flag:
            print(cnt)
            sys.exit()
    cnt += 1
print(-1)
