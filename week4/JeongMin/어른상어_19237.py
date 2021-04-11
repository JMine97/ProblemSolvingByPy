'''
문제정리
n*n격자, m개의 칸에 상어, 냄새는 상어가 k번 이동하면 사라짐
냄새가 없는 칸으로, 그런 칸이 없으면 자신의 냄새가 있는 칸으로
방금 이동한 방향이 보고 있는 방향
수가 작은 상어가 더쎔
인덱스 항상 1부터 시작하자
'''

'''
방향이 주어진 문제는 bfs로 푸는 편이라 bfs를 이용했습니다
상어의 우선순위는 상어마다 key를 만들어 value에 리스트를 넣어 구현했습니다

상어의 번호와 냄새카운트를 담는 배열 graph, 
상어의 위치와 방향을 담는 배열 shark
'''

import sys
input=sys.stdin.readline

n, m, k = map(int, input().split())
move=[[0,0],[-1, 0],[1, 0],[0, -1], [0, 1]] #쓰레기값, 위, 아래, 왼쪽, 오른쪽
graph=[[[0]*2 for _ in range(n)] for _ in range(n)]  #[상어 번호, 냄새카운트]
shark=[[0,0,0] for _ in range(m+1)] #[상어의 위치, 상어의 방향] #쫓겨나면 [-1, -1]로 표시
shark_priority={} #현재 상어의 방향 : 상어의 방향 선호도
remain_shark=m #남은 상어의 수
time=0

#격자의 모습 n
for i in range(n):
    tmp=list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j]!=0:
            shark[tmp[j]][0], shark[tmp[j]][1]=i, j

#상어의 방향
tmp=list(map(int, input().split()))
for i in range(len(tmp)):
    shark[i+1][2]=tmp[i]

#상어의 우선순위
for i in range(1, m+1):
    tmp=[[0]]
    for j in range(4):
        tmp.append(list(map(int, input().split())))
    shark_priority[i]=tmp
# print(graph)
# print(shark)

def shark_move():
    # 1. 1초마다 모든 상어가 동시에 인접한 칸 중 하나로 이동, 냄새를 뿌린다
    #   한 칸에 여러마리가 들어가려고 하면 가장 작은 번호를 가진 상어를 제외하고 모두 내쫓는다
    #   이동방향은 1. 인접한 칸 중 아무 냄새가 없는 칸
    #            2. 그런 칸이 없으면 자신의 냄새가 있는 칸
    for i in range(1, len(shark)):
        if shark[i][0]==-1:
            continue
        r, c=shark[i][0], shark[i][1]
        dir=shark[i][2]
        mv=shark_priority[i][dir]
        j=0
        flag=False
        while True:
            # print(j)
            if j >3:
                j=0; flag=True

            m=mv[j]
            dr, dc = move[m][0], move[m][1]
            nr, nc = r+dr, c+dc

            if 0<=nr<n and 0<=nc<n:
                if graph[nr][nc][1]==0 or (flag and graph[nr][nc][0] == i):
                    #이동
                    shark[i]=[nr, nc, m]
                    break
            j+=1
    return


while time<=1000:
    #냄새를 뿌린다
    for i in range(1, len(shark)):
        if shark[i][0]==-1:
            continue
        r, c = shark[i][0], shark[i][1]
        if graph[r][c][1] ==0 or graph[r][c][0] ==i:
            graph[r][c] = [i, k]
        else:
            remain_shark -= 1
            shark[i] = [-1, -1, -1]

    # print(time)
    # print(shark)
    # [print(graph[i]) for i in range(n)]
    # print('--------')

    shark_move()

    #2. 냄새는 상어가 k번 이동하면 사라진다
    for i in range(n):
        for j in range(n):
            if graph[i][j][0]>0:
                graph[i][j][1]-=1
            if graph[i][j][1]==0:
                graph[i][j][0] = 0

    # 종료 조건
    if remain_shark == 1:
        break

    time += 1


#1번 상어만 격자에 남게 되기까지 걸리는 시간 출력
#1000초가 넘어도 다른 상어 있으면 -1 출력
if remain_shark!=1:
    print(-1)
else:
    print(time)
