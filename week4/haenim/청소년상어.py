'''
    목표: 상어가 먹을 수 있는 물고기 번호의 최댓값 구하기

    현재 상어가 먹을 수 있는 물고기 중에서 번호가 가장 높은 것을 먹는다고 해서
    그게 끝까지 최댓값이 된다고 확신할 수 없다.
    
    => 모든 경우에 대해서 끝까지 탐색이 필요하다

    => dfs

    진행 과정

    1. 현재 칸에 있는 물고기를 먹는다
    2. 1번 물고기부터 16번 물고기 까지 순서대로 물고기들이 움직인다
    3. 이동할 방향에 상어가 있거나 존재하지 않는 칸이면 45도 반시계 회전하고 움직인다
    4. 상어는 현재 방향으로 움직이면서 물고기를 먹는다 (한번에 여러칸 이동도 가능)
    
'''

import copy


#입력
tmp = [list(map(int, input().split())) for _ in range(4)]

lst = [[0]*4 for _ in range(4)]

# 다루기 쉽게 [값, 방향] 형태로 바꿈
for i in range(4):
    for j in range(4):
                                                   # 0 1  / 2 3 / 4 5 / 6 7    
        lst[i][j] = tmp[i][j*2], tmp[i][j*2 +1] -1 # 1 2 / 3 4 / 5 6 / 7 8

count = 0
print(lst)

# 화살표 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1] 

def move_fish(lst, x, y):
    flag = False
    position = None

    #1번 물고기부터 16번 물고기까지 움직임    
    for i in range(1, 17):# 1번 물고기부터 16번 물고기 까지 반복

        # 현재 물고기의 위치 찾기
        for j in range(4):
            for k in range(4):
                if lst[j][k][0] == i:
                    position = j,k

        if position == None: # 현재 물고기가 없으면
            continue # 다음 물고기를 움직임

        x, y = position[0], position[1]
        direct = lst[x][y][1] # 현재 물고기의 방향

        for j in range(8): # 각 방향에 대하여
            nx, ny =  x + dx[direct], y + dy[direct] # 이동할 위치

            if 0 <= nx < 4 and 0 <= ny <4:# 이동할 위치가 범위 내에 있고
                    if not nx == x and ny == y: # 다음으로 이동할 위치에 상어가 있는 게 아니면

                        # 현재 칸과 이동할 칸의 물고기의 위치를 서로 바꿈
                        lst[x][y][0], lst[nx][ny][0] = lst[nx][ny][0], lst[x][y][0]

                        # 방향도 서로 바꿈
                        lst[x][y][1], lst[nx][ny][1] = lst[nx][ny][1], direct

                        break # 반복문 탈출

            direct = (direct+1) % 8 # 3. 이 방향에서 물고기가 못움직였으면 방향을 45도 돌림


def find_possible_shark_pos(lst, x, y):
    positions = []
    derection = array[x][y][1] # 현재 상어의 방향

    for i in range(1,4):
        nx, ny = x + dx[direction], y + dy[direction] # 상어가 다음으로 이동할 위치

        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= lst[nx][ny][0] <= 16: #다음으로 이동할 위치가 범위 내에 있고 거기에 물고기가 존재한다면
            positions.append([nx,ny]) # 이동할 수 있는 위치에 추가

        x, y = nx, ny # 현재 위치를 이동한 위치로 바꿈

    return positions #상어가 이동할 수 있는 모든 위치를 전달
    
def solution(lst, x, y, curr_count):
    lst = copy.deepcopy(lst) #원본 데이터를 바꾸지 않기 위해 딥카피

    # 1. 현재 위치에 있는 물고기 먹음
    fish_number = lst[x][y][0] # 물고기 넘버(1~16)
    lst[x][y][0] = -1 #물고기를 먹어 없어짐

    # 2. 물고기 이동
    move_fish(lst, x, y) # x,y는 현재 상어가 있는 칸


    # 4. 현재 위치에서 상어가 이동할 수 있는 모든 위치 찾기
    possible_shark_pos = find_possible_shark_pos(lst, x, y) 

    # 현재 최댓값과 새로운 최댓값을 비교해서 물고기 번호의 합이 높은 걸 답으로 선택
    count = max(count, curr_count + fish_number) 
        
    # 5. 상어가 이동할 수 있는 모든 위치에 대해서 최댓값 탐색
    answer = nx, ny in possible_shark_pos:
        solution(lst, nx, ny, 

solution(arry, 0, 0, 0)
print(count)
