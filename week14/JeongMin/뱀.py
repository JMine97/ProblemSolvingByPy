##문제 열심히 읽기

'''
뱀은 (0,0)에 위치 길이는 1, 방향은 오른쪽
1. 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
3. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
final : 벽 or 자신의 몸과 부딪히면 게임 끝

L 왼쪽, D 오른쪽
빈칸 -1, 뱀 0, 1 ..., 사과 -4
'''

n=int(input())
k=int(input())
graph=[[-1]*n for _ in range(n)]
move=[[0, 1], [1, 0], [0, -1], [-1, 0]] #동 남 서 북 #L면 --, D면 ++

for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1]=-4

command=[]
for _ in range(int(input())):
    a, b = input().split()
    command.append([int(a), b])

snake=[[0, 0], [0, 0]] #머리, 꼬리
graph[0][0]=0
snake_dir=0
i=0

def next(tail):
    r, c=tail[0], tail[1]

    l=graph[r][c]
    for dr, dc in move:
        nr, nc=r+dr, c+dc
        if 0<=nr<n and 0<=nc<n and graph[nr][nc]==l+1:
            return [nr, nc]

while 1:
    i+=1
    head=snake[0] #r, c 순
    tail=snake[1]

    nr, nc=head[0]+move[snake_dir][0], head[1]+move[snake_dir][1]

    if 0<=nr<n and 0<=nc<n and graph[nr][nc]<0:
        tmp=graph[nr][nc]
        graph[nr][nc] = i
        head[0], head[1] = nr, nc
        #사과가 없을 때
        if tmp!=-4:
            #꼬리 줄이기
            nr_tail, nc_tail = next(tail)
            graph[tail[0]][tail[1]]=-1
            tail[0], tail[1] = nr_tail, nc_tail
    else:
        break

    if command and command[0][0]==i: #게임 시작 시간으로부터 X초가 끝난 뒤
        if command[0][1]=='D':
            snake_dir+=1
            if snake_dir>3:
                snake_dir=0
        else:
            snake_dir -= 1
            if snake_dir<0:
                snake_dir=3
        command.pop(0)
print(i)
