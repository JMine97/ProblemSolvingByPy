import sys

input = sys.stdin.readline

move = [[0, 1], [0, -1], [-1, 0], [1, 0]]  # 오른쪽, 왼쪽, 위, 아래
n, k = map(int, input().split())  # 크기, 말 갯수

graph_color = []  # 칸의 색
chess = []  # [행,열,이동 방향]으로 정렬
locate_chess = [[[] for _ in range(n)] for _ in range(n)]  # 체스 쌓여있는
for _ in range(n):
    graph_color.append(list(map(int, input().split())))

for i in range(k):
    r, c, d = map(int, input().split())
    chess.append([r - 1, c - 1, d - 1])
    locate_chess[r - 1][c - 1].append(i)

cnt = 1

def move_chess(r, c, nr, nc):
    for i in range(len(locate_chess[r][c])):
        num = locate_chess[r][c][i]
        locate_chess[nr][nc].append(num)
        chess[num][0:2] = [nr, nc]
    del locate_chess[r][c][:]


flag = False
while cnt <= 1000:
    for i in range(k):
        r, c, d = chess[i]
        idx = locate_chess[r][c].index(i)
        # print(locate_chess[r][c], i)

        if idx == 0:  # 가장 아래에 있는 말만 이동할 수 있다
            nr, nc = r + move[d][0], c + move[d][1]
            if nr < 0 or nr >= n or nc < 0 or nc >= n or graph_color[nr][nc] == 2:
                # 2 파란색 & 범위 이탈 - 이동방향 반대로 한칸 이동
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                elif d == 3:
                    d = 2
                # if 이동하려는 칸이 파란색 : 방향만 반대로
                nr, nc = r + move[d][0], c + move[d][1]

                if 0 <= nr < n and 0 <= nc < n and graph_color[nr][nc] != 2:
                    if graph_color[nr][nc] == 0:
                        # 그냥 이동
                        # index 0이 제일 바닥
                        move_chess(r, c, nr, nc)

                    elif graph_color[nr][nc] == 1:  # 빨간색
                        # 이동 후 A번 말 포함 그 위의 말 순서 reverse
                        locate_chess[r][c].reverse()
                        move_chess(r, c, nr, nc)
                else:
                    nr, nc = r, c

                chess[i] = [nr, nc, d]

            elif graph_color[nr][nc] == 0:
                # 그냥 이동
                # index 0이 제일 바닥
                move_chess(r, c, nr, nc)

            elif graph_color[nr][nc] == 1:  # 빨간색
                # 이동 후 A번 말 포함 그 위의 말 순서 reverse
                locate_chess[r][c].reverse()
                move_chess(r, c, nr, nc)

            # 탈출조건
            # 턴이 진행되던 중 한 칸에 말이 4개 이상 쌓이면 게임 종료
            # 말 옮길때마다 탈출조건 체크
            if len(locate_chess[nr][nc]) >= 4:
                flag = True
                break
    if flag:
        break
    cnt += 1

if cnt > 1000:
    print(-1)
else:
    print(cnt)
