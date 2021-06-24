'''
swap 적극 활용하기
'''

n, m, x, y, k = map(int, input().split())  # 지도 크기, 주사위 좌표, 명령 갯수
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
graph[x][y] = 0
                              # 0,  1, 2,  3, 4,  5
dice = [0 for _ in range(6)]  # 위, 뒤, 오, 왼, 앞 아래
command = list(map(int, input().split()))

move = [[0, 1], [0, -1], [-1, 0], [1, 0]]

for c in command:  # 동 서 북 남
    c=c-1
    nx, ny=x+move[c][0], y+move[c][1]
    if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
    x, y = nx, ny

    if c==0: #앞, 뒤 고정
        dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]
    elif c==1: #앞, 뒤 고정
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif c==2: #왼, 오 고정
        dice[0], dice[4], dice[5], dice[1] = dice[4], dice[5], dice[1], dice[0]
    else: #왼, 오 고정
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]

    if graph[x][y]==0:
        graph[x][y]=dice[5]
    else:
        dice[5]=graph[x][y]
        graph[x][y]=0
    print(dice[0])
