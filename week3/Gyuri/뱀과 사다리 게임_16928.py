# 뱀과 사다리 게임
# 주사위 조작해서 최소 횟수로 도착점에 도착

# 플레이어는 주사위를 굴려 나온 수만큼 이동
# 10 * 10 = 100개의 칸

# 조건
# 주사위를 굴린 결과 100번 칸을 넘어가면 이동할 수없다!
# 사다리 : 위로 올라간다.
# 뱀 : 아래로 내려간다

# 입력
# 사다리의 수, 뱀의 수
# N개의 줄 : 사다리의 정보 :  x,y (x번칸 -> y번 칸으로 이동)
# M개의 줄 : 뱀의 정보 : u,v(u번칸 -> v번째 칸으로 이동)

# 100은 뱀/ 사다리 아님

# 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
s = [0] * 101       # 칸에 사다리 or 뱀이 있으면 이동 자리, 없으면 0

for i in range(n):
    x, y = map(int, input().split())
    s[x] = y

for i in range(m):
    u, v = map(int, input().split())
    s[u] = v

deq = deque()
dist = [-1] * 101

# 시작은 1에서 하니깐 1 deque 에 넣기
deq.append(1)
# 시작은 만났으니깐 0으로 표시하기
dist[1] = 0

while deq :
    node = deq.popleft()
    # 방문 표시가 있으면 break
    if dist[100] != -1:
        break
    # 주사위 6가지
    for i in range(1, 7):
        next = node + i
        # 사다리가 있으면
        if next <= 100:
            if s[next] != 0:
                next = s[next]
            if dist[next] == -1:
                deq.append(next)
                dist[next] = dist[node] + 1
print(dist[100])

# 주사위 굴리는 최소 횟수,,?
