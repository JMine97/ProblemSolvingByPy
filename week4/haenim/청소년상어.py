'''
    목표: 상어가 먹을 수 있는 물고기 번호의 최댓값 구하기

    ---------------------------------------------------------------------
    
    접근 방법:

    현재 상어가 먹을 수 있는 물고기 중에서 번호가 가장 높은 것 만을 먹었을 때 최대가 되나?

    => 현재 번호가 가장 높은 것을 먹는다고 해서 그게 끝까지 최댓값이 된다고 확신할 수 없다.
    
    => 모든 경우에 대해서 끝까지 탐색이 필요하다

    => dfs

    ----------------------------------------------------------------------

    진행 과정

    1. 현재 칸에 있는 물고기를 먹는다
    2. 1번 부터 16번 물고기 까지 순서대로 물고기들이 움직인다
    3. 이동할 방향에 상어가 있거나 존재하지 않는 칸이면 45도 반시계 회전하고 움직인다
    4. 상어는 현재 방향으로 움직이면서 물고기를 먹는다 (한 번에 여러칸 이동도 가능)
    
'''

import copy


# 화살표 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None

def move_fish(lst, x, y):
    position = []

    #모든 물고기들을 움직임    
    for i in range(1, 17):# 1번 물고기부터 16번 물고기 까지 반복

        # i번 물고기의 위치 찾기
        position = find_fish(lst,i)

        if position == None: # i번 물고기가 없으면
            continue # 다음 물고기를 움직임

        x1, y1 = position[0], position[1] # i번 물고기의 위치 저장
        direct = lst[x1][y1][1] # i번 물고기의 방향

        for j in range(8): # 각 방향에 대하여
            nx, ny =  x1 + dx[direct], y1 + dy[direct] # 이동할 위치

            if 0 <= nx < 4 and 0 <= ny <4: # 이동할 위치가 범위 내에 있고
                    if not (nx == x and ny == y): # 다음으로 이동할 위치에 상어가 있는 게 아니면

                        # 현재 칸과 이동할 칸의 물고기의 위치를 서로 바꿈
                        lst[x1][y1][0], lst[nx][ny][0] = lst[nx][ny][0], lst[x1][y1][0]

                        # 방향도 서로 바꿈
                        lst[x1][y1][1], lst[nx][ny][1] = lst[nx][ny][1], direct

                        break # 반복문 탈출

            direct = (direct+1) % 8 # 3. 이 방향에서 물고기가 못움직였으면 방향을 45도 돌림


def find_possible_shark_pos(lst, x, y):
    positions = [] # 상어가 이동할 수 있는 모든 위치를 저장
    direction = lst[x][y][1] # 현재 상어의 방향

    for i in range(1,4):
        nx, ny = x + dx[direction], y + dy[direction] # 상어가 다음으로 이동할 위치

        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= lst[nx][ny][0] <= 16: # 다음으로 이동할 위치가 범위 내에 있고 거기에 물고기가 존재한다면
            positions.append([nx,ny]) # 이동할 수 있는 위치에 추가

        x, y = nx, ny # 현재 위치를 이동한 위치로 바꿈
        
    return positions #상어가 이동할 수 있는 모든 위치를 전달
    
def dfs(lst, x, y, total):
    global answer
    
    lst = copy.deepcopy(lst) #원본 데이터를 바꾸지 않기 위해 딥카피

    # 1. 현재 위치에 있는 물고기 먹음
    fish_number = lst[x][y][0] # 물고기 넘버(1~16)
    lst[x][y][0] = -1 #물고기를 먹어 없어짐

    # 2. 물고기 이동
    move_fish(lst, x, y) # x,y는 현재 상어가 있는 칸

    # 4. 현재 위치에서 상어가 이동할 수 있는 모든 위치 찾기
    possible_shark_pos = find_possible_shark_pos(lst, x, y)

    # 현재까지의 최댓값과 지금의 물고기 번호 합을 비교해서 물고기 번호의 합이 높은 걸 답으로 업데이트
    answer = max(answer, total + fish_number) 
        
    # 5. 상어가 이동할 수 있는 모든 위치에 대해서 최댓값 탐색
    for nx, ny in possible_shark_pos :
        dfs(lst, nx, ny, total + fish_number)


        
# 입력
tmp = [list(map(int, input().split())) for _ in range(4)]
'''
4 x 8

16 7 1 4 4 3 12 8

14 7 7 6 3 4 10 2

5 2 15 2 8 3 6 4

11 8 2 4 13 5 9 4

'''

# 다루기 쉽게 [물고기 번호, 방향] 형태로 바꿈
lst = [[None]*4 for _ in range(4)]

for i in range(4):
    for j in range(4):
                                                     #  0 1  / 2 3 / 4 5 / 6 7    
        lst[i][j] = [tmp[i][j*2], tmp[i][j*2 +1] -1] # 16 7 / 1 4 / 4 3 / 12 8


'''
[ [[16, 6], [1, 3], [4, 2], [12, 7]],

  [[14, 6], [7, 5], [3, 3], [10, 1]],

  [[5, 1], [15, 1], [8, 2], [6, 3]],

  [[11, 7], [2, 3], [13, 4], [9, 3]]  ]

'''

answer = 0 # 물고기 번호의 최댓값
dfs(lst, 0, 0, 0) # 리스트, x좌표, y좌표, 현재 먹은 물고기 번호 총 합
print(answer)
