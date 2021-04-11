# # 물고기들이 이동하는 함수 필요하고, 그때마다 상어가 또 이동해야 함. (재귀를 써야 하므로 DFS.)
# # 상어가 물고기를 선택하는 경우의 수가 다양할 수 있기 때문. 

import sys
sys.setrecursionlimit(2000)

import copy

graph = [[None]*4 for _ in range(4)]

for i in range(4):
    li = list(map(int, input().split()))
    for j in range(4):
        graph[i][j] = [li[j*2], li[j*2+1]-1] # 물고기 번호, 방향 순서 


dx = [-1, -1, 0, 1, 1, 1, 0, -1] # 나와 있는 순서대로 
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def find_fish(graph, idx): # 해당 물고기의 좌표를 찾는 함수. 숫자를 늘려가며 리턴받기 
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == idx:
                return (i, j)

def move_fish(graph, now_x, now_y): # 모든 물고기를 회전 및 이동시키는 함수
    for i in range(1, 17): # 1 - 16 
        loc = find_fish(graph, i) # location 
        
        if loc != None: # 물고기를 찾았으면, 
            x, y = loc[0], loc[1] # 물고기의 좌표 
            dir = graph[x][y][1] # 해당 물고기의 좌표를 참조해 물고기의 방향을 direction에 넣음 
    
            for _ in range(8):
                nx = x + dx[dir]
                ny = y + dy[dir]
                
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == now_x and ny == now_y): 
                        graph[x][y][1] = dir 
                        graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                        break

                dir = (dir+1)%8 # 방향 + 1 

def get_fishes(graph, now_x, now_y): # 상어가 먹을 수 있는 물고기들을 반환하는 함수 
    fish = []
    dir = graph[now_x][now_y][1]
    for  _ in range(4):
        now_x += dx[dir]
        now_y += dy[dir]
    
        if 0 <= now_x < 4 and 0 <= now_y < 4:
            if graph[now_x][now_y][0] != -1: # 물고기가 있으면 
                fish.append((now_x, now_y)) # 물고기들을 리스트에 담음 
    return fish

result = 0 
def dfs(graph, now_x, now_y, eat):
    global result
    graph = copy.deepcopy(graph)
    
    eat += graph[now_x][now_y][0] # 현재 위치의 물고기 먹고, 
    graph[now_x][now_y][0] = -1 #  -1로 그 자리를 메꿈 
    
    move_fish(graph, now_x, now_y) # 물고기 이동

    loc = get_fishes(graph, now_x, now_y)
     
    if len(loc) == 0: # 더 갈 곳이 없으면 
        result = max(result, eat) # 정답에 최댓값 넣음 
        return # 종료
    
    for nxt_x, nxt_y in loc:
        dfs(graph, nxt_x, nxt_y, eat)


dfs(graph, 0, 0, 0)

print(result)
