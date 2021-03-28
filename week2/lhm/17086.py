from collections import deque

lst = []
n,m = map(int, input().split())

dxs = [1,0,-1,0, -1,1, 1, -1]
dys = [0,1,0,-1, 1, -1,1, -1]

for i in range(n):
    lst.append(list(map(int, input().split())))

def solution(x,y):
    q = deque([(x,y,0)]) #x좌표, y좌표, 거리
    #visited = set([(x,y)]) #방문한 노드들
    visited = [[0]*m for _ in range(n)]
    distance = 0 #아기상어와의 거리
    

    while q:
        #for _ in range(len(q)):
            x,y,distance = q.popleft()

            #아기상어를 만났으면 끝냄
            if lst[x][y]:
                return distance

            distance += 1
            
            #상하 좌우 대각선으로 움직이면서 거리 찾기
            for dx, dy in zip(dxs, dys):
                x2, y2 = x+dx, y+dy
                if 0<= x2 < n and 0 <= y2 < m and not visited[x2][y2] :
                    q.append((x2,y2, distance))
                    #visited.add((x2,y2, distance))
                    visited[x2][y2] = 1
                                
            
    return distance


answer = 0
for i in range(n):
    for j in range(m):
        if not lst[i][j]:
            answer = max(solution(i,j), answer)
print(answer)
