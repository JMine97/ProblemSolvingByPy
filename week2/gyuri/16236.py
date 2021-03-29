# 아기상어의 초기 크기는 2
# 아기상어 < 물고기 : 지날 수 없음
# 아기상어 == 칸을 이동 (먹을 순 없음)
# 아기상어 > 먹을 수 있다

# 먹은 물고기의 수 == 아기상어 크기 : 아기상어 =+ 1

# 가까운 물고기 먹는다
# 거리가 같은 경우 우선순위 : 위쪽,(여러마리 일 경우 가장 왼쪽)

# 1. 최단 경로 구하기 -> BFS 사용하기 (복잡도 O(v+e))
# 2. 지도, 위치정보 저장 자료구조 정하기
# 3. 상하좌우로 한칸씩 움직이기
# 4. 거리가 짧은 물고기가 여러마리일 경우 고려하기

from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y, weight, time, eat):
    q, can_eat = deque(), []                # 바로 먹지 않고 가장 가까운것부터 먹기 위해서 can_eat list에 저장한다. 
    q.append([x, y])
    c = [[-1] * n for _ in range(n)]        # visited 역할을 하는 list, 안에는 time (count)를 저장한다.
    c[x][y] = time
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if c[nx][ny] == -1:
                        if a[nx][ny] == 0 or a[nx][ny] == weight:
                            c[nx][ny] = c[x][y] + 1
                            q.append([nx, ny])
                        elif 0 < a[nx][ny] < weight:
                            can_eat.append([nx, ny])
            qlen -= 1

        if can_eat:
            nx, ny = min(can_eat)
            eat += 1
            if eat == weight:
                eat = 0
                weight += 1
            a[nx][ny] = 0
            return nx, ny, weight, c[x][y] + 1, eat
    print(time)
    sys.exit()

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            x, y = i, j
            a[i][j] = 0

weight, time, eat = 2, 0, 0
while True:
    x, y, weight, time, eat = bfs(x, y, weight, time, eat)
'''
1. 아기 상어의 좌표를 저장하고 0으로 초기화한다
2. 아기 상어 좌표, 무게, 이동 시간, 먹은 횟수를 bfs에 입력할 변수로 사용하고 초기화한다
3. 다음 칸이 0이거나 무게와 같은 칸이면 이동한다
4. 0과 아기 상어의 무게 사이라면 바로 먹지 않고 먹을 수 있는 물고기를 저장하는 can_eat에 저장
5. 먹을 수 있는 물고기가 있으면 그 중 최소값을 먹는다. 그래야 조건대로 가장 위, 가장 왼쪽에 있는 물고기를 먹는다
6. bfs 결과 더 이상 먹을게 없다면 입력한 시간을 출력
'''
