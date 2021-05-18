"""
O(n^2)..??
"""

import sys
input = sys.stdin.readline
 
N, D = map(int, input().split()) # 지름길 개수, 고속도로 길이
lst = [[] for _ in range(10001)]

for _ in range(N):
    s, e, w = map(int, input().split()) # 지름길 시작위치, 도착위치, 지름길 길이
    lst[s].append([w, e]) #시작위치
distance = [i for i in range(D+1)] 
 
for i in range(D+1): #0부터 목적지 까지 반복
    if i != 0: #이전 지점 +1이 더 작다면 업데이트
        distance[i] = min(distance[i], distance[i-1]+1) 
    for w, e in lst[i]: #지름길이 있다면 
        if e <= D and distance[e] > w + distance[i]: #
            distance[e] = w + distance[i]
 
print(distance[D])

N, D = map(int, input().split())# 지름길 개수, 고속도로 길이
li = [list(map(int, input().split())) for _ in range(N)]
dis = [i for i in range(D+1)] #최단거리 테이블 생성

for i in range(D+1): #0부터 목적지 까지 반복
    if i > 0:
        dis[i] = min(dis[i], dis[i-1]+1) #이전 지점 +1이 더 작다면 업데이트
    for s, e, d in li:  #지름길 시작위치, 도착위치, 지름길 길이
        if i == s and e <= D and dis[i]+d < dis[e]: #현재 위치에 지름길이 있다면 업데이트
            dis[e] = dis[i]+d
print(dis[D])

