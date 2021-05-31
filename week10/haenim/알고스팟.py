"""
(x,y)에 알고스팟 운영진이 갇힘
벽을 부숴서 탈출하려고 하는데 최소 몇개 부숴야 하는 지

=> BFS, 다익스트라

O(n)
"""


import sys
import heapq


def dijkstra():
    hq = []
    heapq.heappush(hq, [0, 0, 0])  # 시작점
 

    while hq:
        cnt, x, y = heapq.heappop(hq)  # 벽 부순 횟수가 최소인 경우가 나옴

        if x == n - 1 and y == m - 1:  # 탈출했으면 종료
            return cnt

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
                
            if 0 <= nx < n and 0 <= ny < m: # 다음으로 이동할 장소가 범위내에 있으면
                nc = cnt + room[nx][ny] # 현재 벽부순 횟수 업데이트

                if nc < d[nx][ny]: # 지금 계산한 횟수가 최소 횟수보다 더 짧으면
                    d[nx][ny] = nc # 최소횟수 업데이트
                    heapq.heappush(hq,[nc, nx, ny])

m, n = map(int, input().split()) #미로 가로, 세로 크기
room = [list(map(int, input())) for _ in range(n)] #미로의 상태 0:빈 방 1:벽
d = [[sys.maxsize] * m for _ in range(n)] #출발점으로부터의 최단거리를 저장할 배열
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

print(dijkstra())
