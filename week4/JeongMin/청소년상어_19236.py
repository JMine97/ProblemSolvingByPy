'''''''''
맞았는데 가독성이 떨어져서
수정하겠습니다

잡아먹히면 []가 아니라 [0,0]을 넣었어야 됐는데 []를 넣어
배열 길이가 달라져 예외 잡느라 코드가 길어졌습니다
[0,0]을 넣는 것으로 고치려면 꽤 오래 걸릴 것 같아
이번주차 끝나고 수정하겠습니다
'''''''''


import sys
import copy

input = sys.stdin.readline

move = [[0, 0], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
fish = [[0, 0] for _ in range(17)]  # 인덱스 = 물고기 번호(상어 0번), 값 = 물고기 위치[r,c]
graph = [[] for _ in range(4)]  # 물고기 번호, 방향(빈칸일땐 그냥 0으로)
MAX_SUM = 0

for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(0, len(temp) - 1, 2):
        graph[i].append([temp[j], temp[j + 1]])
        fish[temp[j]] = [i, j // 2]


def move_fish(cfish, cgraph):
    while True:
        for i in range(1, 17):
            if len(cfish[i]) > 0:
                r, c = cfish[i]
                dir = cgraph[r][c][1]
                cnt = 1

                while True:
                    if cnt >= 9:
                        break
                    if dir > 8:
                        dir = 1
                    nr, nc = r+move[dir][0], c + move[dir][1]
                    # 범위 밖이거나 상어가 있으면 방향 바꿈
                    if nr > 3 or nr < 0 or nc > 3 or nc < 0 or (cfish[0][0] == nr and cfish[0][1] == nc):
                        dir += 1
                        cnt += 1
                        continue
                    cgraph[r][c][1] = dir
                    # 물고기와 위치를 바꾼다
                    if len(cgraph[nr][nc]) > 0:
                        j = cgraph[nr][nc][0]
                        cfish[i], cfish[j] = cfish[j], cfish[i]
                        cgraph[r][c], cgraph[nr][nc] = cgraph[nr][nc], cgraph[r][c]
                    else:
                        cfish[i] = [nr, nc]
                        cgraph[r][c], cgraph[nr][nc] = cgraph[nr][nc], cgraph[r][c]
                    break
        break
    return


# 상어가 계속 돎
def dfs(SUM, pfish, pgraph):
    # 종료조건
    # 이동할 수 있는 칸이 없을 때
    if pfish[0][0] > 3 or pfish[0][0] < 0 or pfish[0][1] > 3 or pfish[0][1] < 0 or len(
            pgraph[pfish[0][0]][pfish[0][1]]) == 0:  # 상어는 해당 자리에 물고기가 없으면 움직이지 못한다
        global MAX_SUM
        MAX_SUM = max(MAX_SUM, SUM)
        return

    cgraph = copy.deepcopy(pgraph)
    cfish = copy.deepcopy(pfish)

    rshark = cfish[0][0]
    cshark = cfish[0][1]

    # 상어가 물고기를 먹고 해당 물고기의 방향을 갖는다
    fish_num = cgraph[rshark][cshark][0]
    fish_dir = cgraph[rshark][cshark][1]

    cfish[fish_num] = []  # 잡아먹힘
    cgraph[rshark][cshark] = []

    # 물고기 이동
    move_fish(cfish, cgraph)

    # 상어가 이동할 수 있는 방향
    shark_can_go = []
    for _ in range(3):
        nr, nc = rshark + move[fish_dir][0], cshark + move[fish_dir][1]
        shark_can_go.append([nr, nc])
        rshark, cshark = nr, nc

    # shark가 다음에 갈 곳
    for i in shark_can_go:
        cfish[0] = i
        dfs(SUM + fish_num, cfish, cgraph)


dfs(0, fish, graph)
print(MAX_SUM)
